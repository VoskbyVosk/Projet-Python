import random


#DEBUT

#On créer le plateau de jeu de 3x3
x = [["▢", "▢", "▢"], ["▢", "▢", "▢"], ["▢", "▢", "▢"]]

#On affiche le plateau vide
print("Voici le tableau du jeu ainsi que les coordonnées de chaque case : \n")
print(x[0][0], " ", x[0][1], " ", x[0][2],)
print(x[1][0], " ", x[1][1], " ", x[1][2],)
print(x[2][0], " ", x[2][1], " ", x[2][2],)
print()

#
def morpion(turn, nbtour): 
    #Si c'est le tour du joueur 1 (ici le joueur physique)
    if turn == "J1" :
        #Demander la case que le joueur veut changer et prendre sa valeur dans la variable "choix"
        choix = input("J1 : Insérer la case que vous voulez changer : ")
        print()
        #Conditions pour faire correspondre l'entrée du joueur avec la case correspondante, uniquement si elle est vide
        #Ligne 1
        if choix == "1" and x[0][0] == "▢":
            x[0][0] = "⊛"
            nbtour = nbtour+1
        elif choix == "2" and x[0][1] == "▢":
            x[0][1] = "⊛"
            nbtour = nbtour+1
        elif choix == "3" and x[0][2] == "▢":
            x[0][2] = "⊛"
            nbtour = nbtour+1

        #Ligne 2
        elif choix == "4" and x[1][0] == "▢":
            x[1][0] = "⊛"
            nbtour = nbtour+1
        elif choix == "5" and x[1][1] == "▢":
            x[1][1] = "⊛"
            nbtour = nbtour+1
        elif choix == "6" and x[1][2] == "▢":
            x[1][2] = "⊛"
            nbtour = nbtour+1

        #Ligne 3
        elif choix == "7" and x[2][0] == "▢":
            x[2][0] = "⊛"
            nbtour = nbtour+1
        elif choix == "8" and x[2][1] == "▢":
            x[2][1] = "⊛"
            nbtour = nbtour+1
        elif choix == "9" and x[2][2] == "▢":
            x[2][2] = "⊛"
            nbtour = nbtour+1

        #Sinon afficher le message d'erreur et renvoyer le joueur au choix de la case
        else :
            print("Erreur : La case sélectionnée est soit déjà pleine soit inexistante !")
            morpion(turn, nbtour)
            
        #Afficher le tableau après que le joueur ait joué
        print("Voici le tableau du jeu ainsi que les coordonnées de chaque case : \n")
        print(x[0][0], " ", x[0][1], " ", x[0][2],)
        print(x[1][0], " ", x[1][1], " ", x[1][2],)
        print(x[2][0], " ", x[2][1], " ", x[2][2],)
        print()
        #Appeler la fonction "checkIfWin" pour le joueur 1 qui vérifiera si ce joueur a gagné la partie ou non
        checkIfWin("J1", nbtour)

    #Quand c'est le tour du Joueur 2
    elif turn == "J2" :

        #Si le tour est le premier, vérifier si le joueur a joué soit au milieu soit autre part, et placer la croix en fonction du choix du joueur
        if nbtour == 1 :
            if x[1][1] == "▢" :
                x[1][1] = "✕"
                nbtour = nbtour + 1
            else :
                x[0][2] = "✕"
                nbtour = nbtour + 1

        #Il y a un bug qui n'est malheureusement pas de mon ressort, donc si le numéro du tour est mauvais, lui rajouter 1 puis rappeler la fonction "morpion"
        elif nbtour == 4 :
            nbtour = nbtour + 1
            morpion("J2", nbtour)
        elif nbtour == 6 :
            nbtour = nbtour + 1
            morpion("J2", nbtour)
        elif nbtour == 8 :
            nbtour = nbtour + 1
            morpion("J2", nbtour)

        #Sinon si le tour est le troisième, vérifier que les mouvements seulement réalisables au tour 3 et non pris en compte par la fonction "verifbot" soient existant et les contrer
        #Sinon, appeler la fonction "verifbot"
        elif nbtour == 3 :
            #Coin haut gauche
            if x[0][0] == "⊛" :
                if x[2][1] == "⊛":
                    x[2][0] = "✕"
                    nbtour = nbtour + 1
                elif x[1][2] == "⊛" :
                    x[0][2] = "✕"
                    nbtour = nbtour + 1
                elif x[2][2] == "⊛" :
                    x[0][1] = "✕"
                    nbtour = nbtour + 1
                else :
                    verifbot(nbtour)
            #Coin haut droite
            elif x[0][2] == "⊛" :
                if x[2][1] == "⊛":
                    x[2][2] = "✕"
                    nbtour = nbtour + 1
                elif x[1][0] == "⊛" :
                    x[0][0] = "✕"
                    nbtour = nbtour + 1
                elif x[2][0] == "⊛" :
                    x[0][1] = "✕"
                    nbtour = nbtour + 1
                else :
                    verifbot(nbtour)
            #Coin bas gauche
            elif x[2][0] == "⊛" :
                if x[0][1] == "⊛":
                    x[0][0] = "✕"
                    nbtour = nbtour + 1
                elif x[1][2] == "⊛" :
                    x[2][2] = "✕"
                    nbtour = nbtour + 1
                elif x[0][2] == "⊛" :
                    x[2][1] = "✕"
                    nbtour = nbtour + 1
                else :
                    verifbot(nbtour)
            #Coin bas droite
            elif x[2][2] == "⊛" :
                if x[0][1] == "⊛":
                    x[0][2] = "✕"
                    nbtour = nbtour + 1
                elif x[1][0] == "⊛" :
                    x[2][0] = "✕"
                    nbtour = nbtour + 1
                elif x[0][0] == "⊛" :
                    x[2][1] = "✕"
                    nbtour = nbtour + 1
                else :
                    verifbot(nbtour)
            else : 
                verifbot(nbtour)

        #Sinon si le tour est le cinquiè^me appeler la fonction "verifbot"
        elif nbtour == 5 :
            verifbot(nbtour)

        #Sinon si le tour est le septième, appeler la fonction "verifbot qui saura contrer n'importe quel mouvement du septième tour"
        elif nbtour == 7 :
            verifbot(nbtour)

        #Afficher le tableau après que le bot ait joué
        print("Voici le tableau du jeu ainsi que les coordonnées de chaque case : \n")
        print(x[0][0], " ", x[0][1], " ", x[0][2],)
        print(x[1][0], " ", x[1][1], " ", x[1][2],)
        print(x[2][0], " ", x[2][1], " ", x[2][2],)
        print()
        #Appeler la fonction "checkIfWin" pour le joueur 2 qui vérifiera si ce joueur a gagné la partie ou non (ici le bot)
        checkIfWin("J2", nbtour)

    #Sinon si ce n'est pas le tour d'un joueur et donc que quelqu'un a gagné la partie ou qu'il y a égalité
    elif turn == "no" :
        #Alors demander au joueur si il veut recommencer et implémenter son choix dans la variable "re"
        re = input("Voulez-vous recommencer ? ")
        #Tant que le choix du joueur "re" est différent de "oui"
        while re != "oui":
            #Si la réponse du joueur est "non"
            if re == "non" :
                #Alors afficher un message d'au revoir et terminer le code (return ne fonctionne pas pour dieu ne sait quelle raison)
                print("Au revoir !")
                exit()
            #Sinon
            else :
                #Alors afficher un message d'erreur et redemander le choix du joueur
                re = input("Réponse incorrecte. Voulez-vous recommencer ? ")
        #Sinon
        else :
                #Afficher un message de bonne chance
                print("Bonne chance !")
                #Réinitialiser le tableau du morpion
                x[0][0] = "▢"
                x[0][1] = "▢"
                x[0][2] = "▢"
                x[1][0] = "▢"
                x[1][1] = "▢"
                x[1][2] = "▢"
                x[2][0] = "▢"
                x[2][1] = "▢"
                x[2][2] = "▢"
                #Afficher le tableau vide avec toute les coordonées correspondantes aux cases
                print("Voici le tableau du jeu ainsi que les coordonnées de chaque case : \n")
                print(x[0][0], " ", x[0][1], " ", x[0][2],)
                print(x[1][0], " ", x[1][1], " ", x[1][2],)
                print(x[2][0], " ", x[2][1], " ", x[2][2],)
                #Réinitialiser le nombre de tours
                nbtour = 0
                #Appeler la fonction "morpion" avec comme paramètre le joueur dont c'est le tour
                morpion("J1", nbtour)

#Créer une fonction "verifbot" qui permettra de vérifier si il y a 2 croix dans la même ligne, colonne ou diagonale et de compléter avec une troisième croix
#Et si il n'y a aucune croix à compléter, alors vérifier si il y a 2 cercles dans la même ligne, colonne ou diagonale et compléter la troisième case avec une croix
def verifbot(nbtour) :

    #Verifier si il y a deux croix côte à côte, si oui et que la troisième case est vide, alors placer une croix
    #Ligne 1
    if x[0][0] == "✕" and x[0][1] == "✕" and x[0][2] != "⊛" :
        x[0][2] = "✕"
        nbtour = nbtour + 1
        return
    elif x[0][1] == "✕" and x[0][2] == "✕" and x [0][0] != "⊛" :
        x[0][0] = "✕"
        nbtour = nbtour + 1
        return
    elif x[0][0] == "✕" and x[0][2] == "✕" and x[0][1] != "⊛" :
        x[0][1] = "✕"
        nbtour = nbtour + 1
        return
    #Ligne 2
    elif x[1][0] == "✕" and x[1][1] == "✕" and x[1][2] != "⊛" :
        x[1][2] = "✕"
        nbtour = nbtour + 1
        return
    elif x[1][1] == "✕" and x[1][2] == "✕" and x [1][0] != "⊛" :
        x[1][0] = "✕"
        nbtour = nbtour + 1
        return
    elif x[1][0] == "✕" and x[1][2] == "✕" and x[1][1] != "⊛" :
        x[1][1] = "✕"
        nbtour = nbtour + 1
        return
    #Ligne 3
    elif x[2][0] == "✕" and x[2][1] == "✕" and x[2][2] != "⊛" :
        x[2][2] = "✕"
        nbtour = nbtour + 1
        return
    elif x[2][1] == "✕" and x[2][2] == "✕" and x [2][0] != "⊛" :
        x[2][0] = "✕"
        nbtour = nbtour + 1
        return
    elif x[2][0] == "✕" and x[2][2] == "✕" and x[2][1] != "⊛" :
        x[2][1] = "✕"
        nbtour = nbtour + 1
        return
    #Colonne 1
    elif x[0][0] == "✕" and x[1][0] == "✕" and x[2][0] != "⊛" :
        x[2][0] = "✕"
        nbtour = nbtour + 1
        return
    elif x[0][0] == "✕" and x[2][0] == "✕" and x[1][0] != "⊛" :
        x[1][0] = "✕"
        nbtour = nbtour + 1
        return
    elif x[1][0] == "✕" and x[2][0] == "✕" and x[0][0] != "⊛" :
        x[0][0] = "✕"
        nbtour = nbtour + 1
        return
    #Colonne 2
    elif x[0][1] == "✕" and x[1][1] == "✕" and x[2][1] != "⊛" :
        x[2][1] = "✕"
        nbtour = nbtour + 1
        return
    elif x[0][1] == "✕" and x[2][1] == "✕" and x[1][1] != "⊛" :
        x[1][1] = "✕"
        nbtour = nbtour + 1
        return
    elif x[1][1] == "✕" and x[2][1] == "✕" and x[0][1] != "⊛" :
        x[0][1] = "✕"
        nbtour = nbtour + 1
        return
    #Colonne 3
    elif x[0][2] == "✕" and x[1][2] == "✕" and x[2][2] != "⊛" :
        x[2][2] = "✕"
        nbtour = nbtour + 1
        return
    elif x[0][2] == "✕" and x[2][2] == "✕" and x[1][2] != "⊛" :
        x[1][2] = "✕"
        nbtour = nbtour + 1
        return
    elif x[1][2] == "✕" and x[2][2] == "✕" and x[0][2] != "⊛" :
        x[0][2] = "✕"
        nbtour = nbtour + 1
        return
    #Diagonale 1
    elif x[0][0] == "✕" and x[1][1] == "✕" and x[2][2] != "⊛" :
        x[2][2] = "✕"
        nbtour = nbtour + 1
        return
    elif x[1][1] == "✕" and x[2][2] == "✕" and x[0][0] != "⊛" :
        x[0][0] = "✕"
        nbtour = nbtour + 1
        return
    elif x[2][2] == "✕" and x[0][0] == "✕" and x[1][1] != "⊛" :
        x[1][1] = "✕"
        nbtour = nbtour + 1
        return
    #Diagonale 2
    elif x[0][2] == "✕" and x[1][1] == "✕" and x[2][0] != "⊛" :
        x[2][0] = "✕"
        nbtour = nbtour + 1
        return
    elif x[1][1] == "✕" and x[2][0] == "✕" and x[0][2] != "⊛" :
        x[0][2] = "✕"
        nbtour = nbtour + 1
        return
    elif x[2][0] == "✕" and x[0][2] == "✕" and x[1][1] != "⊛" :
        x[1][1] = "✕"
        nbtour = nbtour + 1
        return

    #Verifier si il y a deux cercles côte à côte, si oui et que la troisième case est vide, alors placer une croix
    #Ligne 1
    elif x[0][0] == "⊛" and x[0][1] == "⊛" and x[0][2] != "✕" :
        x[0][2] = "✕"
        nbtour = nbtour + 1
        return
    elif x[0][1] == "⊛" and x[0][2] == "⊛" and x [0][0] != "✕" :
        x[0][0] = "✕"
        nbtour = nbtour + 1
        return
    elif x[0][0] == "⊛" and x[0][2] == "⊛" and x[0][1] != "✕" :
        x[0][1] = "✕"
        nbtour = nbtour + 1
        return
    #Ligne 2
    elif x[1][0] == "⊛" and x[1][1] == "⊛" and x[1][2] != "✕" :
        x[1][2] = "✕"
        nbtour = nbtour + 1
        return
    elif x[1][1] == "⊛" and x[1][2] == "⊛" and x [1][0] != "✕" :
        x[1][0] = "✕"
        nbtour = nbtour + 1
        return
    elif x[1][0] == "⊛" and x[1][2] == "⊛" and x[1][1] != "✕" :
        x[1][1] = "✕"
        nbtour = nbtour + 1
        return
    #Ligne 3
    elif x[2][0] == "⊛" and x[2][1] == "⊛" and x[2][2] != "✕" :
        x[2][2] = "✕"
        nbtour = nbtour + 1
        return
    elif x[2][1] == "⊛" and x[2][2] == "⊛" and x [2][0] != "✕" :
        x[2][0] = "✕"
        nbtour = nbtour + 1
        return
    elif x[2][0] == "⊛" and x[2][2] == "⊛" and x[2][1] != "✕" :
        x[2][1] = "✕"
        nbtour = nbtour + 1
        return
    #Colonne 1
    elif x[0][0] == "⊛" and x[1][0] == "⊛" and x[2][0] != "✕" :
        x[2][0] = "✕"
        nbtour = nbtour + 1
        return
    elif x[0][0] == "⊛" and x[2][0] == "⊛" and x[1][0] != "✕" :
        x[1][0] = "✕"
        nbtour = nbtour + 1
        return
    elif x[1][0] == "⊛" and x[2][0] == "⊛" and x[0][0] != "✕" :
        x[0][0] = "✕"
        nbtour = nbtour + 1
        return
    #Colonne 2
    elif x[0][1] == "⊛" and x[1][1] == "⊛" and x[2][1] != "✕" :
        x[2][1] = "✕"
        nbtour = nbtour + 1
        return
    elif x[0][1] == "⊛" and x[2][1] == "⊛" and x[1][1] != "✕" :
        x[1][1] = "✕"
        nbtour = nbtour + 1
        return
    elif x[1][1] == "⊛" and x[2][1] == "⊛" and x[0][1] != "✕" :
        x[0][1] = "✕"
        nbtour = nbtour + 1
        return
    #Colonne 3
    elif x[0][2] == "⊛" and x[1][2] == "⊛" and x[2][2] != "✕" :
        x[2][2] = "✕"
        nbtour = nbtour + 1
        return
    elif x[0][2] == "⊛" and x[2][2] == "⊛" and x[1][2] != "✕" :
        x[1][2] = "✕"
        nbtour = nbtour + 1
        return
    elif x[1][2] == "⊛" and x[2][2] == "⊛" and x[0][2] != "✕" :
        x[0][2] = "✕"
        nbtour = nbtour + 1
        return
    #Diagonale
    elif x[0][0] == "⊛" and x[1][1] == "⊛" and x[2][2] != "✕" :
        x[2][2] = "✕"
        nbtour = nbtour + 1
        return
    elif x[1][1] == "⊛" and x[2][2] == "⊛" and x[0][0] != "✕" :
        x[0][0] = "✕"
        nbtour = nbtour + 1
        return
    elif x[2][2] == "⊛" and x[0][0] == "⊛" and x[1][1] != "✕" :
        x[1][1] = "✕"
        nbtour = nbtour + 1
        return
    #Diagonale 2
    elif x[0][2] == "⊛" and x[1][1] == "⊛" and x[2][0] != "✕" :
        x[2][0] = "✕"
        nbtour = nbtour + 1
        return
    elif x[1][1] == "⊛" and x[2][0] == "⊛" and x[0][2] != "✕" :
        x[0][2] = "✕"
        nbtour = nbtour + 1
        return
    elif x[2][0] == "⊛" and x[0][2] == "⊛" and x[1][1] != "✕" :
        x[1][1] = "✕"
        nbtour = nbtour + 1
        return

    #Sinon
    else :
        #Si aucune des conditions au dessus sont valides, vérifier ces conditions-ci qui sont des cas plus spécifiques
        if x[0][0] == "▢" :
            x[0][0] = "✕"
            nbtour = nbtour + 1
            return
        elif x[0][1] == "▢" :
            x[0][1] = "✕"
            nbtour = nbtour + 1
            return
        elif x[0][2] == "▢" :
            x[0][2] = "✕"
            nbtour = nbtour + 1
            return
        elif x[1][0] == "▢" :
            x[1][0] = "✕"
            nbtour = nbtour + 1
            return
        elif x[1][1] == "▢" :
            x[1][1] = "✕"
            nbtour = nbtour + 1
            return
        elif x[1][2] == "▢" :
            x[1][2] = "✕"
            nbtour = nbtour + 1
            return
        elif x[2][0] == "▢" :
            x[2][0] = "✕"
            nbtour = nbtour + 1
            return
        elif x[2][1] == "▢" :
            x[2][1] = "✕"
            nbtour = nbtour + 1
            return
        elif x[2][2] == "▢" :
            x[2][2] = "✕"
            nbtour = nbtour + 1
            return
        else :
            return
    

#Créer une fonction "checkIfWin" qui vérifier si un joueur a gagné ou pas à chaque tour
def checkIfWin(turn, nbtour):

    #Si c'est le tour du joueur 1
    if turn == "J1" :

        #Si une des trois lignes comprant 3 cercles
        #Alors le joueur 1 gagne et on renvoie la fonction morpion avec la fin de match comme condition après afficher que le joueur a gagné
        if x[0][0] == "⊛" and x[0][1] == "⊛" and x[0][2] == "⊛" :
            print("J1 Wins")
            morpion("no", nbtour)
        elif x[1][0] == "⊛" and x[1][1] == "⊛" and x[1][2] == "⊛" :
            print("J1 Wins")
            morpion("no", nbtour)
        elif x[2][0] == "⊛" and x[2][1] == "⊛" and x[2][2] == "⊛" :
            print("J1 Wins")
            morpion("no", nbtour)
        #Si une des trois colonnes comprant 3 cercles
        #Alors le joueur 1 gagne et on renvoie la fonction morpion avec la fin de match comme condition après afficher que le joueur a gagné
        elif x[0][0] == "⊛" and x[1][0] == "⊛" and x[2][0] == "⊛" :
            print("J1 Wins")
            morpion("no", nbtour)
        elif x[0][1] == "⊛" and x[1][1] == "⊛" and x[2][1] == "⊛" :
            print("J1 Wins")
            morpion("no", nbtour)
        elif x[0][2] == "⊛" and x[1][2] == "⊛" and x[2][2] == "⊛" :
            print("J1 Wins")
            morpion("no", nbtour)
        #Si une des deux diagonales comprant 3 cercles
        #Alors le joueur 1 gagne et on renvoie la fonction morpion avec la fin de match comme condition après afficher que le joueur a gagné
        elif x[0][0] == "⊛" and x[1][1] == "⊛" and x[2][2] == "⊛" :
            print("J1 Wins")
            morpion("no", nbtour)
        elif x[0][2] == "⊛" and x[1][1] == "⊛" and x[2][0] == "⊛" :
            print("J1 Wins")
            morpion("no", nbtour)
        #Si le tour est le neuvième et donc après avoir vérifier si le joueur a gagné
        elif nbtour == 9 :
            #Alors afficher l'égalité et renvoyer la fonction morpion avec la fin de match comme condition
            print("Egalité")
            morpion("no", nbtour)
        #Sinon
        else :
            #Alors renvoyer la fonction morpion avec le joueur dont c'est le tour
            morpion("J2", nbtour)

    #Si c'est le tour du joueur 2 (ici le bot)
    elif turn == "J2" :

        #Si une des trois lignes comprant 3 croix
        #Alors le joueur 2 gagne et on renvoie la fonction morpion avec la fin de match comme condition après afficher que le joueur a gagné
        if x[0][0] == "✕"  and x[0][1] == "✕"  and x[0][2] == "✕" :
            print("The Bot Wins")
            morpion("no", nbtour)
        elif x[1][0] == "✕"  and x[1][1] == "✕"  and x[1][2] == "✕" :
            print("The Bot Wins")
            morpion("no", nbtour)
        elif x[2][0] == "✕"  and x[2][1] == "✕"  and x[2][2] == "✕" :
            print("The Bot Wins")
            morpion("no", nbtour)
        #Si une des trois colonnes comprant 3 croix
        #Alors le joueur 2 gagne et on renvoie la fonction morpion avec la fin de match comme condition après afficher que le joueur a gagné
        elif x[0][0] == "✕"  and x[1][0] == "✕"  and x[2][0] == "✕" :
            print("The Bot Wins")
            morpion("no", nbtour)
        if x[0][1] == "✕"  and x[1][1] == "✕"  and x[2][1] == "✕" :
            print("The Bot Wins")
            morpion("no", nbtour)
        elif x[0][2] == "✕"  and x[1][2] == "✕"  and x[2][2] == "✕" :
            print("The Bot Wins")
            morpion("no", nbtour)
        #Si une des deux diagonales comprant 3 croix
        #Alors le joueur 2 gagne et on renvoie la fonction morpion avec la fin de match comme condition après afficher que le joueur a gagné
        elif x[0][0] == "✕"  and x[1][1] == "✕"  and x[2][2] == "✕" :
            print("The Bot Wins")
            morpion("no", nbtour)
        elif x[0][2] == "✕"  and x[1][1] == "✕"  and x[2][0] == "✕" :
            print("The Bot Wins")
            morpion("no", nbtour)
        #Si le tour est le neuvième et donc après avoir vérifier si le joueur a gagné
        elif nbtour == 9 :
            #Alors afficher l'égalité et renvoyer la fonction morpion avec la fin de match comme condition
            print("Egalité")
            morpion("no", nbtour)
        #Sinon
        else :
            #Alors renvoyer la fonction morpion avec le joueur dont c'est le tour
            morpion("J1", nbtour)

#Appeler la fonction morpion au tour 0 avec le joueur qui commence
morpion("J1", 0)
#FIN