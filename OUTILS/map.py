
def afficher_map(gameState : dict) -> dict:
    

    res: list = gameState["inventaire"]
    return res

def move(gameState : dict,Xdeplacment,Ydeplacement):
    res = -1
    position = gameState["position"]
    map = gameState["map"]
    newPosition = (position[0]+Xdeplacment,position[1]+Ydeplacement)
    Id = map[newPosition[0]][newPosition[1]]
    if Id == -1:
        res = "OutOfMap"