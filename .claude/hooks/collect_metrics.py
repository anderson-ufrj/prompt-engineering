#!/usr/bin/env python3
"""
Auto-collect metrics hook for Claude Code interactions
Author: Anderson Henrique da Silva

This hook captures rich interaction data after each tool use
and stores it for analysis in the prompt engineering lab.
"""

import json
import sys
import os
from datetime import datetime
from pathlib import Path
import hashlib
import re

# Configuration
METRICS_DIR = Path(__file__).parent.parent.parent / "evidence" / "metrics" / "data"
METRICS_DIR.mkdir(parents=True, exist_ok=True)

# Tool categories for pattern analysis
TOOL_CATEGORIES = {
    "exploration": ["Read", "Glob", "Grep", "LSP", "WebSearch", "WebFetch"],
    "modification": ["Write", "Edit", "MultiEdit", "NotebookEdit"],
    "execution": ["Bash", "Task"],
    "planning": ["TodoWrite", "EnterPlanMode", "ExitPlanMode"],
    "interaction": ["AskUserQuestion", "Skill"],
}


def estimate_tokens(text: str) -> int:
    """Rough token estimation (1 token ≈ 4 chars for English)"""
    if not text:
        return 0
    return len(str(text)) // 4


def detect_success(tool_name: str, tool_response: dict) -> bool:
    """Detect if tool execution was successful based on response"""
    if not isinstance(tool_response, dict):
        return True  # Assume success if no structured response

    # Explicit success field
    if "success" in tool_response:
        return bool(tool_response["success"])

    # Bash command - check return code
    if tool_name == "Bash":
        return tool_response.get("returnCode", 0) == 0

    # Check for error indicators
    error_keys = ["error", "Error", "exception", "Exception"]
    for key in error_keys:
        if key in tool_response:
            return False

    return True


def categorize_tool(tool_name: str) -> str:
    """Categorize tool by its function"""
    for category, tools in TOOL_CATEGORIES.items():
        if tool_name in tools:
            return category
    return "other"


def extract_context_hints(tool_input: dict, tool_name: str) -> list:
    """Extract context hints from tool input"""
    hints = []

    if not isinstance(tool_input, dict):
        return hints

    # File path hints
    file_path = tool_input.get("file_path") or tool_input.get("path", "")
    if file_path:
        # Extract file type
        ext = Path(file_path).suffix
        if ext:
            hints.append(f"file_type:{ext}")

        # Extract directory context
        parts = Path(file_path).parts
        if "tests" in parts or "test" in parts:
            hints.append("context:testing")
        elif "src" in parts:
            hints.append("context:source")
        elif "docs" in parts:
            hints.append("context:documentation")

    # Pattern hints for Grep
    if tool_name == "Grep" and "pattern" in tool_input:
        hints.append("action:search")

    # Command hints for Bash
    if tool_name == "Bash" and "command" in tool_input:
        cmd = tool_input["command"]
        if cmd.startswith("git"):
            hints.append("action:git")
        elif "pytest" in cmd or "test" in cmd:
            hints.append("action:testing")
        elif "pip" in cmd or "npm" in cmd:
            hints.append("action:dependencies")

    return hints


def detect_patterns(tool_name: str, tool_input: dict, session_metrics: dict) -> str:
    """Detect interaction patterns"""
    category = categorize_tool(tool_name)

    # Common patterns
    if category == "exploration":
        return "pattern:investigation"
    elif category == "modification":
        return "pattern:implementation"
    elif category == "execution":
        if "test" in str(tool_input).lower():
            return "pattern:validation"
        return "pattern:execution"
    elif category == "planning":
        return "pattern:planning"

    return None


def collect_interaction(event_data: dict) -> None:
    """Collect rich metrics from a Claude Code PostToolUse interaction"""

    timestamp = datetime.now().isoformat()

    # Generate unique ID
    interaction_id = hashlib.md5(
        f"{timestamp}{os.getpid()}".encode()
    ).hexdigest()[:8]

    # Extract PostToolUse fields (correct field names from Claude Code)
    session_id = event_data.get("session_id")
    tool_name = event_data.get("tool_name")
    tool_use_id = event_data.get("tool_use_id")
    tool_input = event_data.get("tool_input", {})
    tool_response = event_data.get("tool_response", {})
    permission_mode = event_data.get("permission_mode", "unknown")
    cwd = event_data.get("cwd")
    transcript_path = event_data.get("transcript_path")

    # Derived metrics
    is_success = detect_success(tool_name, tool_response)
    tool_category = categorize_tool(tool_name)
    context_hints = extract_context_hints(tool_input, tool_name)
    pattern = detect_patterns(tool_name, tool_input, {})

    # Token estimation
    input_tokens = estimate_tokens(json.dumps(tool_input))
    output_tokens = estimate_tokens(json.dumps(tool_response))

    # Build enriched metrics object
    metrics = {
        "id": interaction_id,
        "timestamp": timestamp,
        "session_id": session_id,
        "tool_use_id": tool_use_id,

        # Tool information
        "tool_name": tool_name,
        "tool_category": tool_category,
        "permission_mode": permission_mode,

        # Context
        "cwd": cwd,
        "project": os.path.basename(cwd) if cwd else None,

        # Input/Output analysis (without sensitive content)
        "input_keys": list(tool_input.keys()) if isinstance(tool_input, dict) else None,
        "input_tokens_est": input_tokens,
        "output_tokens_est": output_tokens,
        "total_tokens_est": input_tokens + output_tokens,

        # Success indicators
        "success": is_success,
        "success_indicators": ["return_code_zero" if is_success else "error_detected"],

        # Pattern analysis
        "context_hints": context_hints,
        "pattern_applied": pattern,

        # Quality score heuristic (0-100)
        # Based on: success (50pts) + reasonable token usage (25pts) + context richness (25pts)
        "quality_score": (
            (50 if is_success else 0) +
            (25 if 10 < input_tokens < 5000 else 10) +
            (min(len(context_hints) * 5, 25))
        ),

        # Iteration tracking (will be enriched by session analysis)
        "iteration_count": 1,

        # Metadata
        "transcript_path": transcript_path,
        "collector_version": "2.0.0"
    }

    # Save to file
    output_file = METRICS_DIR / f"{interaction_id}.json"
    with open(output_file, 'w') as f:
        json.dump(metrics, f, indent=2, ensure_ascii=False)

    # Log summary to stderr
    quality_indicator = "+" if metrics["quality_score"] >= 70 else "~" if metrics["quality_score"] >= 50 else "-"
    print(
        f"[metrics] {quality_indicator} {tool_name} ({tool_category}) "
        f"q={metrics['quality_score']} t={metrics['total_tokens_est']}",
        file=sys.stderr
    )


def main():
    """Main entry point for hook"""
    try:
        event_data = json.load(sys.stdin)

        # Verify this is a PostToolUse event
        if event_data.get("hook_event_name") == "PostToolUse":
            collect_interaction(event_data)

    except json.JSONDecodeError:
        # No valid JSON input - silent fail
        pass
    except Exception as e:
        print(f"[metrics] Error: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
