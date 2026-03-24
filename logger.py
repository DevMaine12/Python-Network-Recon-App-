"""
Logger utility for clean CLI output with timestamps and severity levels.
Used throughout the toolkit for consistent, readable status messages.
"""

import datetime
from typing import Optional

# Try to use colorama for colored output (works on Windows)
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False
    Fore = type('Fore', (), {'GREEN': '', 'YELLOW': '', 'RED': '', 'CYAN': '', 'WHITE': ''})()
    Style = type('Style', (), {'RESET_ALL': ''})()


def _timestamp() -> str:
    """Return current timestamp in readable format."""
    return datetime.datetime.now().strftime("%H:%M:%S")


def info(message: str) -> None:
    """Log an informational message (normal operation)."""
    ts = _timestamp()
    if HAS_COLOR:
        print(f"{Fore.CYAN}[{ts}]{Style.RESET_ALL} {Fore.GREEN}[INFO]{Style.RESET_ALL} {message}")
    else:
        print(f"[{ts}] [INFO] {message}")


def warning(message: str) -> None:
    """Log a warning message (potential issue)."""
    ts = _timestamp()
    if HAS_COLOR:
        print(f"{Fore.CYAN}[{ts}]{Style.RESET_ALL} {Fore.YELLOW}[WARNING]{Style.RESET_ALL} {message}")
    else:
        print(f"[{ts}] [WARNING] {message}")


def error(message: str, exception: Optional[Exception] = None) -> None:
    """Log an error message (something went wrong)."""
    ts = _timestamp()
    if HAS_COLOR:
        print(f"{Fore.CYAN}[{ts}]{Style.RESET_ALL} {Fore.RED}[ERROR]{Style.RESET_ALL} {message}")
    else:
        print(f"[{ts}] [ERROR] {message}")
    if exception:
        print(f"  Details: {exception}")


def success(message: str) -> None:
    """Log a success message."""
    ts = _timestamp()
    if HAS_COLOR:
        print(f"{Fore.CYAN}[{ts}]{Style.RESET_ALL} {Fore.GREEN}[OK]{Style.RESET_ALL} {message}")
    else:
        print(f"[{ts}] [OK] {message}")
