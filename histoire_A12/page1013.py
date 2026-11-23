
from OUTILS.map import move, afficher_map
def page1013(gameState: dict) -> int:
    print("vousetesenpage13")
    print(gameState["position"])
    res = -2
    afficher_map(gameState)
    res = move(gameState,1013)
    
    
            
        
    return res
