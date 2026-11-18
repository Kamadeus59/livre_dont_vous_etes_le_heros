def menu() -> dict:
    """Création du personnage : retourne le dictionnaire gameState."""
    gameState: dict = {
        "nom": '',
        "inventaire": [],
        "map" : [],
        "position" : [1,1]
    }
    iteration_page = 1
    for y in range(14):
        gameState["map"].append([])
        for x in range(14):
            if x == 0 or x == 13 or y == 0 or y == 13 :
                gameState["map"][y].append(-1)
            else:
                if iteration_page < 10: 
                    gameState["map"][y].append("1" + "0"+"0"+str(iteration_page))
                elif iteration_page < 100:
                    gameState["map"][y].append("1" + "0"+str(iteration_page))
                else: 
                    gameState["map"][y].append("1" + str(iteration_page))
                iteration_page += 1
            
    return gameState
