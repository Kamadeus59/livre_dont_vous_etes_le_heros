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
    for i in range(14):
        gameState["map"].append([])
        for j in range(14):
            if j == 0 or j == 13 or i == 0 or i == 13 :
                gameState["map"][i].append(-1)
            else:
                if iteration_page < 10: 
                    gameState["map"][i].append("0"+"0"+str(iteration_page))
                elif iteration_page < 100:
                    gameState["map"][i].append("0"+str(iteration_page))
                else: 
                    gameState["map"][i].append(iteration_page)
                iteration_page += 1
            
    print(gameState["map"])


    return gameState
