"""
CLI layout utilities for tables and structured output.
Provides clean, readable display of scan results.
"""

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False
    Fore = type('Fore', (), {'GREEN': '', 'YELLOW': '', 'RED': '', 'WHITE': '', 'CYAN': ''})()
    Style = type('Style', (), {'RESET_ALL': '', 'BRIGHT': ''})()


def table_header(columns: list[str], widths: list[int] | None = None) -> str:
    """Create a table header row."""
    if not widths:
        widths = [max(len(c), 10) for c in columns]
    row = " | ".join(c.ljust(w) for c, w in zip(columns, widths))
    sep = "-+-".join("-" * w for w in widths)
    return f"{row}\n{sep}"


def table_row(values: list[str], widths: list[int]) -> str:
    """Create a table data row."""
    return " | ".join(str(v).ljust(w) for v, w in zip(values, widths))


def print_table(headers: list[str], rows: list[list[str]], col_widths: list[int] | None = None) -> None:
    """Print a formatted table with headers and rows."""
    if not col_widths:
        all_rows = [headers] + rows
        col_widths = [max(len(str(r[i])) for r in all_rows) + 2 for i in range(len(headers))]
    print(table_header(headers, col_widths))
    for row in rows:
        print(table_row(row, col_widths))


def separator(char: str = "-", length: int = 50) -> str:
    """Create a horizontal separator line."""
    return char * length


def print_separator(char: str = "-", length: int = 50) -> None:
    """Print a separator line."""
    print(separator(char, length))


def status_indicator(ok: bool, message: str) -> str:
    """Return a colored status indicator."""
    if HAS_COLOR:
        return f"{Fore.GREEN}[✓]{Style.RESET_ALL} {message}" if ok else f"{Fore.YELLOW}[!]{Style.RESET_ALL} {message}"
    return f"[✓] {message}" if ok else "[!] " + message
