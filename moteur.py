"""
Moteur de "livre dont vous êtes le héros".

Organisation des fichiers :

    moteur.py
    ASCII/                 <- les dessins, un fichier par dessin
        ascii_gameover.py  <- contient def ascii_gameover()
        ascii_dragon.py    <- contient def ascii_dragon()
        ...
    OUTILS/                <- fonctions annexes réutilisables (combats...)
        combat.py
    histoire_A12/          <- un dossier par histoire
        menu.py            <- contient def menu()
        page1.py           <- contient def page1(gameState)
        page2.py           <- contient def page2(gameState)
        ...

menu() ne prend aucun paramètre : elle prépare la partie (personnage,
difficulté, règles... selon le jeu) et retourne le dictionnaire gameState de départ.

Toutes les fonctions sont typées :
    def menu() -> dict:
    def pageX(gameState: dict) -> int:

Chaque pageX(gameState) retourne le numéro de la page suivante.
Valeurs spéciales :
     0 : fin du jeu
    -1 : GAME OVER (voir ASCII/ascii_gameover.py), propose de rejouer ou de quitter
    -2 : cas non prévu. Convention des étudiants : chaque page commence par
         res = -2 et se termine par return res. Si res vaut encore -2 à la fin,
         un cas a été oublié et le moteur s'arrête avec un message d'erreur.

Pour afficher un dessin dans une page :
    from ASCII.ascii_dragon import ascii_dragon
    ascii_dragon()

Pour utiliser une fonction annexe :
    from OUTILS.combat import combat_dragon

Déroulement : menu() est appelée en premier, puis la page 1.

Lancement (le nom du dossier est obligatoire) :
    python moteur.py histoire_A12

Ce fichier suit les mêmes conventions que celles demandées aux étudiants
(un seul return par fonction, fonctions typées, pas de break / continue /
while True).
Il utilise en revanche quelques outils hors programme (importlib, inspect,
try / except, sys.exit, typing.Callable) : ils sont nécessaires pour charger les fichiers des
étudiants et afficher des messages d'erreur clairs.
"""

import importlib
import inspect
import os
import sys
import traceback
from typing import Callable

sys.dont_write_bytecode = True   # évite les dossiers __pycache__ chez les étudiants

from ASCII.ascii_gameover import ascii_gameover   # ASCII/ascii_gameover.py

PAGES_DE_FIN = (0, -1)
CAS_NON_PREVU = -2
DOSSIER_MOTEUR = os.path.dirname(os.path.abspath(__file__))


def erreur(message: str) -> None:
    """Affiche un message d'erreur lisible et arrête le programme."""
    print("\n" + "=" * 60)
    print("ERREUR :", message)
    print("=" * 60)
    sys.exit(1)


def plantage(ou: str) -> None:
    """Affiche l'erreur Python survenue dans le code de l'étudiant et arrête."""
    print("\n" + "=" * 60)
    print(f"ERREUR : le code de {ou} a planté.")
    print("Détail (regardez la dernière ligne qui cite votre fichier) :\n")
    traceback.print_exc()
    print("=" * 60)
    sys.exit(1)


def verifier_dossier(dossier: str) -> None:
    """Vérifie que le dossier de l'histoire existe et contient un menu.py."""
    if not dossier.isidentifier():
        erreur(f"Le nom de dossier '{dossier}' n'est pas valide.\n"
               f"Utilisez seulement des lettres, des chiffres et _ "
               f"(pas d'espace, pas de tiret, pas de chiffre au début).")
    chemin = os.path.join(DOSSIER_MOTEUR, dossier)
    if not os.path.isdir(chemin):
        erreur(f"Dossier '{dossier}' introuvable.\n"
               f"Il doit être dans le même dossier que moteur.py.")
    if not lister_pages(dossier):
        erreur(f"Aucun fichier pageX.py trouvé dans le dossier '{dossier}'.")


def lister_pages(dossier: str) -> list[int]:
    """Retourne la liste triée des numéros de pages (fichiers pageX.py)."""
    numeros = []
    for nom in os.listdir(os.path.join(DOSSIER_MOTEUR, dossier)):
        if nom.startswith("page") and nom.endswith(".py") and nom[4:-3].isdigit():
            numeros.append(int(nom[4:-3]))
    return sorted(numeros)


def charger_fonction(dossier: str, nom: str, nb_params: int,
                     description_params: str,
                     signature_attendue: str) -> Callable | None:
    """
    Importe dossier/nom.py et retourne la fonction qui porte le même nom
    (menu dans menu.py, page3 dans page3.py...).
    Retourne None si le fichier n'existe pas.
    """
    res = None
    fichier = f"{dossier}/{nom}.py"

    if os.path.isfile(os.path.join(DOSSIER_MOTEUR, dossier, nom + ".py")):
        module = None
        try:
            module = importlib.import_module(f"{dossier}.{nom}")
        except SyntaxError as e:
            erreur(f"Erreur de syntaxe dans '{fichier}', ligne {e.lineno} :\n"
                   f"    {(e.text or '').strip()}\n    -> {e.msg}")
        except Exception:
            plantage(f"'{fichier}' (au chargement du fichier)")

        fonction = getattr(module, nom, None)
        if fonction is None or not callable(fonction):
            trouvees = []
            for n in vars(module):
                f = getattr(module, n)
                if inspect.isfunction(f) and f.__module__ == module.__name__:
                    trouvees.append(n)
            if len(trouvees) == 0:
                trouvees = "aucune"
            erreur(f"Le fichier '{fichier}' doit contenir une fonction '{nom}'.\n"
                   f"Fonctions trouvées dans ce fichier : {trouvees}")

        signature = inspect.signature(fonction)
        nb = len(signature.parameters)
        if nb != nb_params:
            erreur(f"'{nom}' (dans '{fichier}') doit prendre {description_params}, "
                   f"elle en prend {nb}.")

        # le typage des fonctions est exigé par les consignes
        typee = signature.return_annotation is not inspect.Signature.empty
        for nom_param in signature.parameters:
            if signature.parameters[nom_param].annotation is inspect.Signature.empty:
                typee = False
        if not typee:
            erreur(f"'{nom}' (dans '{fichier}') n'est pas typée.\n"
                   f"Écrivez : {signature_attendue}")

        res = fonction

    return res


def lancer_menu(dossier: str) -> dict:
    """Appelle menu() (préparation de la partie) et vérifie qu'elle retourne un dictionnaire."""
    fonction = charger_fonction(dossier, "menu", 0, "aucun paramètre",
                                "def menu() -> dict:")
    if fonction is None:
        erreur(f"Le fichier '{dossier}/menu.py' n'existe pas.\n"
               f"Il doit contenir la fonction menu() qui prépare la partie.")

    try:
        gameState = fonction()
    except Exception:
        plantage("la fonction menu")

    if gameState is None:
        erreur("menu() n'a rien retourné (il manque un 'return' ?).\n"
               "Elle doit retourner le dictionnaire gameState de départ.")
    if not isinstance(gameState, dict):
        erreur(f"menu() a retourné {gameState!r} "
               f"(type {type(gameState).__name__}), alors qu'un dictionnaire est attendu.")
    return gameState


def trouver_page(dossier: str, numero: int, page_precedente: int | None) -> Callable:
    """Retourne la fonction pageX du fichier pageX.py, ou affiche une erreur claire."""
    nom = f"page{numero}"
    fonction = charger_fonction(dossier, nom, 1, "exactement 1 paramètre (gameState)",
                                f"def {nom}(gameState: dict) -> int:")
    if fonction is None:
        origine = (f"La page {page_precedente} a demandé d'aller à la page {numero}"
                   if page_precedente is not None
                   else f"La page de départ est {numero}")
        erreur(f"{origine}, mais le fichier '{dossier}/{nom}.py' n'existe pas.\n"
               f"Pages existantes : {lister_pages(dossier)}")
    return fonction


def verifier_retour(resultat: object, numero: int) -> None:
    """Vérifie que la page a bien retourné un numéro de page."""
    if resultat is None:
        erreur(f"La page {numero} n'a rien retourné (il manque un 'return' ?).\n"
               f"Rappel : commencez la fonction par res = -2 et terminez-la par return res.")
    # bool est un sous-type de int en Python : on l'exclut explicitement
    if isinstance(resultat, bool) or not isinstance(resultat, int):
        erreur(f"La page {numero} a retourné {resultat!r} "
               f"(type {type(resultat).__name__}), alors qu'un nombre entier "
               f"est attendu.\nAstuce : utilisez int(...) si la valeur vient d'un input().")
    if resultat == CAS_NON_PREVU:
        erreur(f"La page {numero} a retourné -2 : CAS NON PRÉVU.\n"
               f"La variable res a gardé sa valeur par défaut (-2) : dans le cas\n"
               f"qui vient de se produire, aucune ligne 'res = ...' n'a été exécutée.\n"
               f"Relisez vos if / elif / else de la page {numero} "
               f"(avez-vous prévu le cas d'un choix invalide ?).")
    if resultat < CAS_NON_PREVU:
        erreur(f"La page {numero} a retourné {resultat} : un numéro de page ne peut "
               f"pas être négatif.\nValeurs spéciales autorisées : 0 (fin du jeu), "
               f"-1 (GAME OVER), -2 (cas non prévu).")


def ecran_game_over() -> bool:
    """Affiche GAME OVER. Retourne True pour rejouer, False pour quitter."""
    res = False
    question = ("Appuyez sur R puis Entrée pour recommencer, "
                "ou sur Q puis Entrée pour quitter : ")

    ascii_gameover()
    choix = input(question).strip().upper()
    while choix != "R" and choix != "Q":
        print("Choix non reconnu.")
        choix = input(question).strip().upper()

    if choix == "R":
        print("\n" * 2)
        res = True
    else:
        print("À bientôt !")
        res = False
    return res


def partie(dossier: str) -> int:
    """Joue une partie complète (menu puis pages). Retourne 0 ou -1."""
    gameState = lancer_menu(dossier)
    page_actuelle = 1
    page_precedente = None

    while page_actuelle not in PAGES_DE_FIN:
        fonction = trouver_page(dossier, page_actuelle, page_precedente)

        try:
            resultat = fonction(gameState)
        except Exception:
            plantage(f"la page {page_actuelle}")

        verifier_retour(resultat, page_actuelle)
        page_precedente, page_actuelle = page_actuelle, resultat

    return page_actuelle


def jouer(dossier: str) -> None:
    """Enchaîne les parties tant que le joueur choisit de rejouer."""
    verifier_dossier(dossier)

    rejouer = True
    while rejouer:
        fin = partie(dossier)
        if fin == -1:
            rejouer = ecran_game_over()    # R : True, Q : False
        else:
            print("\n--- FIN DU JEU ---")
            rejouer = False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        erreur("Indiquez le dossier de l'histoire à charger.\n"
               "Exemple : python moteur.py histoire_A12")
    else:
        jouer(sys.argv[1].rstrip("/\\"))   # tolère "histoire_A12/"
