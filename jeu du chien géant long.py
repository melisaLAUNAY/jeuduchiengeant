import random
choixSortie="rien"
while choixSortie!="quitter":
    print("Tu te trouves dans le ventre d'un chien géant!")
    print("Tu dois choisir par quel trou tu dois t'enfuir:")
    choixJoueur=input("1,2,3 ou 4?")
    if choixJoueur=="1":
        print("Haha tu es rentré en collision avec des crottes de nez!")
        print("Game over,loser!")
    elif choixJoueur=="2":
        print("Quel anus puant! Heureusement,la lumière est proche!")
        print("Bravo,tu as Gagné!!!")
        print("Maintenant, va te prendre une douche!")
    elif choixJoueur=="3":
        print("Les oreilles sont bouchées! Comment faire?")
        print("Tu peux soit:")
        print("1)Retirer la cérumen en creusant comme un fou.")
        print("2)Pisser dessus pour la faire fondre.")
        choixduDragon=input("Tape 1 ou 2")
        if choixduDragon=="1":
            print("Cela prend un temps fou! C'est impossibleeeeeeeeeee!!!!")
            print("Le monde se divise en deux catégories:")
            print ("666)ceux qui ont un pistolet chargé")
            print ("23)ceux qui creusent")
            choixUltime=input("Tape 666 ou 23")
            if choixUltime=="666":
                print("Pan Pan!")
                print("Tu es mort!")
            elif choixUltime=="23":
                print("Creuse, creuse!!!Laissons entrer la lumière!")
                print("Tu as Gagné!!!")
            else:
                print("C'est soit le chiffre de Satan soit la réponse à la question:Quel est le sens de la vie!!!!")
        elif choixduDragon=="2":
            print("Ton pipi est hautement chimique! Oh punaise!")
            print("Tu as réussi à sortir! Comme quoi les OGM c'est bon pour l'organisme!")
            print("Tu as des supers pouvoirs grâce à eux! Comme ton pipi contaminé!")
            print("Tu as Gagné!!!!")
        else:
            print("C'est 1 ou 2! Pas autre chose!")
    elif choixJoueur=="4":
        print("Tu rencontres Mr Os, et il parle!")
        print("Il te demande si tu veux jouer à un jeu?")
        choixOs=input("y ou n")
        if choixOs=="n":
            print("Va te faire foutre!")
            print("Game Over,loser!")
        elif choixOs=="y":
            print("-Si tu devines le nombre auquel je pense, je vais t'aider! dit Mr Os")
            print("Devine un chiffre entre 1 et 10")
            nombre=int(input("Quel chiffre choisis-tu?"))
            if nombre==random.randint(1,10):
                print("-Bravo,tu as deviné")
                print("-Je vais t'aider")
                print("Tu as Gagné!!!")
            else:
                print("-Je ne vais pas t'aider, tu n'as pas deviné")
                print("Game over,loser!")
    else:
        print("Désolé tu n'as pas entré 1,2,3 ou 4")
        choixSortie=input("Appuie sur Entrée pour rejouer ou tape quitter pour arrêter.")
       
