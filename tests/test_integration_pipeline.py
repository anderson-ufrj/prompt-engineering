#!/usr/bin/env python3
"""
Tests for Integration Pipeline
Author: Anderson Henrique da Silva
Location: Minas Gerais, Brazil
"""

import pytest
import json
import tempfile
from pathlib import Path
from datetime import datetime
from unittest.mock import patch, MagicMock
import sys

sys.path.append(str(Path(__file__).parent.parent))

from integration_pipeline import IntegrationPipeline


class TestIntegrationPipeline:
    """Test cases for IntegrationPipeline class"""

    @pytest.fixture
    def mock_components(self):
        """Mock all pipeline components"""
        with patch('integration_pipeline.MetricsCollector') as mock_mc, \
             patch('integration_pipeline.ExperimentRunner') as mock_er, \
             patch('integration_pipeline.AutoCalibrationEngine') as mock_ace, \
             patch('integration_pipeline.PerformanceDashboard') as mock_pd, \
             patch('integration_pipeline.VersionManager') as mock_vm:

            yield {
                'metrics_collector': mock_mc.return_value,
                'experiment_runner': mock_er.return_value,
                'calibration_engine': mock_ace.return_value,
                'dashboard': mock_pd.return_value,
                'version_manager': mock_vm.return_value
            }

    @pytest.fixture
    def pipeline(self, mock_components):
        """Create pipeline with mocked components"""
        return IntegrationPipeline()

    def test_pipeline_initialization(self, pipeline):
        """Test pipeline initializes with correct defaults"""
        assert pipeline.min_interactions_for_training == 50
        assert pipeline.min_experiment_duration_days == 7
        assert pipeline.auto_calibration_threshold == 0.7

    def test_determine_success_indicators_high_quality(self, pipeline):
        """Test success indicators for high quality score"""
        indicators = pipeline._determine_success_indicators(0.9)

        assert "task_completed" in indicators
        assert "no_followup_needed" in indicators
        assert "user_satisfied" in indicators

    def test_determine_success_indicators_medium_quality(self, pipeline):
        """Test success indicators for medium quality score"""
        indicators = pipeline._determine_success_indicators(0.7)

        assert "task_completed" in indicators
        assert "minor_followup_needed" in indicators

    def test_determine_success_indicators_low_quality(self, pipeline):
        """Test success indicators for low quality score"""
        indicators = pipeline._determine_success_indicators(0.4)

        assert "task_incomplete" in indicators
        assert "major_revisions_needed" in indicators

    def test_collect_interaction(self, pipeline, mock_components):
        """Test interaction collection"""
        mock_components['metrics_collector'].capture_interaction.return_value = "test-id-123"

        interaction_id = pipeline.collect_interaction(
            prompt_tokens=100,
            response_tokens=200,
            response_time_ms=1500,
            quality_score=0.85,
            iteration_count=1,
            context_used=["anderson-skill", "debugging"],
            pattern_applied="chain"
        )

        assert interaction_id == "test-id-123"
        mock_components['metrics_collector'].capture_interaction.assert_called_once()

    def test_collect_interaction_auto_success_indicators(self, pipeline, mock_components):
        """Test that success indicators are auto-generated when not provided"""
        mock_components['metrics_collector'].capture_interaction.return_value = "test-id"

        pipeline.collect_interaction(
            prompt_tokens=100,
            response_tokens=200,
            response_time_ms=1500,
            quality_score=0.85,
            iteration_count=1,
            context_used=["anderson-skill"]
        )

        # Verify capture_interaction was called with auto-generated indicators
        call_args = mock_components['metrics_collector'].capture_interaction.call_args
        metrics = call_args[0][0]
        assert "task_completed" in metrics.success_indicators

    def test_run_health_check_healthy(self, pipeline, mock_components):
        """Test health check with healthy system"""
        mock_components['metrics_collector'].generate_report.return_value = {
            'total_interactions': 100,
            'avg_quality_score': 0.85
        }

        health = pipeline.run_health_check()

        assert health['overall_status'] == 'healthy'
        assert 'components' in health
        assert health['components']['metrics_collection']['status'] == 'operational'

    def test_run_health_check_no_data(self, pipeline, mock_components):
        """Test health check with no data"""
        mock_components['metrics_collector'].generate_report.return_value = {
            'error': 'No interactions found'
        }

        health = pipeline.run_health_check()

        assert health['components']['metrics_collection']['status'] == 'no_data'

    def test_run_health_check_low_quality_recommendation(self, pipeline, mock_components):
        """Test health check generates recommendation for low quality"""
        mock_components['metrics_collector'].generate_report.return_value = {
            'total_interactions': 100,
            'avg_quality_score': 0.5
        }

        health = pipeline.run_health_check()

        assert any("70%" in r for r in health['recommendations'])

    def test_train_calibration_models_insufficient_data(self, pipeline, mock_components):
        """Test training fails with insufficient data"""
        mock_components['metrics_collector'].generate_report.return_value = {
            'total_interactions': 10  # Less than 50
        }

        result = pipeline.train_calibration_models()

        assert result['status'] == 'insufficient_data'
        assert result['required'] == 50
        assert result['available'] == 10

    def test_train_calibration_models_no_data(self, pipeline, mock_components):
        """Test training fails with no data"""
        mock_components['metrics_collector'].generate_report.return_value = {
            'error': 'No data available'
        }

        result = pipeline.train_calibration_models()

        assert result['status'] == 'failed'

    def test_suggest_prompt_optimizations(self, pipeline, mock_components):
        """Test prompt optimization suggestions"""
        mock_prediction = MagicMock()
        mock_prediction.confidence = 0.8
        mock_prediction.recommended_adjustments = ["Add examples"]
        mock_prediction.prompt_characteristics = {"type": "debug"}

        mock_components['calibration_engine'].predict_optimal_config.return_value = mock_prediction
        mock_components['calibration_engine'].suggest_context_improvements.return_value = ["Improve context"]

        context = {
            'context_elements': ['debugging'],
            'target_outcome': 'improve quality'
        }

        result = pipeline.suggest_prompt_optimizations(context)

        assert result['status'] == 'success'
        assert result['predicted_success_rate'] == 0.8
        assert "Add examples" in result['recommendations']

    def test_suggest_prompt_optimizations_fallback(self, pipeline, mock_components):
        """Test fallback recommendations when prediction fails"""
        mock_components['calibration_engine'].predict_optimal_config.side_effect = Exception("Model not trained")

        context = {'context_elements': ['debugging']}
        result = pipeline.suggest_prompt_optimizations(context)

        assert result['status'] == 'prediction_failed'
        assert len(result['fallback_recommendations']) > 0

    def test_generate_performance_report(self, pipeline, mock_components):
        """Test performance report generation"""
        mock_components['dashboard'].generate_comprehensive_report.return_value = {
            'total_interactions': 50,
            'avg_quality_score': 0.85
        }

        result = pipeline.generate_performance_report(days=30)

        assert result['status'] == 'success'
        assert 'report' in result
        assert 'insights' in result
        assert 'generated_at' in result

    def test_generate_performance_report_error(self, pipeline, mock_components):
        """Test performance report with error"""
        mock_components['dashboard'].generate_comprehensive_report.return_value = {
            'error': 'No data available'
        }

        result = pipeline.generate_performance_report(days=30)

        assert result['status'] == 'report_failed'

    def test_generate_insights_excellent_quality(self, pipeline):
        """Test insight generation for excellent quality"""
        report = {'avg_quality_score': 0.95}

        insights = pipeline._generate_insights(report)

        assert any("excellent" in i.lower() or "optimal" in i.lower() for i in insights)

    def test_generate_insights_poor_quality(self, pipeline):
        """Test insight generation for poor quality"""
        report = {'avg_quality_score': 0.5}

        insights = pipeline._generate_insights(report)

        assert any("improvement" in i.lower() or "below" in i.lower() for i in insights)

    def test_generate_insights_slow_response(self, pipeline):
        """Test insight generation for slow response times"""
        report = {'avg_quality_score': 0.8, 'avg_response_time': 3000}

        insights = pipeline._generate_insights(report)

        assert any("response" in i.lower() or "2s" in i for i in insights)

    def test_generate_insights_with_trends(self, pipeline):
        """Test insight generation with trend data"""
        report = {
            'avg_quality_score': 0.8,
            'trend_analysis': {
                'quality_trend': {
                    'direction': 'declining'
                }
            }
        }

        insights = pipeline._generate_insights(report)

        assert any("declining" in i.lower() for i in insights)


class TestIntegrationPipelineEdgeCases:
    """Edge case tests for integration pipeline"""

    @pytest.fixture
    def mock_components(self):
        with patch('integration_pipeline.MetricsCollector') as mock_mc, \
             patch('integration_pipeline.ExperimentRunner') as mock_er, \
             patch('integration_pipeline.AutoCalibrationEngine') as mock_ace, \
             patch('integration_pipeline.PerformanceDashboard') as mock_pd, \
             patch('integration_pipeline.VersionManager') as mock_vm:
            yield {
                'metrics_collector': mock_mc.return_value,
                'experiment_runner': mock_er.return_value,
                'calibration_engine': mock_ace.return_value,
                'dashboard': mock_pd.return_value,
                'version_manager': mock_vm.return_value
            }

    def test_quality_score_boundary_high(self, mock_components):
        """Test quality score at 0.8 boundary"""
        pipeline = IntegrationPipeline()
        indicators = pipeline._determine_success_indicators(0.8)

        assert "user_satisfied" in indicators

    def test_quality_score_boundary_medium(self, mock_components):
        """Test quality score at 0.6 boundary"""
        pipeline = IntegrationPipeline()
        indicators = pipeline._determine_success_indicators(0.6)

        assert "minor_followup_needed" in indicators

    def test_run_experiment_success(self, mock_components):
        """Test running an experiment"""
        pipeline = IntegrationPipeline()

        mock_components['experiment_runner'].run_experiment.return_value = {
            'winner': 'variant_a',
            'confidence_level': 0.95,
            'statistical_significance': True
        }
        mock_components['experiment_runner'].generate_experiment_report.return_value = "Report"

        experiment_config = {
            "id": "test-exp",
            "name": "Test Experiment",
            "hypothesis": "Test hypothesis",
            "variants": [
                {
                    "id": "control",
                    "name": "Control",
                    "prompt_template": "Standard",
                    "context_modifiers": [],
                    "expected_outcome": "Baseline",
                    "success_criteria": ["quality > 0.7"]
                }
            ],
            "control_variant": "control",
            "metrics_to_track": ["quality_score"],
            "sample_size": 50
        }

        result = pipeline.run_experiment(experiment_config)

        assert result['status'] == 'success'
        assert result['winner'] == 'variant_a'


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
