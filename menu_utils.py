"""
Menu input utilities for the dashboard-style CLI.
Handles user input with ESC support to return to main dashboard.
"""

# Strings that should trigger return to dashboard
ESCAPE_INPUTS = frozenset({"esc", "ESC", "escape", "q", "Q", "quit"})


def is_escape_input(user_input: str) -> bool:
    """Check if user input means 'return to dashboard'."""
    return user_input.strip() in ESCAPE_INPUTS


def get_choice(prompt: str = "Enter choice: ", allow_escape: bool = True) -> str:
    """
    Get user choice from input. Returns 'esc' if user wants to go back.
    """
    try:
        choice = input(prompt).strip()
        if allow_escape and is_escape_input(choice):
            return "esc"
        return choice
    except (EOFError, KeyboardInterrupt):
        return "esc"


def get_input(prompt: str, default: str = "") -> tuple[str, bool]:
    """
    Get user input. Returns (value, escaped).
    If escaped is True, user wants to return to dashboard.
    """
    try:
        value = input(prompt).strip()
        if is_escape_input(value):
            return "", True
        return value if value else default, False
    except (EOFError, KeyboardInterrupt):
        return "", True


def press_enter_to_continue() -> bool:
    """
    Wait for user to press Enter. Returns True if ESC was pressed.
    """
    try:
        value = input("\nPress ENTER to continue (or ESC to return): ").strip()
        return is_escape_input(value)
    except (EOFError, KeyboardInterrupt):
        return True


def clear_screen() -> None:
    """Clear terminal screen for cleaner navigation."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
