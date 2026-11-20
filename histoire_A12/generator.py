for i in range(3,145):
    if i <10:
        number = "100"+str(i)
    elif i <100:
        number = "10"+str(i)
    elif i<1000:
        number = "1"+str(i)
    open(f"page{number}.py", "w").write(
f"""
from OUTILS.map import move, afficher_map
def page{number}(gameState: dict) -> int:\n    print(\"vousetesenpage{i}\")
    res = -2
    afficher_map(gameState)
    res = move(gameState,1001)
    
    
            
        
    return res
""")
