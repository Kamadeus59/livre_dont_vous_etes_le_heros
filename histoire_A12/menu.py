def menu() -> dict:
    """Création du personnage : retourne le dictionnaire gameState."""
    print("=== CRÉATION DU PERSONNAGE ===")
    nom: str = input("Quel est votre nom ? ")
    gameState: dict = {
        "nom": nom,
        "inventaire": [],
        "map" : []
    }
    print(f"Bienvenue, {nom}")
    iteration_page = 1
    for i in range(12):
        gameState["map"].append([])
        for j in range(12):
            gameState["map"][i].append(iteration_page)
            iteration_page += 1
            
    print(gameState["map"])


    return gameState
