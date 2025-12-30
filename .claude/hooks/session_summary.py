#!/usr/bin/env python3
"""
Session summary hook for Claude Code
Author: Anderson Henrique da Silva

Generates a summary of the session when it ends,
aggregating metrics collected during the session.
"""

import json
import sys
import os
from datetime import datetime
from pathlib import Path

# Configuration
METRICS_DIR = Path(__file__).parent.parent.parent / "evidence" / "metrics" / "data"
SESSIONS_DIR = Path(__file__).parent.parent.parent / "evidence" / "metrics" / "sessions"
SESSIONS_DIR.mkdir(parents=True, exist_ok=True)


def summarize_session(event_data: dict) -> None:
    """Generate summary for completed session"""

    session_id = event_data.get("session_id", "unknown")
    reason = event_data.get("reason", "unknown")
    transcript_path = event_data.get("transcript_path")

    # Count metrics from this session
    session_metrics = []
    for file in METRICS_DIR.glob("*.json"):
        try:
            with open(file) as f:
                metric = json.load(f)
                if metric.get("session_id") == session_id:
                    session_metrics.append(metric)
        except (json.JSONDecodeError, KeyError):
            continue

    # Build session summary
    summary = {
        "session_id": session_id,
        "ended_at": datetime.now().isoformat(),
        "end_reason": reason,
        "transcript_path": transcript_path,
        "project": os.getcwd(),
        "metrics": {
            "total_tool_uses": len(session_metrics),
            "tools_used": list(set(
                m.get("tool_name") for m in session_metrics
                if m.get("tool_name")
            )),
        }
    }

    # Parse transcript if available
    if transcript_path and Path(transcript_path).exists():
        try:
            summary["metrics"]["transcript_analyzed"] = True
            # Could analyze transcript for more detailed metrics
        except Exception:
            summary["metrics"]["transcript_analyzed"] = False

    # Save session summary
    output_file = SESSIONS_DIR / f"session_{session_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, 'w') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print(f"[session] Summary saved: {output_file.name}", file=sys.stderr)


def main():
    """Main entry point"""
    try:
        event_data = json.load(sys.stdin)
        summarize_session(event_data)
    except json.JSONDecodeError:
        pass
    except Exception as e:
        print(f"[session] Error: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
