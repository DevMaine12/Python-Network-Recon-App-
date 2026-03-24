#!/usr/bin/env python3
"""
Recon Toolkit - Defensive Cybersecurity Reconnaissance

A modular CLI toolkit for educational cybersecurity learning.
Port scanning, DNS analysis, directory discovery, and HTTP header analysis.

Author: DevMaine12 🇨🇺 🇵🇷
"""

import sys
import os
import io

# Ensure UTF-8 output for Windows console (supports emoji in creator credit)
if sys.platform == "win32":
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    except (AttributeError, OSError):
        pass

# Ensure we can import from project root
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dashboard.dashboard import run_dashboard


def main() -> None:
    """Entry point for the Recon Toolkit."""
    try:
        run_dashboard()
    except KeyboardInterrupt:
        print("\n\nInterrupted. Exiting safely.")
        sys.exit(0)
    except Exception as e:
        print(f"\n[FATAL] Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
