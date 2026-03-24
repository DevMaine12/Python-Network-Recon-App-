"""
ASCII banner for the Recon Toolkit CLI.
Clean, professional appearance without excessive art.
"""

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False
    Fore = type('Fore', (), {'CYAN': '', 'WHITE': '', 'RED': ''})()
    Style = type('Style', (), {'RESET_ALL': '', 'BRIGHT': ''})()


def show_banner() -> None:
    """Display the main application banner."""
    banner = """
+==========================================================+
|              R E C O N   T O O L K I T                   |
|         Defensive Cybersecurity Reconnaissance           |
+==========================================================+
"""
    if HAS_COLOR:
        print(f"{Fore.CYAN}{banner}{Style.RESET_ALL}")
    else:
        print(banner)


def show_module_banner(title: str) -> None:
    """Display a module-specific banner."""
    width = 50
    line = "=" * width
    header = f"\n{line}\n{title.center(width)}\n{line}\n"
    if HAS_COLOR:
        print(f"{Fore.CYAN}{header}{Style.RESET_ALL}")
    else:
        print(header)
