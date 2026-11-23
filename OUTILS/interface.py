from ASCII import ascii_interface
from OUTILS import map
from OUTILS import inventaire
def interface():
    '''
    Affiche l'interface du jeu.
    '''
    ascii_interface.afficher_menu()
    #afficher le menu
    validAnswer = False

def ouvrir_map(gameState):
    '''
    Permet d'afficher la map dans le cmd
    '''
    map.afficher_map(gameState)

def ouvrir_inventaire(gameState):
    '''
    Permet d'afficher l'interface dans le cmd
    '''
    inventaire.ouvrir_inventaire(gameState)


