from ASCII import ascii_map 

def afficher_map(gameState : dict) -> dict:
    print("1")
    ascii_map.ascii_map()

    res: list = gameState["inventaire"]
    return res

'''def move(gameState : dict,Xdeplacment,Ydeplacement) -> str:
    res : str= "Error"
    position : tuple= gameState["position"]
    map : list= gameState["map"]
    newPosition : tuple= (position[0]+Xdeplacment,position[1]+Ydeplacement)
    Id : number = map[newPosition[0]][newPosition[1]]
    if Id == -1:
        res = "OutOfMap"
    else:
        res = f"GoToTileNumber{Id}"
    print(res)
    return res'''