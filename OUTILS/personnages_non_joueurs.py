PNJ_dialogues : dict = {
    "Mia" : {
        "introduction" : ["bonjour !",
             ["Bonjour, ça va ?","1"],
             ["où est le boss ?","2"],
             ["dis moi bonjour !","1"],
             ["au revoir !", "quit"]
            ]
        ,
        "1":["ça marche !",
             ["Tu peux juste dire ça gros","introduction"]
        ]
        ,
        "2":["alors euuuuh",["","3"]]
        ,
        "3":["attends que je réfléchisse", ["j'attends","2"]]
        
    }
}
"""
PNJ_dialogues contient les PNJs
Un PNJ Contient plusieurs états de conversation
Un état de conversation contient plusieurs choix
Chaque choix contient : son texte dis par le joueur PUIS l'état de conversation auquel ça va mener
Si il n'y a qu'un choix : le choix est pris en appuyant sur entrée
"""
def dialoguer_avec_PNJ(nom:str,gameState):
    PNJ = PNJ_dialogues[nom]
    Conversation_en_cours = True
    Stade_de_la_conversation = "introduction"
    while Conversation_en_cours:
        print()
        print(f"----------->                {nom} :    ",end ="")
        print(PNJ[Stade_de_la_conversation][0])
        print()

        #obtenir tous les choix possibles
        choix_possibles = []
        un_seul_choix = len(PNJ[Stade_de_la_conversation])==2
        if un_seul_choix: #cas où on peut juste aller à la suite
            print("    Entrée pour continuer")
        else:
            for choix in range(1,len(PNJ[Stade_de_la_conversation])):
                choix_possibles.append(str(choix))
            
            #print tous les choix possibles de discussion
            for texteId in choix_possibles:
                print("    ", texteId,":",PNJ[Stade_de_la_conversation][int(texteId)][0])
        print()
        print("     q pour quitter")

        
        Choix_de_l_utilisateur = input(">")
        if un_seul_choix and Choix_de_l_utilisateur=="":
            Choix_de_l_utilisateur = "1"
        else: #vérification que le choix est valide et traitement du choix

            while (not Choix_de_l_utilisateur.isdigit() or not (Choix_de_l_utilisateur in choix_possibles)) and (not Choix_de_l_utilisateur=="q" or Choix_de_l_utilisateur=="Q"):
                print("Entre un choix valide !")
                Choix_de_l_utilisateur = input(">")

        
        if Choix_de_l_utilisateur == "q" or Choix_de_l_utilisateur =="Q":
            Conversation_en_cours = False
        else: #process le choix du joueur
            if PNJ[Stade_de_la_conversation][int(Choix_de_l_utilisateur)][0] != "":
                print()
                print(f"----------->                {gameState["nom"]} :    ",end ="")
                print(PNJ[Stade_de_la_conversation][int(Choix_de_l_utilisateur)][0])
                print()
            Stade_de_la_conversation = PNJ[Stade_de_la_conversation][int(Choix_de_l_utilisateur)][1]


        if Stade_de_la_conversation == "quit":
            Conversation_en_cours = False
            
        """while (not Choix_de_l_utilisateur.isdigit()) or (int(Choix_de_l_utilisateur) not in range(1,len(PNJ[Stade_de_la_conversation]))):
            print("veuillez entrer un choix valide !")
            Choix_de_l_utilisateur = (input("parler :"))
        Stade_de_la_conversation = int(Choix_de_l_utilisateur)"""

