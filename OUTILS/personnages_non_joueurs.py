PNJ_dialogues : dict = {
    "Mia" : {
        "introduction" : ["bonjour !",
             ["Bonjour, ça va ?","1"],
             ["où est le boss ?","1"],
             ["dis moi bonjour !","1"],
             ["au revoir !", "quit"]
            ]
        ,
        "1":["ça marche !",
             ["Tu peux juste dire ça gros","introduction"]
            ]
    }
}

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
        for choix in range(1,len(PNJ[Stade_de_la_conversation])):
            choix_possibles.append(str(choix))
        
        #print tous les choix possibles de discussion
        for texteId in choix_possibles:
            print("    ", texteId,":",PNJ[Stade_de_la_conversation][int(texteId)][0])
        print()
        print("     q pour quitter")

        
        Choix_de_l_utilisateur = input(">")

        #vérification que le choix est valide et traitement du choix

        while (not Choix_de_l_utilisateur.isdigit() or not (Choix_de_l_utilisateur in choix_possibles)) and (not Choix_de_l_utilisateur=="q" or Choix_de_l_utilisateur=="Q"):
            print("    refais gros")
            Choix_de_l_utilisateur = input("    parler :")
        if Choix_de_l_utilisateur == "q" or Choix_de_l_utilisateur =="Q":
            Conversation_en_cours = False
        else:
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

