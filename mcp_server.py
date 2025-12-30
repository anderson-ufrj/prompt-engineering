#!/usr/bin/env python3
"""
MCP Server for Prompt Engineering Lab
Exposes prompt engineering tools via Model Context Protocol

Author: Anderson Henrique da Silva
Location: Minas Gerais, Brazil

Usage:
    Local:  python mcp_server.py
    Remote: MCP_MODE=remote python mcp_server.py
"""

import os
import sys
import json
import logging
from pathlib import Path
from typing import Optional
from datetime import datetime

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from mcp.server.fastmcp import FastMCP

# Configure logging (critical for stdio servers)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('mcp_server.log'), logging.StreamHandler(sys.stderr)]
)
logger = logging.getLogger("prompt-engineering-mcp")

# Initialize FastMCP server
mcp = FastMCP("prompt-engineering-lab")

# =============================================================================
# LAZY IMPORTS - Only load heavy modules when needed
# =============================================================================

_pipeline = None
_metrics_collector = None
_experiment_runner = None
_calibration_engine = None
_dashboard = None


def get_pipeline():
    """Lazy load integration pipeline"""
    global _pipeline
    if _pipeline is None:
        from src.pipeline.integration_pipeline import IntegrationPipeline
        _pipeline = IntegrationPipeline()
    return _pipeline


def get_metrics_collector():
    """Lazy load metrics collector"""
    global _metrics_collector
    if _metrics_collector is None:
        from src.metrics.interaction_analyzer import MetricsCollector
        _metrics_collector = MetricsCollector()
    return _metrics_collector


def get_experiment_runner():
    """Lazy load experiment runner"""
    global _experiment_runner
    if _experiment_runner is None:
        from src.experiments.experiment_runner import ExperimentRunner
        _experiment_runner = ExperimentRunner()
    return _experiment_runner


def get_calibration_engine():
    """Lazy load calibration engine"""
    global _calibration_engine
    if _calibration_engine is None:
        from src.calibration.auto_calibration import AutoCalibrationEngine
        _calibration_engine = AutoCalibrationEngine()
    return _calibration_engine


def get_dashboard():
    """Lazy load dashboard"""
    global _dashboard
    if _dashboard is None:
        from src.calibration.dashboard import PerformanceDashboard
        _dashboard = PerformanceDashboard()
    return _dashboard


# =============================================================================
# TOOLS: SYSTEM HEALTH & STATUS
# =============================================================================

@mcp.tool()
def health_check() -> str:
    """
    Run system health check on the prompt engineering lab.

    Returns status of all components: metrics, experiments, calibration, data freshness.
    Use this to verify the system is operational before running other commands.
    """
    logger.info("Running health check")
    try:
        pipeline = get_pipeline()
        result = pipeline.run_health_check()
        return json.dumps(result, indent=2, ensure_ascii=False)
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return json.dumps({"status": "error", "message": str(e)})


# =============================================================================
# TOOLS: METRICS COLLECTION
# =============================================================================

@mcp.tool()
def collect_interaction(
    prompt_tokens: int,
    response_tokens: int,
    response_time_ms: int,
    quality_score: float,
    iteration_count: int,
    context_used: list[str],
    pattern_applied: Optional[str] = None
) -> str:
    """
    Collect metrics from an AI interaction for analysis and calibration.

    Args:
        prompt_tokens: Number of tokens in the prompt
        response_tokens: Number of tokens in the response
        response_time_ms: Response time in milliseconds
        quality_score: Quality score from 0.0 to 1.0
        iteration_count: Number of iterations needed
        context_used: List of context elements used (e.g., ["anderson-skill", "debugging"])
        pattern_applied: Optional pattern name (e.g., "chain", "parallel")

    Returns:
        Interaction ID for reference
    """
    logger.info(f"Collecting interaction: quality={quality_score}, pattern={pattern_applied}")
    try:
        pipeline = get_pipeline()
        interaction_id = pipeline.collect_interaction(
            prompt_tokens=prompt_tokens,
            response_tokens=response_tokens,
            response_time_ms=response_time_ms,
            quality_score=quality_score,
            iteration_count=iteration_count,
            context_used=context_used,
            pattern_applied=pattern_applied
        )
        return json.dumps({
            "status": "success",
            "interaction_id": interaction_id,
            "message": f"Interaction collected successfully"
        })
    except Exception as e:
        logger.error(f"Failed to collect interaction: {e}")
        return json.dumps({"status": "error", "message": str(e)})


@mcp.tool()
def get_metrics_report(days: int = 7) -> str:
    """
    Generate a metrics report for the specified period.

    Args:
        days: Number of days to include in the report (default: 7)

    Returns:
        Comprehensive metrics report with quality scores, patterns, and recommendations
    """
    logger.info(f"Generating metrics report for {days} days")
    try:
        collector = get_metrics_collector()
        report = collector.generate_report(days=days)
        return json.dumps(report, indent=2, ensure_ascii=False)
    except Exception as e:
        logger.error(f"Failed to generate report: {e}")
        return json.dumps({"status": "error", "message": str(e)})


# =============================================================================
# TOOLS: PERFORMANCE DASHBOARD
# =============================================================================

@mcp.tool()
def get_performance_report(days: int = 30) -> str:
    """
    Generate comprehensive performance report with trends and visualizations.

    Args:
        days: Number of days to analyze (default: 30)

    Returns:
        Detailed performance report with trends, patterns, and actionable recommendations
    """
    logger.info(f"Generating performance report for {days} days")
    try:
        pipeline = get_pipeline()
        result = pipeline.generate_performance_report(days)
        return json.dumps(result, indent=2, ensure_ascii=False, default=str)
    except Exception as e:
        logger.error(f"Failed to generate performance report: {e}")
        return json.dumps({"status": "error", "message": str(e)})


# =============================================================================
# TOOLS: A/B EXPERIMENTS
# =============================================================================

@mcp.tool()
def create_experiment(
    experiment_id: str,
    name: str,
    hypothesis: str,
    variant_a_name: str,
    variant_a_template: str,
    variant_b_name: str,
    variant_b_template: str,
    sample_size: int = 100
) -> str:
    """
    Create a new A/B experiment to test prompt variations.

    Args:
        experiment_id: Unique identifier for the experiment
        name: Human-readable experiment name
        hypothesis: What you expect to happen (e.g., "Adding examples improves quality by 15%")
        variant_a_name: Name for control variant
        variant_a_template: Prompt template for variant A
        variant_b_name: Name for test variant
        variant_b_template: Prompt template for variant B
        sample_size: Number of interactions per variant (default: 100)

    Returns:
        Experiment creation confirmation
    """
    logger.info(f"Creating experiment: {experiment_id}")
    try:
        from src.experiments.experiment_runner import Experiment, ExperimentVariant

        runner = get_experiment_runner()

        experiment = Experiment(
            id=experiment_id,
            name=name,
            hypothesis=hypothesis,
            variants=[
                ExperimentVariant(
                    id="variant_a",
                    name=variant_a_name,
                    prompt_template=variant_a_template,
                    context_modifiers=[],
                    expected_outcome="Control baseline",
                    success_criteria=["quality_score > 0.7"]
                ),
                ExperimentVariant(
                    id="variant_b",
                    name=variant_b_name,
                    prompt_template=variant_b_template,
                    context_modifiers=[],
                    expected_outcome="Test improvement",
                    success_criteria=["quality_score > 0.75"]
                )
            ],
            control_variant="variant_a",
            metrics_to_track=["quality_score", "response_time", "iteration_count"],
            sample_size=sample_size
        )

        exp_id = runner.create_experiment(experiment)
        return json.dumps({
            "status": "success",
            "experiment_id": exp_id,
            "message": f"Experiment '{name}' created successfully"
        })
    except Exception as e:
        logger.error(f"Failed to create experiment: {e}")
        return json.dumps({"status": "error", "message": str(e)})


@mcp.tool()
def run_experiment(experiment_id: str) -> str:
    """
    Run an existing A/B experiment and collect results.

    Args:
        experiment_id: ID of the experiment to run

    Returns:
        Experiment results with statistical analysis and winner recommendation
    """
    logger.info(f"Running experiment: {experiment_id}")
    try:
        runner = get_experiment_runner()
        results = runner.run_experiment(experiment_id)
        return json.dumps(results, indent=2, ensure_ascii=False)
    except Exception as e:
        logger.error(f"Failed to run experiment: {e}")
        return json.dumps({"status": "error", "message": str(e)})


@mcp.tool()
def get_experiment_report(experiment_id: str) -> str:
    """
    Generate a formatted report for a completed experiment.

    Args:
        experiment_id: ID of the experiment

    Returns:
        Markdown-formatted experiment report with results and conclusions
    """
    logger.info(f"Generating experiment report: {experiment_id}")
    try:
        runner = get_experiment_runner()
        report = runner.generate_experiment_report(experiment_id)
        return report
    except Exception as e:
        logger.error(f"Failed to generate experiment report: {e}")
        return f"Error: {str(e)}"


# =============================================================================
# TOOLS: AUTO-CALIBRATION
# =============================================================================

@mcp.tool()
def train_calibration_models(force_retrain: bool = False) -> str:
    """
    Train ML models for auto-calibration based on historical interaction data.

    Requires at least 50 interactions for training.

    Args:
        force_retrain: Force retraining even if models exist (default: False)

    Returns:
        Training results including model accuracy and clusters found
    """
    logger.info(f"Training calibration models (force={force_retrain})")
    try:
        pipeline = get_pipeline()
        result = pipeline.train_calibration_models(force_retrain=force_retrain)
        return json.dumps(result, indent=2, ensure_ascii=False)
    except Exception as e:
        logger.error(f"Failed to train models: {e}")
        return json.dumps({"status": "error", "message": str(e)})


@mcp.tool()
def suggest_optimizations(
    context_type: str,
    context_elements: list[str],
    target_outcome: str = "improve quality"
) -> str:
    """
    Get AI-powered suggestions for prompt optimization.

    Args:
        context_type: Type of context (e.g., "debugging", "brainstorming", "code_review")
        context_elements: List of context elements being used
        target_outcome: What you want to improve (default: "improve quality")

    Returns:
        Optimization suggestions with predicted success rate
    """
    logger.info(f"Getting optimization suggestions for {context_type}")
    try:
        pipeline = get_pipeline()
        context = {
            "type": context_type,
            "context_elements": context_elements,
            "target_outcome": target_outcome
        }
        result = pipeline.suggest_prompt_optimizations(context)
        return json.dumps(result, indent=2, ensure_ascii=False)
    except Exception as e:
        logger.error(f"Failed to get suggestions: {e}")
        return json.dumps({"status": "error", "message": str(e)})


@mcp.tool()
def auto_optimize(target_metric: str = "quality_score") -> str:
    """
    Automatically optimize prompts based on collected data.

    Analyzes historical data, trains models if needed, and suggests optimizations.

    Args:
        target_metric: Metric to optimize for (quality_score, response_time, iteration_count)

    Returns:
        Optimization results with actionable recommendations
    """
    logger.info(f"Running auto-optimization for {target_metric}")
    try:
        pipeline = get_pipeline()
        result = pipeline.auto_optimize(target_metric=target_metric)
        return json.dumps(result, indent=2, ensure_ascii=False, default=str)
    except Exception as e:
        logger.error(f"Failed to auto-optimize: {e}")
        return json.dumps({"status": "error", "message": str(e)})


# =============================================================================
# TOOLS: AGENTS (Brazilian Personas)
# =============================================================================

@mcp.tool()
def list_agents() -> str:
    """
    List all available Brazilian agents (personas) in the lab.

    Each agent has a specific role based on DSRM methodology.

    Returns:
        List of agents with their roles and when to use them
    """
    agents = {
        "santos-dumont": {
            "name": "Santos Dumont",
            "role": "Tech Lead / Architect",
            "focus": "System architecture, delegation, technical decisions",
            "when_to_use": "Starting new features, architecture decisions, coordinating work"
        },
        "machado-de-assis": {
            "name": "Machado de Assis",
            "role": "Documentarist",
            "focus": "Documentation, communication, papers",
            "when_to_use": "Writing docs, README, scientific papers"
        },
        "vital-brazil": {
            "name": "Vital Brazil",
            "role": "QA Engineer",
            "focus": "Testing, validation, quality assurance",
            "when_to_use": "Writing tests, code review, validation"
        },
        "aleijadinho": {
            "name": "Aleijadinho",
            "role": "Code Reviewer",
            "focus": "Refinement, refactoring, code quality",
            "when_to_use": "Code review, refactoring, optimization"
        },
        "coimbra": {
            "name": "Coimbra",
            "role": "DevOps",
            "focus": "Automation, CI/CD, deployment",
            "when_to_use": "Setting up pipelines, deployment, automation"
        },
        "nise-da-silveira": {
            "name": "Nise da Silveira",
            "role": "Neural Pattern Analyst",
            "focus": "Cognitive patterns, interaction analysis",
            "when_to_use": "Analyzing interaction patterns, calibration insights"
        }
    }
    return json.dumps(agents, indent=2, ensure_ascii=False)


@mcp.tool()
def get_agent_prompt(agent_id: str) -> str:
    """
    Get the activation prompt for a specific Brazilian agent.

    Args:
        agent_id: Agent identifier (e.g., "santos-dumont", "vital-brazil")

    Returns:
        Agent's base prompt and context for activation
    """
    logger.info(f"Getting agent prompt: {agent_id}")
    try:
        agent_file = Path("artifacts/agents") / f"{agent_id}.md"
        if not agent_file.exists():
            return json.dumps({
                "status": "error",
                "message": f"Agent '{agent_id}' not found. Use list_agents() to see available agents."
            })

        with open(agent_file, 'r') as f:
            content = f.read()

        return json.dumps({
            "status": "success",
            "agent_id": agent_id,
            "prompt": content
        })
    except Exception as e:
        logger.error(f"Failed to get agent prompt: {e}")
        return json.dumps({"status": "error", "message": str(e)})


# =============================================================================
# TOOLS: CONTEXT & PATTERNS
# =============================================================================

@mcp.tool()
def get_effective_patterns() -> str:
    """
    Get list of effective patterns from the evidence base.

    Returns:
        Patterns that have proven effective based on historical data
    """
    logger.info("Getting effective patterns")
    try:
        patterns_path = Path("evidence/patterns")
        patterns = []

        if patterns_path.exists():
            for file in patterns_path.glob("*.md"):
                patterns.append({
                    "name": file.stem,
                    "file": str(file)
                })

        if not patterns:
            patterns = [
                {"name": "chain", "description": "Sequential reasoning for complex problems"},
                {"name": "parallel", "description": "Multiple perspectives simultaneously"},
                {"name": "recursive", "description": "Breaking down into sub-problems"},
                {"name": "reflective", "description": "Self-correction and iteration"}
            ]

        return json.dumps({
            "status": "success",
            "patterns": patterns,
            "count": len(patterns)
        }, indent=2)
    except Exception as e:
        logger.error(f"Failed to get patterns: {e}")
        return json.dumps({"status": "error", "message": str(e)})


@mcp.tool()
def get_antipatterns() -> str:
    """
    Get list of antipatterns to avoid based on the evidence base.

    Returns:
        Patterns that have proven ineffective and should be avoided
    """
    logger.info("Getting antipatterns")
    try:
        antipatterns_path = Path("evidence/antipatterns")
        antipatterns = []

        if antipatterns_path.exists():
            for file in antipatterns_path.glob("*.md"):
                antipatterns.append({
                    "name": file.stem,
                    "file": str(file)
                })

        if not antipatterns:
            antipatterns = [
                {"name": "vague_context", "description": "Prompts without specific context"},
                {"name": "no_examples", "description": "Missing concrete examples"},
                {"name": "overloaded_prompt", "description": "Too many instructions at once"},
                {"name": "no_success_criteria", "description": "Missing definition of done"}
            ]

        return json.dumps({
            "status": "success",
            "antipatterns": antipatterns,
            "count": len(antipatterns)
        }, indent=2)
    except Exception as e:
        logger.error(f"Failed to get antipatterns: {e}")
        return json.dumps({"status": "error", "message": str(e)})


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

def main():
    """Start the MCP server"""
    mode = os.getenv("MCP_MODE", "local")
    port = int(os.getenv("MCP_PORT", "8000"))

    logger.info(f"Starting Prompt Engineering Lab MCP Server")
    logger.info(f"Mode: {mode}, Port: {port}")

    if mode == "remote":
        # Railway/Cloud - SSE transport
        logger.info("Running in REMOTE mode (SSE)")
        mcp.run(transport="sse", host="0.0.0.0", port=port)
    else:
        # Local - stdio transport
        logger.info("Running in LOCAL mode (stdio)")
        mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
