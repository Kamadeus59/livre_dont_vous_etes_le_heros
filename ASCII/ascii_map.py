carre = "#"
terrain = 

def couleurs_disponibles() -> bool:
    """True si le terminal sait afficher les couleurs ANSI."""
    res = False
    if not os.environ.get("NO_COLOR") and sys.stdout.isatty():
        if os.name == "nt":
            os.system("")   # active les couleurs ANSI dans la console Windows
        res = True
    return res

def afficher_map():
    

def ascii_map() -> None:
    """Affiche l'écran GAME OVER complet (ou la version simple sans couleurs)."""
    if couleurs_disponibles():
        print()
        afficher_map()
        print()
    else:
        print(VERSION_SIMPLE)