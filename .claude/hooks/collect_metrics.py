#!/usr/bin/env python3
"""
Auto-collect metrics hook for Claude Code interactions
Author: Anderson Henrique da Silva

This hook captures interaction data after each Claude response
and stores it for later analysis.
"""

import json
import sys
import os
from datetime import datetime
from pathlib import Path
import hashlib

# Configuration
METRICS_DIR = Path(__file__).parent.parent.parent / "evidence" / "metrics" / "data"
METRICS_DIR.mkdir(parents=True, exist_ok=True)


def collect_interaction(event_data: dict) -> None:
    """Collect metrics from a Claude Code interaction"""

    # Extract relevant data from event
    timestamp = datetime.now().isoformat()

    # Generate unique ID
    interaction_id = hashlib.md5(
        f"{timestamp}{os.getpid()}".encode()
    ).hexdigest()[:8]

    # Build metrics object
    metrics = {
        "id": interaction_id,
        "timestamp": timestamp,
        "event_type": event_data.get("type", "unknown"),
        "tool_name": event_data.get("tool", {}).get("name"),
        "session_id": event_data.get("session_id"),
        "project": os.getcwd(),
        # Placeholder - will be enriched by analysis
        "quality_score": None,
        "iteration_count": 1,
        "context_used": [],
        "pattern_applied": None,
        "success_indicators": []
    }

    # Save to file
    output_file = METRICS_DIR / f"{interaction_id}.json"
    with open(output_file, 'w') as f:
        json.dump(metrics, f, indent=2, ensure_ascii=False)

    # Log to stderr (visible in debug mode)
    print(f"[metrics] Collected: {interaction_id}", file=sys.stderr)


def main():
    """Main entry point for hook"""
    # Read event from stdin
    try:
        event_data = json.load(sys.stdin)
        collect_interaction(event_data)
    except json.JSONDecodeError:
        # No valid JSON input
        pass
    except Exception as e:
        print(f"[metrics] Error: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
