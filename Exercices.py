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
    return withdrawFees(salaireBrut; coeff)
