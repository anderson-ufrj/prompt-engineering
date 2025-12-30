#!/usr/bin/env python3
"""
Tests for Performance Dashboard
Author: Anderson Henrique da Silva
Location: Minas Gerais, Brazil
"""

import pytest
import json
import tempfile
from pathlib import Path
from datetime import datetime, timedelta
from unittest.mock import patch, MagicMock
import sys

sys.path.append(str(Path(__file__).parent.parent))

from src.calibration.dashboard import PerformanceDashboard


class TestPerformanceDashboard:
    """Test cases for PerformanceDashboard class"""

    @pytest.fixture
    def temp_data_path(self):
        """Create temporary directory for test data"""
        with tempfile.TemporaryDirectory() as tmpdir:
            data_path = Path(tmpdir) / "data"
            data_path.mkdir()
            yield data_path

    @pytest.fixture
    def dashboard(self, temp_data_path):
        """Create dashboard with temp paths"""
        with patch('src.calibration.dashboard.plt'), patch('src.calibration.dashboard.sns'):
            dash = PerformanceDashboard(data_path=temp_data_path)
            dash.reports_path = temp_data_path.parent / "reports"
            dash.reports_path.mkdir(exist_ok=True)
            return dash

    @pytest.fixture
    def sample_interactions(self):
        """Sample interaction data for testing"""
        base_time = datetime.now()
        return [
            {
                "timestamp": (base_time - timedelta(days=1)).isoformat(),
                "prompt_tokens": 150,
                "response_tokens": 300,
                "response_time_ms": 1200,
                "quality_score": 0.85,
                "iteration_count": 1,
                "context_used": ["anderson-skill", "debugging"],
                "pattern_applied": "chain"
            },
            {
                "timestamp": (base_time - timedelta(days=2)).isoformat(),
                "prompt_tokens": 200,
                "response_tokens": 400,
                "response_time_ms": 1800,
                "quality_score": 0.92,
                "iteration_count": 2,
                "context_used": ["anderson-skill", "brainstorming"],
                "pattern_applied": "parallel"
            },
            {
                "timestamp": (base_time - timedelta(days=3)).isoformat(),
                "prompt_tokens": 100,
                "response_tokens": 250,
                "response_time_ms": 900,
                "quality_score": 0.78,
                "iteration_count": 1,
                "context_used": ["anderson-skill"],
                "pattern_applied": "chain"
            }
        ]

    def _save_interactions(self, data_path: Path, interactions: list):
        """Helper to save interactions to temp directory"""
        for i, interaction in enumerate(interactions):
            file_path = data_path / f"interaction_{i}.json"
            with open(file_path, 'w') as f:
                json.dump(interaction, f)

    def test_dashboard_initialization(self, temp_data_path):
        """Test dashboard initializes correctly"""
        with patch('src.calibration.dashboard.plt'), patch('src.calibration.dashboard.sns'):
            dashboard = PerformanceDashboard(data_path=temp_data_path)
            assert dashboard.data_path == temp_data_path
            assert dashboard.reports_path.exists()

    def test_load_interaction_data_empty(self, dashboard):
        """Test loading data when no interactions exist"""
        df = dashboard.load_interaction_data(days=7)
        assert df.empty

    def test_load_interaction_data_with_data(self, dashboard, sample_interactions):
        """Test loading interaction data"""
        self._save_interactions(dashboard.data_path, sample_interactions)

        df = dashboard.load_interaction_data(days=7)

        assert len(df) == 3
        assert 'quality_score' in df.columns
        assert 'response_time_ms' in df.columns

    def test_load_interaction_data_filters_old(self, dashboard, sample_interactions):
        """Test that old data is filtered out"""
        # Add an old interaction
        old_interaction = sample_interactions[0].copy()
        old_interaction["timestamp"] = (datetime.now() - timedelta(days=15)).isoformat()

        all_interactions = sample_interactions + [old_interaction]
        self._save_interactions(dashboard.data_path, all_interactions)

        df = dashboard.load_interaction_data(days=7)

        # Should only have 3, not 4
        assert len(df) == 3

    def test_generate_report_no_data(self, dashboard):
        """Test report generation with no data"""
        report = dashboard.generate_comprehensive_report(days=7)

        assert "error" in report
        assert "No data available" in report["error"]

    @patch('src.calibration.dashboard.PerformanceDashboard._create_visualizations')
    @patch('src.calibration.dashboard.PerformanceDashboard._save_report')
    def test_generate_report_with_data(self, mock_save, mock_viz, dashboard, sample_interactions):
        """Test comprehensive report generation"""
        self._save_interactions(dashboard.data_path, sample_interactions)

        report = dashboard.generate_comprehensive_report(days=7)

        assert "error" not in report
        assert report["total_interactions"] == 3
        assert "avg_quality_score" in report
        assert "avg_response_time" in report
        assert "recommendations" in report

        # Verify average calculations
        expected_avg_quality = (0.85 + 0.92 + 0.78) / 3
        assert abs(report["avg_quality_score"] - expected_avg_quality) < 0.01

    def test_analyze_patterns(self, dashboard, sample_interactions):
        """Test pattern analysis"""
        self._save_interactions(dashboard.data_path, sample_interactions)
        df = dashboard.load_interaction_data(days=7)

        patterns = dashboard._analyze_patterns(df)

        assert "most_used" in patterns
        assert patterns["most_used"] == "chain"  # appears twice
        assert "pattern_distribution" in patterns
        assert patterns["pattern_distribution"]["chain"] == 2
        assert patterns["pattern_distribution"]["parallel"] == 1

    def test_analyze_context_performance(self, dashboard, sample_interactions):
        """Test context performance analysis"""
        self._save_interactions(dashboard.data_path, sample_interactions)
        df = dashboard.load_interaction_data(days=7)

        context_perf = dashboard._analyze_context_performance(df)

        assert "anderson-skill" in context_perf
        # anderson-skill appears in all 3 interactions

    def test_generate_recommendations_low_quality(self, dashboard):
        """Test recommendations for low quality scores"""
        import pandas as pd

        df = pd.DataFrame([
            {"quality_score": 0.5, "iteration_count": 1, "response_time_ms": 1000},
            {"quality_score": 0.6, "iteration_count": 1, "response_time_ms": 1000},
        ])

        with patch.object(dashboard, '_calculate_trends', return_value={"insufficient_data": True}):
            recommendations = dashboard._generate_recommendations(df)

        assert any("below 70%" in r for r in recommendations)

    def test_generate_recommendations_high_iterations(self, dashboard):
        """Test recommendations for high iteration counts"""
        import pandas as pd

        df = pd.DataFrame([
            {"quality_score": 0.8, "iteration_count": 3, "response_time_ms": 1000},
            {"quality_score": 0.8, "iteration_count": 4, "response_time_ms": 1000},
        ])

        with patch.object(dashboard, '_calculate_trends', return_value={"insufficient_data": True}):
            recommendations = dashboard._generate_recommendations(df)

        assert any("iteration count" in r.lower() for r in recommendations)

    def test_generate_recommendations_slow_response(self, dashboard):
        """Test recommendations for slow response times"""
        import pandas as pd

        df = pd.DataFrame([
            {"quality_score": 0.8, "iteration_count": 1, "response_time_ms": 3000},
            {"quality_score": 0.8, "iteration_count": 1, "response_time_ms": 2500},
        ])

        with patch.object(dashboard, '_calculate_trends', return_value={"insufficient_data": True}):
            recommendations = dashboard._generate_recommendations(df)

        assert any("2s" in r or "response time" in r.lower() for r in recommendations)

    def test_generate_recommendations_excellent_quality(self, dashboard):
        """Test recommendations for excellent quality"""
        import pandas as pd

        df = pd.DataFrame([
            {"quality_score": 0.95, "iteration_count": 1, "response_time_ms": 1000},
            {"quality_score": 0.92, "iteration_count": 1, "response_time_ms": 1000},
        ])

        with patch.object(dashboard, '_calculate_trends', return_value={"insufficient_data": True}):
            recommendations = dashboard._generate_recommendations(df)

        assert any("excellent" in r.lower() for r in recommendations)

    def test_calculate_trends_insufficient_data(self, dashboard):
        """Test trend calculation with insufficient data"""
        import pandas as pd

        df = pd.DataFrame([
            {"timestamp": datetime.now().isoformat(), "quality_score": 0.8,
             "response_time_ms": 1000, "iteration_count": 1}
        ])

        trends = dashboard._calculate_trends(df, 7)

        assert trends.get("insufficient_data") == True

    def test_calculate_trends_with_data(self, dashboard, sample_interactions):
        """Test trend calculation with sufficient data"""
        # Create interactions on different days
        interactions = []
        for i in range(5):
            interaction = sample_interactions[0].copy()
            interaction["timestamp"] = (datetime.now() - timedelta(days=i)).isoformat()
            interaction["quality_score"] = 0.7 + (i * 0.05)  # Increasing quality
            interactions.append(interaction)

        self._save_interactions(dashboard.data_path, interactions)
        df = dashboard.load_interaction_data(days=7)

        trends = dashboard._calculate_trends(df, 7)

        assert "quality_trend" in trends
        assert "direction" in trends["quality_trend"]

    def test_format_markdown_report(self, dashboard):
        """Test markdown report formatting"""
        metrics = {
            "period": "Last 7 days",
            "total_interactions": 10,
            "avg_quality_score": 0.85,
            "avg_response_time": 1500,
            "avg_iterations": 1.5,
            "success_rate": 0.8,
            "trend_analysis": {
                "quality_trend": {
                    "direction": "improving",
                    "slope": 0.01,
                    "r_squared": 0.85
                }
            },
            "pattern_analysis": {
                "most_used": "chain",
                "best_performing": "parallel"
            },
            "context_performance": {
                "debugging": 0.85,
                "brainstorming": 0.90
            },
            "recommendations": [
                "Test recommendation 1",
                "Test recommendation 2"
            ]
        }

        report = dashboard._format_markdown_report(metrics)

        assert "# Performance Report" in report
        assert "Total Interactions:** 10" in report
        assert "0.85" in report
        assert "improving" in report
        assert "chain" in report
        assert "debugging" in report
        assert "Test recommendation 1" in report

    @patch('src.calibration.dashboard.plt')
    def test_create_visualizations(self, mock_plt, dashboard, sample_interactions):
        """Test visualization creation doesn't crash"""
        self._save_interactions(dashboard.data_path, sample_interactions)
        df = dashboard.load_interaction_data(days=7)

        # Setup mock for subplots - use MagicMock with __getitem__ support
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_axes = MagicMock()
        mock_axes.__getitem__ = MagicMock(return_value=mock_ax)
        mock_plt.subplots.return_value = (mock_fig, mock_axes)

        # Should not raise
        dashboard._create_visualizations(df, 7)

        # Verify plt was called
        assert mock_plt.subplots.called

    def test_save_report(self, dashboard):
        """Test report saving"""
        metrics = {
            "period": "Last 7 days",
            "total_interactions": 5,
            "avg_quality_score": 0.85,
            "avg_response_time": 1200,
            "avg_iterations": 1.2,
            "success_rate": 0.8,
            "trend_analysis": {"insufficient_data": True},
            "pattern_analysis": {},
            "context_performance": {},
            "recommendations": ["Test recommendation"]
        }

        dashboard._save_report(metrics, 7)

        # Check JSON file exists
        json_files = list(dashboard.reports_path.glob("*.json"))
        assert len(json_files) >= 1

        # Check MD file exists
        md_files = list(dashboard.reports_path.glob("*.md"))
        assert len(md_files) >= 1


class TestDashboardEdgeCases:
    """Edge case tests for dashboard"""

    @pytest.fixture
    def temp_data_path(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            data_path = Path(tmpdir) / "data"
            data_path.mkdir()
            yield data_path

    def test_invalid_json_files_ignored(self, temp_data_path):
        """Test that invalid JSON files are ignored"""
        # Create invalid JSON file
        invalid_file = temp_data_path / "invalid.json"
        with open(invalid_file, 'w') as f:
            f.write("not valid json {{{")

        # Create valid file
        valid_file = temp_data_path / "valid.json"
        with open(valid_file, 'w') as f:
            json.dump({
                "timestamp": datetime.now().isoformat(),
                "quality_score": 0.8,
                "response_time_ms": 1000,
                "iteration_count": 1
            }, f)

        with patch('src.calibration.dashboard.plt'), patch('src.calibration.dashboard.sns'):
            dashboard = PerformanceDashboard(data_path=temp_data_path)
            df = dashboard.load_interaction_data(days=7)

        # Should only have 1 valid interaction
        assert len(df) == 1

    def test_missing_timestamp_ignored(self, temp_data_path):
        """Test that files without timestamp are ignored"""
        invalid_file = temp_data_path / "no_timestamp.json"
        with open(invalid_file, 'w') as f:
            json.dump({"quality_score": 0.8}, f)

        with patch('src.calibration.dashboard.plt'), patch('src.calibration.dashboard.sns'):
            dashboard = PerformanceDashboard(data_path=temp_data_path)
            df = dashboard.load_interaction_data(days=7)

        assert df.empty


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
