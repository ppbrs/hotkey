"""Helper functions."""
import os


def clear_screen() -> None:
    """Clear terminal screen."""
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        raise RuntimeError("Unsupported OS.")
