'''Première page de l'histoire,
Reveil le jour du voyage, Choix entre placard ou bureau pour fouiller les affaires.
Pas le meme stuff dans les deux endroits, donc deux pages différentes pour la suite de l'histoire.'''
from OUTILS.combat import ouvrir_inventaire
def page1(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu
    print("Vous vous réveillez le jour de votre voyage. Vous êtes excité mais vous devez toujours vous préparer. \n")
    print("Vous ne savez plus où sont toutes vos affaires, vous vous souvenez les avoirs préparer la veille, mais la soirée avant votre départ vous a trop amoché. \n")
    print("Vous regardez l'heure : 11h58, il ne vous reste que 2 minutes pour vous préparer et partir. \n")
    print("Vous n'avez pas le temps pour chercher toutes vos affaires, vous ne pouvez fouiller que deux endroits de la chambre. \n")
    print("Vous avez deux choix : 1 - Ouvrir le placard ou 2 - Regarder sous votre bureau. \n")
    choix: str = input("Que voulez-vous faire ? (1 ou 2) : ")
    if choix == "1":
        print("Vous ouvrez donc le placard et commencé a le fouiller. \n")
        res = 2
    elif choix == "2":
        print("Vous regardez sous votre bureau et commencé a le fouiller. \n")
        res = 3
    else:
        print("Vous n'avez pas fait un choix valide. Vous perdez du temps et vous ne pouvez pas vous préparer correctement. \n")
        res = 1


    

    return res
