import os
import sys

def couleurs_disponibles() -> bool:
    """True si le terminal sait afficher les couleurs ANSI."""
    res = False
    if not os.environ.get("NO_COLOR") and sys.stdout.isatty():
        if os.name == "nt":
            os.system("")   # active les couleurs ANSI dans la console Windows
        res = True
    return res