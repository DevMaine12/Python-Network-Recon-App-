"""
Result export utility for saving scan reports to TXT files.
All reports go into the results/ directory with consistent formatting.
"""

import os
import datetime
import re


def sanitize_filename(target: str) -> str:
    """Convert target (domain/URL) to safe filename component."""
    # Replace invalid chars with underscore
    safe = re.sub(r'[^\w\-\.]', '_', target)
    # Limit length
    return safe[:50] if len(safe) > 50 else safe


def build_filename(module_name: str, target: str, extension: str = "txt") -> str:
    """Build a filename for a scan report."""
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    results_dir = os.path.join(base, "results")
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    safe_target = sanitize_filename(target)
    module_short = module_name.replace(" ", "_").lower()
    return os.path.join(results_dir, f"{module_short}_{safe_target}_{date_str}.{extension}")


def write_report(
    module_name: str,
    target: str,
    content: str,
    header_title: str = "RECON TOOLKIT SCAN REPORT"
) -> str | None:
    """
    Write a scan report to the results directory.
    Returns the file path on success, None on failure.
    """
    try:
        filepath = build_filename(module_name, target)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        report = f"""
{'=' * 52}
{header_title}
{'=' * 52}

Timestamp: {timestamp}
Module: {module_name}
Target: {target}

{content}

{'=' * 52}
Created by DevMaine12 🇨🇺 🇵🇷
{'=' * 52}
"""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(report.strip())

        return filepath
    except Exception as e:
        return None
