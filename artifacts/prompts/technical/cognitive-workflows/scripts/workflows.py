#!/usr/bin/env python3
"""
Cognitive Workflow Patterns

Implementations of Anthropic's multi-LLM patterns for complex reasoning.
Based on "Building Effective Agents" research.

Usage:
    from workflows import chain, parallel, route, orchestrate, evaluate
"""

from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from typing import Callable, Any
import re


# =============================================================================
# Pattern 1: Chain
# =============================================================================

def chain(input_data: str, steps: list[Callable[[str], str]]) -> str:
    """
    Sequential processing where each step builds on previous output.

    Args:
        input_data: Initial input to process
        steps: List of functions, each taking string and returning string

    Returns:
        Final processed result

    Example:
        result = chain(
            "raw data",
            [clean, analyze, format]
        )
    """
    result = input_data
    for i, step in enumerate(steps, 1):
        print(f"Step {i}/{len(steps)}: {step.__name__}")
        result = step(result)
    return result


# =============================================================================
# Pattern 2: Parallel
# =============================================================================

@dataclass
class PerspectiveResult:
    """Result from a single perspective analysis."""
    name: str
    analysis: str
    score: float | None = None


def parallel(
    input_data: str,
    perspectives: dict[str, Callable[[str], str]],
    max_workers: int = 4
) -> list[PerspectiveResult]:
    """
    Analyze input from multiple perspectives simultaneously.

    Args:
        input_data: Data to analyze
        perspectives: Dict of {name: analyzer_function}
        max_workers: Max concurrent analyses

    Returns:
        List of PerspectiveResult objects

    Example:
        results = parallel(
            "job offer details",
            {
                "financial": analyze_financial,
                "technical": analyze_technical,
                "career": analyze_career
            }
        )
    """
    results = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(func, input_data): name
            for name, func in perspectives.items()
        }

        for future in futures:
            name = futures[future]
            try:
                analysis = future.result()
                results.append(PerspectiveResult(name=name, analysis=analysis))
            except Exception as e:
                results.append(
                    PerspectiveResult(name=name, analysis=f"Error: {e}")
                )

    return results


def synthesize_parallel(
    results: list[PerspectiveResult],
    weights: dict[str, float] | None = None
) -> str:
    """
    Synthesize parallel analysis results.

    Args:
        results: List of perspective results
        weights: Optional weights per perspective (must sum to 1.0)

    Returns:
        Synthesized summary
    """
    if weights is None:
        weights = {r.name: 1.0 / len(results) for r in results}

    lines = ["## Synthesis\n"]

    for result in results:
        weight = weights.get(result.name, 0)
        lines.append(f"### {result.name.title()} ({weight:.0%})")
        lines.append(result.analysis)
        lines.append("")

    return "\n".join(lines)


# =============================================================================
# Pattern 3: Route
# =============================================================================

@dataclass
class Route:
    """Definition of a route."""
    category: str
    handler: Callable[[str], str]
    description: str = ""


def route(
    input_data: str,
    classifier: Callable[[str], str],
    routes: list[Route]
) -> str:
    """
    Classify input and route to appropriate handler.

    Args:
        input_data: Data to classify and process
        classifier: Function that returns category name
        routes: List of Route objects

    Returns:
        Handler result for matched route

    Example:
        result = route(
            task_description,
            classify_task,
            [
                Route("debug", handle_debug),
                Route("feature", handle_feature),
                Route("docs", handle_docs)
            ]
        )
    """
    category = classifier(input_data).strip().lower()

    route_map = {r.category.lower(): r for r in routes}

    if category not in route_map:
        available = list(route_map.keys())
        raise ValueError(f"Unknown category '{category}'. Available: {available}")

    selected = route_map[category]
    print(f"Routed to: {selected.category}")

    return selected.handler(input_data)


# =============================================================================
# Pattern 4: Orchestrator-Workers
# =============================================================================

@dataclass
class Subtask:
    """A subtask generated by the orchestrator."""
    task_type: str
    description: str
    context: dict[str, Any] | None = None


@dataclass
class WorkerResult:
    """Result from a worker."""
    task_type: str
    result: str


def orchestrate(
    task: str,
    analyzer: Callable[[str], list[Subtask]],
    worker: Callable[[str, Subtask], str],
    synthesizer: Callable[[str, list[WorkerResult]], str]
) -> str:
    """
    Orchestrator-Workers pattern for dynamic task decomposition.

    Args:
        task: Complex task description
        analyzer: Function that breaks task into subtasks
        worker: Function that handles each subtask
        synthesizer: Function that combines worker results

    Returns:
        Final synthesized result

    Example:
        result = orchestrate(
            "Review this PR",
            analyze_pr,
            review_aspect,
            combine_reviews
        )
    """
    # Phase 1: Analyze and decompose
    print("Orchestrator: Analyzing task...")
    subtasks = analyzer(task)
    print(f"Orchestrator: Identified {len(subtasks)} subtasks")

    # Phase 2: Execute workers
    worker_results = []
    for i, subtask in enumerate(subtasks, 1):
        print(f"Worker {i}/{len(subtasks)}: {subtask.task_type}")
        result = worker(task, subtask)
        worker_results.append(
            WorkerResult(task_type=subtask.task_type, result=result)
        )

    # Phase 3: Synthesize
    print("Orchestrator: Synthesizing results...")
    return synthesizer(task, worker_results)


# =============================================================================
# Pattern 5: Evaluator-Optimizer
# =============================================================================

@dataclass
class Evaluation:
    """Result of evaluating generated content."""
    passed: bool
    scores: dict[str, float]
    feedback: list[str]


def evaluate_optimize(
    task: str,
    generator: Callable[[str, str | None], str],
    evaluator: Callable[[str, str], Evaluation],
    max_iterations: int = 3,
    threshold: float = 4.0
) -> tuple[str, list[Evaluation]]:
    """
    Iterative refinement with evaluation feedback.

    Args:
        task: Task description
        generator: Function that generates/improves output
        evaluator: Function that evaluates output
        max_iterations: Maximum refinement cycles
        threshold: Minimum score to pass

    Returns:
        Tuple of (final_output, evaluation_history)

    Example:
        result, history = evaluate_optimize(
            "Write API docs",
            generate_docs,
            evaluate_docs,
            max_iterations=3
        )
    """
    history = []
    current_output = None
    feedback_text = None

    for iteration in range(1, max_iterations + 1):
        print(f"\n--- Iteration {iteration}/{max_iterations} ---")

        # Generate/improve
        current_output = generator(task, feedback_text)

        # Evaluate
        evaluation = evaluator(task, current_output)
        history.append(evaluation)

        print(f"Scores: {evaluation.scores}")
        print(f"Passed: {evaluation.passed}")

        if evaluation.passed:
            print("✓ Evaluation passed!")
            break

        # Prepare feedback for next iteration
        feedback_text = "\n".join(evaluation.feedback)
        print(f"Feedback: {feedback_text}")

    return current_output, history


# =============================================================================
# Utility: XML Parser
# =============================================================================

def extract_xml(text: str, tag: str) -> str:
    """
    Extract content from XML-style tags.

    Args:
        text: Text containing XML tags
        tag: Tag name to extract

    Returns:
        Content between tags or empty string
    """
    pattern = rf"<{tag}>(.*?)</{tag}>"
    match = re.search(pattern, text, re.DOTALL)
    return match.group(1).strip() if match else ""


def extract_all_xml(text: str, tag: str) -> list[str]:
    """Extract all occurrences of a tag."""
    pattern = rf"<{tag}>(.*?)</{tag}>"
    return [m.strip() for m in re.findall(pattern, text, re.DOTALL)]


# =============================================================================
# Example Usage
# =============================================================================

if __name__ == "__main__":
    # Example: Simple chain
    def uppercase(s: str) -> str:
        return s.upper()

    def add_prefix(s: str) -> str:
        return f"[PROCESSED] {s}"

    result = chain("hello world", [uppercase, add_prefix])
    print(f"Chain result: {result}")

    # Example: Parallel (mock)
    def mock_financial(s: str) -> str:
        return "Financial analysis: Positive ROI expected"

    def mock_technical(s: str) -> str:
        return "Technical analysis: Stack alignment is good"

    results = parallel("job offer", {
        "financial": mock_financial,
        "technical": mock_technical
    })

    for r in results:
        print(f"{r.name}: {r.analysis}")
