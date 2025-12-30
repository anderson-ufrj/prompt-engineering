#!/usr/bin/env python3
"""
Tests for Interaction Metrics Analyzer
Author: Anderson Henrique da Silva
Location: Minas Gerais, Brazil
"""

import pytest
import json
import tempfile
from pathlib import Path
from datetime import datetime
import sys
import os

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from evidence.metrics.interaction_analyzer import (
    InteractionMetrics, 
    MetricsCollector
)

class TestInteractionMetrics:
    """Test cases for InteractionMetrics dataclass"""
    
    def test_interaction_metrics_creation(self):
        """Test basic creation of InteractionMetrics"""
        metrics = InteractionMetrics(
            timestamp=datetime.now().isoformat(),
            prompt_tokens=150,
            response_tokens=280,
            response_time_ms=1200,
            quality_score=0.85,
            iteration_count=1,
            context_used=["anderson-skill", "debugging"],
            pattern_applied="chain",
            success_indicators=["task_completed", "no_followup_needed"]
        )
        
        assert metrics.prompt_tokens == 150
        assert metrics.response_tokens == 280
        assert metrics.quality_score == 0.85
        assert metrics.iteration_count == 1
        assert "anderson-skill" in metrics.context_used
        
    def test_interaction_metrics_validation(self):
        """Test validation of metric values"""
        with pytest.raises(ValueError):
            # Quality score should be between 0 and 1
            InteractionMetrics(
                timestamp=datetime.now().isoformat(),
                prompt_tokens=150,
                response_tokens=280,
                response_time_ms=1200,
                quality_score=1.5,  # Invalid
                iteration_count=1,
                context_used=["anderson-skill"]
            )

class TestMetricsCollector:
    """Test cases for MetricsCollector class"""
    
    @pytest.fixture
    def temp_storage(self):
        """Create temporary storage for testing"""
        with tempfile.TemporaryDirectory() as tmpdir:
            yield Path(tmpdir)
    
    @pytest.fixture
    def collector(self, temp_storage):
        """Create MetricsCollector with temp storage"""
        return MetricsCollector(storage_path=temp_storage)
    
    def test_capture_interaction(self, collector):
        """Test capturing a single interaction"""
        metrics = InteractionMetrics(
            timestamp=datetime.now().isoformat(),
            prompt_tokens=150,
            response_tokens=280,
            response_time_ms=1200,
            quality_score=0.85,
            iteration_count=1,
            context_used=["anderson-skill", "debugging"]
        )
        
        interaction_id = collector.capture_interaction(metrics)
        
        assert interaction_id is not None
        assert len(interaction_id) == 8  # MD5 hash truncated to 8 chars
        
        # Verify file was created
        expected_file = collector.storage_path / f"{interaction_id}.json"
        assert expected_file.exists()
        
        # Verify content
        with open(expected_file) as f:
            saved_data = json.load(f)
            assert saved_data['prompt_tokens'] == 150
            assert saved_data['quality_score'] == 0.85
    
    def test_generate_report_empty_data(self, collector):
        """Test report generation with no data"""
        report = collector.generate_report(days=7)
        
        assert 'error' in report
        assert 'No interactions found' in report['error']
    
    def test_generate_report_with_data(self, collector):
        """Test report generation with sample data"""
        # Create multiple interactions
        for i in range(3):
            metrics = InteractionMetrics(
                timestamp=datetime.now().isoformat(),
                prompt_tokens=100 + i * 50,
                response_tokens=200 + i * 40,
                response_time_ms=1000 + i * 200,
                quality_score=0.7 + i * 0.1,
                iteration_count=1 + i,
                context_used=["anderson-skill", f"test-{i}"]
            )
            collector.capture_interaction(metrics)
        
        report = collector.generate_report(days=7)
        
        assert 'error' not in report
        assert report['total_interactions'] == 3
        assert report['avg_quality_score'] > 0
        assert report['avg_response_time'] > 0
        assert 'top_patterns' in report
        assert 'quality_distribution' in report
        assert 'recommendations' in report
    
    def test_quality_distribution_calculation(self, collector):
        """Test quality distribution calculation"""
        # Create interactions with different quality scores
        quality_scores = [0.9, 0.8, 0.7, 0.6, 0.4]
        for score in quality_scores:
            metrics = InteractionMetrics(
                timestamp=datetime.now().isoformat(),
                prompt_tokens=150,
                response_tokens=280,
                response_time_ms=1200,
                quality_score=score,
                iteration_count=1,
                context_used=["anderson-skill"]
            )
            collector.capture_interaction(metrics)
        
        report = collector.generate_report(days=7)
        distribution = report['quality_distribution']
        
        # Should have high, medium, low categories
        assert 'high' in distribution
        assert 'medium' in distribution
        assert 'low' in distribution
        
        # Based on our scores: 0.9, 0.8 (high), 0.7, 0.6 (medium), 0.4 (low)
        assert distribution['high'] == 2
        assert distribution['medium'] == 2
        assert distribution['low'] == 1
    
    def test_recommendations_generation(self, collector):
        """Test recommendations generation logic"""
        # Create low-quality interactions
        for _ in range(3):
            metrics = InteractionMetrics(
                timestamp=datetime.now().isoformat(),
                prompt_tokens=150,
                response_tokens=280,
                response_time_ms=1200,
                quality_score=0.5,  # Low quality
                iteration_count=3,  # High iterations
                context_used=["anderson-skill"]
            )
            collector.capture_interaction(metrics)
        
        report = collector.generate_report(days=7)
        recommendations = report['recommendations']
        
        # Should have recommendations for low quality and high iterations
        assert len(recommendations) > 0
        
        quality_rec = any("quality" in rec.lower() for rec in recommendations)
        iteration_rec = any("iteration" in rec.lower() for rec in recommendations)
        
        assert quality_rec or iteration_rec, "Should have quality or iteration recommendations"
    
    def test_data_persistence(self, collector):
        """Test that data persists across collector instances"""
        metrics = InteractionMetrics(
            timestamp=datetime.now().isoformat(),
            prompt_tokens=150,
            response_tokens=280,
            response_time_ms=1200,
            quality_score=0.85,
            iteration_count=1,
            context_used=["anderson-skill"]
        )
        
        interaction_id = collector.capture_interaction(metrics)
        
        # Create new collector instance with same storage
        new_collector = MetricsCollector(storage_path=collector.storage_path)
        report = new_collector.generate_report(days=7)
        
        assert report['total_interactions'] == 1
        assert report['avg_quality_score'] == 0.85
    
    def test_old_data_exclusion(self, collector):
        """Test that old data is excluded from reports"""
        # Create old interaction (outside report window)
        old_timestamp = (datetime.now() - timedelta(days=10)).isoformat()
        old_metrics = InteractionMetrics(
            timestamp=old_timestamp,
            prompt_tokens=150,
            response_tokens=280,
            response_time_ms=1200,
            quality_score=0.95,
            iteration_count=1,
            context_used=["anderson-skill"]
        )
        collector.capture_interaction(old_metrics)
        
        # Create recent interaction
        recent_metrics = InteractionMetrics(
            timestamp=datetime.now().isoformat(),
            prompt_tokens=150,
            response_tokens=280,
            response_time_ms=1200,
            quality_score=0.75,
            iteration_count=1,
            context_used=["anderson-skill"]
        )
        collector.capture_interaction(recent_metrics)
        
        # Generate report for last 7 days
        report = collector.generate_report(days=7)
        
        # Should only include recent interaction
        assert report['total_interactions'] == 1
        assert report['avg_quality_score'] == 0.75  # Not 0.95 from old data

class TestIntegration:
    """Integration tests for the complete workflow"""
    
    def test_complete_workflow(self):
        """Test complete interaction capture and reporting workflow"""
        with tempfile.TemporaryDirectory() as tmpdir:
            storage_path = Path(tmpdir)
            collector = MetricsCollector(storage_path=storage_path)
            
            # Simulate real interaction sequence
            interactions = [
                {
                    "prompt_tokens": 120,
                    "response_tokens": 250,
                    "response_time_ms": 1100,
                    "quality_score": 0.85,
                    "iteration_count": 1,
                    "context_used": ["anderson-skill", "debugging"],
                    "pattern_applied": "chain"
                },
                {
                    "prompt_tokens": 200,
                    "response_tokens": 400,
                    "response_time_ms": 1800,
                    "quality_score": 0.72,
                    "iteration_count": 2,
                    "context_used": ["anderson-skill", "brainstorming"],
                    "pattern_applied": "parallel"
                },
                {
                    "prompt_tokens": 180,
                    "response_tokens": 320,
                    "response_time_ms": 1500,
                    "quality_score": 0.91,
                    "iteration_count": 1,
                    "context_used": ["anderson-skill", "code-review"],
                    "pattern_applied": "evaluator"
                }
            ]
            
            # Capture all interactions
            for interaction_data in interactions:
                metrics = InteractionMetrics(
                    timestamp=datetime.now().isoformat(),
                    **interaction_data
                )
                collector.capture_interaction(metrics)
            
            # Generate comprehensive report
            report = collector.generate_report(days=7)
            
            # Verify report accuracy
            assert report['total_interactions'] == 3
            expected_avg_quality = sum(i['quality_score'] for i in interactions) / 3
            assert abs(report['avg_quality_score'] - expected_avg_quality) < 0.01
            
            # Verify pattern analysis
            assert 'chain' in report['top_patterns']
            assert 'parallel' in report['top_patterns']
            
            # Verify recommendations
            assert len(report['recommendations']) > 0

if __name__ == "__main__":
    pytest.main([__file__, "-v"])