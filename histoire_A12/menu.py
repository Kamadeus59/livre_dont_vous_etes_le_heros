def menu() -> dict:
    """Création du personnage : retourne le dictionnaire gameState."""
    print("=== CRÉATION DU PERSONNAGE ===")
    nom: str = input("Quel est votre nom ? ")
    gameState: dict = {
        "nom": nom,
        "force": 7,
        "vie": 12,
        "portée": 1,
        "inventaire": [],
    }
    print(f"Bienvenue, {nom} ! Force : {gameState['force']}, Vie : {gameState['vie']}\n")
    return gameState
