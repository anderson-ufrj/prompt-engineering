#!/usr/bin/env python3
"""
Tests for Experiment Runner
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

from src.experiments.experiment_runner import (
    Experiment,
    ExperimentVariant,
    ExperimentRunner
)

class TestExperimentVariant:
    """Test cases for ExperimentVariant dataclass"""
    
    def test_variant_creation(self):
        """Test basic creation of ExperimentVariant"""
        variant = ExperimentVariant(
            id="v1-test",
            name="Test Variant",
            prompt_template="Test prompt template",
            context_modifiers=["modifier1", "modifier2"],
            expected_outcome="Better performance",
            success_criteria=["quality_score > 0.8", "iteration_count < 2"]
        )
        
        assert variant.id == "v1-test"
        assert variant.name == "Test Variant"
        assert len(variant.context_modifiers) == 2
        assert len(variant.success_criteria) == 2

class TestExperiment:
    """Test cases for Experiment dataclass"""
    
    def test_experiment_creation(self):
        """Test basic creation of Experiment"""
        variants = [
            ExperimentVariant(
                id="control",
                name="Control",
                prompt_template="Standard prompt",
                context_modifiers=[],
                expected_outcome="Baseline",
                success_criteria=["quality_score > 0.7"]
            ),
            ExperimentVariant(
                id="treatment",
                name="Treatment",
                prompt_template="Enhanced prompt",
                context_modifiers=["examples", "specificity"],
                expected_outcome="Improved quality",
                success_criteria=["quality_score > 0.8"]
            )
        ]
        
        experiment = Experiment(
            id="exp-001",
            name="Prompt Enhancement Test",
            hypothesis="Adding examples improves quality by 15%",
            variants=variants,
            control_variant="control",
            metrics_to_track=["quality_score", "response_time", "iteration_count"],
            sample_size=100
        )
        
        assert experiment.id == "exp-001"
        assert experiment.name == "Prompt Enhancement Test"
        assert len(experiment.variants) == 2
        assert experiment.control_variant == "control"
        assert experiment.sample_size == 100
        assert experiment.status == "draft"
    
    def test_experiment_auto_timestamp(self):
        """Test that created_at is automatically set"""
        experiment = Experiment(
            id="test",
            name="Test",
            hypothesis="Test hypothesis",
            variants=[],
            control_variant="control",
            metrics_to_track=[],
            sample_size=10
        )
        
        assert experiment.created_at is not None
        # Should be recent (within last minute)
        created_time = datetime.fromisoformat(experiment.created_at)
        assert (datetime.now() - created_time).seconds < 60

class TestExperimentRunner:
    """Test cases for ExperimentRunner class"""
    
    @pytest.fixture
    def temp_base_path(self):
        """Create temporary base path for testing"""
        with tempfile.TemporaryDirectory() as tmpdir:
            yield Path(tmpdir)
    
    @pytest.fixture
    def runner(self, temp_base_path):
        """Create ExperimentRunner with temp paths"""
        return ExperimentRunner(base_path=temp_base_path)
    
    def test_create_experiment(self, runner):
        """Test experiment creation"""
        experiment = Experiment(
            id="test-exp-001",
            name="Test Experiment",
            hypothesis="Test hypothesis",
            variants=[
                ExperimentVariant(
                    id="control",
                    name="Control",
                    prompt_template="Standard",
                    context_modifiers=[],
                    expected_outcome="Baseline",
                    success_criteria=["quality > 0.7"]
                )
            ],
            control_variant="control",
            metrics_to_track=["quality"],
            sample_size=50
        )
        
        experiment_id = runner.create_experiment(experiment)
        
        assert experiment_id == "test-exp-001"
        
        # Verify file was created
        exp_file = runner.hypothesis_path / f"{experiment_id}.json"
        assert exp_file.exists()
        
        # Verify content
        with open(exp_file) as f:
            saved_data = json.load(f)
            assert saved_data['id'] == "test-exp-001"
            assert saved_data['name'] == "Test Experiment"
            assert saved_data['sample_size'] == 50
    
    def test_run_experiment_not_found(self, runner):
        """Test running non-existent experiment"""
        results = runner.run_experiment("non-existent")
        
        assert 'error' in results
        assert 'Experiment not found' in results['error']
    
    def test_run_experiment_success(self, runner):
        """Test successful experiment execution"""
        # Create experiment
        experiment = Experiment(
            id="success-test",
            name="Success Test",
            hypothesis="This will work",
            variants=[
                ExperimentVariant(
                    id="control",
                    name="Control",
                    prompt_template="Standard prompt",
                    context_modifiers=[],
                    expected_outcome="Baseline performance",
                    success_criteria=["quality_score > 0.7"]
                ),
                ExperimentVariant(
                    id="treatment",
                    name="Treatment",
                    prompt_template="Enhanced prompt",
                    context_modifiers=["examples"],
                    expected_outcome="Improved performance",
                    success_criteria=["quality_score > 0.8"]
                )
            ],
            control_variant="control",
            metrics_to_track=["quality_score", "response_time", "user_satisfaction"],
            sample_size=100
        )
        
        runner.create_experiment(experiment)
        results = runner.run_experiment("success-test")
        
        # Verify results structure
        assert results['experiment_id'] == "success-test"
        assert 'started_at' in results
        assert 'completed_at' in results
        assert 'variant_results' in results
        assert 'statistical_significance' in results
        assert 'winner' in results
        assert 'confidence_level' in results
        
        # Should have results for both variants
        assert len(results['variant_results']) == 2
        assert 'control' in results['variant_results']
        assert 'treatment' in results['variant_results']
        
        # Verify variant results structure
        control_results = results['variant_results']['control']
        assert 'total_interactions' in control_results
        assert 'success_rate' in control_results
        assert 'avg_quality_score' in control_results
        assert 'avg_response_time' in control_results
    
    def test_statistical_analysis(self, runner):
        """Test statistical analysis logic"""
        # Create experiment with multiple variants
        experiment = Experiment(
            id="stats-test",
            name="Statistical Test",
            hypothesis="Multiple variants test",
            variants=[
                ExperimentVariant(
                    id="v1",
                    name="Variant 1",
                    prompt_template="Prompt 1",
                    context_modifiers=[],
                    expected_outcome="Good",
                    success_criteria=["quality > 0.7"]
                ),
                ExperimentVariant(
                    id="v2",
                    name="Variant 2",
                    prompt_template="Prompt 2",
                    context_modifiers=["modifier"],
                    expected_outcome="Better",
                    success_criteria=["quality > 0.8"]
                ),
                ExperimentVariant(
                    id="v3",
                    name="Variant 3",
                    prompt_template="Prompt 3",
                    context_modifiers=["modifier1", "modifier2"],
                    expected_outcome="Best",
                    success_criteria=["quality > 0.9"]
                )
            ],
            control_variant="v1",
            metrics_to_track=["quality_score"],
            sample_size=50
        )
        
        runner.create_experiment(experiment)
        results = runner.run_experiment("stats-test")
        
        # Should have a winner
        assert results['winner'] is not None
        assert results['winner'] in ['v1', 'v2', 'v3']
        
        # Should have confidence level
        assert 0 <= results['confidence_level'] <= 1
        
        # Should determine statistical significance
        assert isinstance(results['statistical_significance'], bool)
    
    def test_generate_experiment_report(self, runner):
        """Test report generation"""
        # Create and run experiment
        experiment = Experiment(
            id="report-test",
            name="Report Test",
            hypothesis="Testing report generation",
            variants=[
                ExperimentVariant(
                    id="control",
                    name="Control Group",
                    prompt_template="Standard approach",
                    context_modifiers=[],
                    expected_outcome="Baseline",
                    success_criteria=["quality_score > 0.7", "iteration_count < 2"]
                )
            ],
            control_variant="control",
            metrics_to_track=["quality_score", "iteration_count"],
            sample_size=75
        )
        
        runner.create_experiment(experiment)
        runner.run_experiment("report-test")
        
        report = runner.generate_experiment_report("report-test")
        
        # Verify report content
        assert "Experiment Report: Report Test" in report
        assert "Hypothesis" in report
        assert "Testing report generation" in report
        assert "Results Summary" in report
        assert "Variant Performance" in report
        assert "Control Group" in report
        assert "Success Rate:" in report
        assert "Quality Score:" in report
        assert "Conclusion" in report
    
    def test_experiment_report_without_results(self, runner):
        """Test report generation without running experiment"""
        experiment = Experiment(
            id="no-results-test",
            name="No Results Test",
            hypothesis="No results yet",
            variants=[],
            control_variant="",
            metrics_to_track=[],
            sample_size=10
        )
        
        runner.create_experiment(experiment)
        report = runner.generate_experiment_report("no-results-test")
        
        assert report == "Experiment results not found"
    
    def test_single_variant_experiment(self, runner):
        """Test experiment with only one variant (should fail analysis)"""
        experiment = Experiment(
            id="single-variant",
            name="Single Variant",
            hypothesis="Only one variant",
            variants=[
                ExperimentVariant(
                    id="only-one",
                    name="Only Variant",
                    prompt_template="Single prompt",
                    context_modifiers=[],
                    expected_outcome="Solo",
                    success_criteria=["quality > 0.5"]
                )
            ],
            control_variant="only-one",
            metrics_to_track=["quality"],
            sample_size=30
        )
        
        runner.create_experiment(experiment)
        results = runner.run_experiment("single-variant")
        
        # Should indicate need for more variants
        assert 'error' in results
        assert 'Need at least 2 variants for analysis' in results['error']

class TestIntegration:
    """Integration tests for complete experiment workflow"""
    
    def test_complete_experiment_workflow(self):
        """Test complete experiment lifecycle"""
        with tempfile.TemporaryDirectory() as tmpdir:
            base_path = Path(tmpdir)
            runner = ExperimentRunner(base_path=base_path)
            
            # Create realistic experiment
            experiment = Experiment(
                id="real-world-test",
                name="Context Length Impact",
                hypothesis="Shorter context improves response time without quality loss",
                variants=[
                    ExperimentVariant(
                        id="long-context",
                        name="Long Context",
                        prompt_template="Full context with detailed background information",
                        context_modifiers=["full_context", "detailed_background"],
                        expected_outcome="High quality but slower",
                        success_criteria=["quality_score > 0.85", "response_time < 2000"]
                    ),
                    ExperimentVariant(
                        id="short-context",
                        name="Short Context",
                        prompt_template="Essential context only",
                        context_modifiers=["essential_only", "minimal_background"],
                        expected_outcome="Faster response with good quality",
                        success_criteria=["quality_score > 0.80", "response_time < 1500"]
                    ),
                    ExperimentVariant(
                        id="adaptive-context",
                        name="Adaptive Context",
                        prompt_template="Context adapted to task complexity",
                        context_modifiers=["adaptive", "complexity_based"],
                        expected_outcome="Optimal balance",
                        success_criteria=["quality_score > 0.82", "response_time < 1700"]
                    )
                ],
                control_variant="long-context",
                metrics_to_track=["quality_score", "response_time", "iteration_count", "user_satisfaction"],
                sample_size=150
            )
            
            # Create experiment
            exp_id = runner.create_experiment(experiment)
            assert exp_id == "real-world-test"
            
            # Verify experiment was saved
            exp_file = runner.hypothesis_path / f"{exp_id}.json"
            assert exp_file.exists()
            
            with open(exp_file) as f:
                saved_exp = json.load(f)
                assert saved_exp['hypothesis'] == experiment.hypothesis
                assert len(saved_exp['variants']) == 3
            
            # Run experiment
            results = runner.run_experiment(exp_id)
            
            # Verify results
            assert results['experiment_id'] == exp_id
            assert 'winner' in results
            assert results['winner'] in ['long-context', 'short-context', 'adaptive-context']
            assert 'confidence_level' in results
            assert 0 <= results['confidence_level'] <= 1
            
            # Verify all variants have results
            assert len(results['variant_results']) == 3
            for variant_id in ['long-context', 'short-context', 'adaptive-context']:
                assert variant_id in results['variant_results']
                variant_result = results['variant_results'][variant_id]
                assert 'success_rate' in variant_result
                assert 'avg_quality_score' in variant_result
                assert 'avg_response_time' in variant_result
            
            # Generate and verify report
            report = runner.generate_experiment_report(exp_id)
            assert "Context Length Impact" in report
            assert "Shorter context improves response time" in report
            assert "Winner:" in report
            assert "Confidence Level:" in report
            
            # Verify results were saved
            result_file = runner.results_path / f"{exp_id}_results.json"
            assert result_file.exists()

if __name__ == "__main__":
    pytest.main([__file__, "-v"])