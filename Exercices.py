from random import *

def calculSalaireParSeconde(salaireHoraire, heureParJourOuvrable, jourOuvrable):
    #Assigner a salaireAnnuel, le nombre d'heure travaillées en un an
    salaireAnnuel = salaireHoraire * heureParJourOuvrable * jourOuvrable
    #Calculer, puis assigner a nombreDeSecondeParAn, le nombre de seconde dans une année non-bisextile
    nombreDeSecondeParAn = 60 * 60 * 24 * 365
    #Retourner le salaire Annuel devisé pas le nombre de seconde par an
    return salaireAnnuel / nombreDeSecondeParAn


def withdrawFees(total, percent):
    #Calculer le montant des taxes
    fees = total * (percent / 100)
    #Retourner total moins les taxes
    return total - fees

def calculSalaireNet(salaireBrut, coeff):
    #Calculer et Retourner le salaire Net a partir du salaire Brut
    #return withdrawFees(salaireBrut, coeff)

    #Si j'occupe un poste de la fonction publique
    if public :
        #alors je retourne le salaire brut - 15% de taxes
        return withdrawFees(salaireBrut, 15)
    #Sinon ? C'est que je suis travailleur dans le secteur privé, alors je retourne le salaire brut - 23% de douille à l'ancienne 
    else:
        return withdrawFees(salaireBrut, 23)


def divide(x,y):
    #Si y est égal a 0, alors la division est impossible
    if y == 0:
        print("Bah alors ?")
        return None
    #Sinon
    else:
        return x / y



def input():
    i = input("Veuillez saisir un caractère")


def mini_jeu():
    x = 0
    while i != g:
        x = x + 1
    return "Valeur trouvé en " +x+ "essai(s)"