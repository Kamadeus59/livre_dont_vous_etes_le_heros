from OUTILS import map

def page1(gameState: dict) -> int:
    res = - 2

    a = int(input("Que voulez vous faire ?"))
    if a == "m":
        map.afficher_map(gameState)
        
    
    return res