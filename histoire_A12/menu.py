def menu() -> dict:
    """Création du personnage : retourne le dictionnaire gameState."""
    gameState: dict = {
        "nom": '',
        "inventaire": ["TEST"],
        "map" : [],
        "position" : (1,1), # postion[0] = Y, postion[1] = X /// 1002 = [1,2]
        "ancienne position":(1,1),
        "ID_map" : 1001 #l'id de la tuile sur laquelle on est. Départ : 1001 
    }
    iteration_page = 1
    for y in range(14):
        gameState["map"].append([])
        for x in range(14):
            if x == 0 or x == 13 or y == 0 or y == 13 :
                gameState["map"][y].append(-1)
            else:
                if iteration_page < 10: 
                    gameState["map"][y].append("1" + "0" + "0"+str(iteration_page))
                elif iteration_page < 100:
                    gameState["map"][y].append("1" + "0"+str(iteration_page))
                else: 
                    gameState["map"][y].append("1" + str(iteration_page))
                iteration_page += 1
            
    return gameState
