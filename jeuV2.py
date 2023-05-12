import random

def aff (t):
    '''Affiche le jeu des allumettes'''
    for i in range(4):
        print("{0:2}.{1:12} ({2})".format (i+1,"|"*t[i],t[i]))

def int_to_bin (allu):
    '''Tranforme un entier en chaine de 3 caractères correspondant au binaire de l'entier pris en entrée'''
    alluBin = []
    for elt in allu :
        binallu = bin(elt)[2::]
        while len(binallu) != 3 :
            binallu = '0' + binallu
        alluBin.append(binallu)
    return alluBin

def paire(allu):
    '''Renvoie True si le jeu est en configuration paire, False sinon'''
    listeBin = int_to_bin(allu)
    add1 = int(listeBin[0][0]) + int(listeBin[1][0]) + int(listeBin[2][0]) + int(listeBin[3][0])
    add2 = int(listeBin[0][1]) + int(listeBin[1][1]) + int(listeBin[2][1]) + int(listeBin[3][1])
    add3 = int(listeBin[0][2]) + int(listeBin[1][2]) + int(listeBin[2][2]) + int(listeBin[3][2])
    return add1 % 2 == 0 and add2 % 2 == 0 and add3 % 2 == 0

def IAChoicePaire(allu) :
    '''Fait un choix aléatoire pour l'ordinateur'''
    alluJ = allu
    ligneIA = random.randint (0,3)
    while allu[ligneIA] == 0:
        ligneIA = random.randint(0,3)
    retireIA = random.randint (1,alluJ[ligneIA])
    print("Je retire " + str(retireIA) +" allumettes sur la ligne" + str (ligneIA) )
    allu[ligneIA] -= retireIA


def IAChoiceImpaire(allu) :
    '''Fait un choix 'intelligent' pour l'ordinateur'''
    # J'ai utilisé la variable stock, qui ne dépend pas directement de allu (je pouvais pas l'initialiser à [0,0,0,0], sinon le programme ne rentrait pas du tout dans le while)
    stock = [0,0,0,1]
    while not paire(stock) :
        possibleLigneIA = random.randint (0,3)
        while allu[possibleLigneIA] == 0:
            possibleLigneIA = random.randint(0,3)
        possibleRetireIA = random.randint (1,allu[possibleLigneIA])
        for i in range (len(allu)) : # Ici on remplit la liste stock à l'aide de la liste allu, et on retire les allumettes pour tester si la configuration est bonne
            if i == possibleLigneIA :
                stock[i] = allu[possibleLigneIA] - possibleRetireIA
            else :
                stock[i] = allu[i]
    print("Je retire " + str(possibleRetireIA) + " allumettes sur la ligne " + str(possibleLigneIA+1))
    return stock

def Game ():
    '''Fait tourner le jeu'''

    # Initialisation des variables
    allu=[1,3,5,7]
    win= False
    while allu!=[0,0,0,0]:
        aff(allu)


        # Choix du joueur

            # Choix de la ligne
        ligneJ=int(input("Sur quelle ligne voulez vous enlever une allumette? (1,2,3 ou 4)"))
        while ligneJ < 1 or ligneJ > 4:
            ligneJ = int(input("Choississez entre 1,2,3 ou 4"))
        while allu[ligneJ-1]==0:
            ligneJ = int(input("Vous avez choisi une ligne vide"))

            # Choix du nombre d'alllumettes à retirer
        retireJ = int(input("Combien d'allumettes voulez vous retirez?"))
        while retireJ > allu[ligneJ-1]:
            retireJ = int(input("Vous avez choisis trop d'allumettes."))

            # Applique le choix du joueur
        allu[ligneJ-1]= allu [ligneJ-1]- retireJ

        # Vérifie si la partie est fini
        if allu ==[0,0,0,0]:
            win= True
        aff(allu)

        # Choix de l'ordi

        if allu!= [0,0,0,0]:

            # Choix en cas de configuration paire (random)
            if paire(allu) :
                IAChoicePaire(allu)
            else :
            # Choix en cas de configuration impaire (intelligent)
                allu = IAChoiceImpaire(allu)


        # Vérifie si la partie est fini
        if allu == [0,0,0,0]:
            aff(allu)
            print("Fini")

    # Vérifie qui a gagné
    if win ==True:
        print("Vous avez gagné")

    else:
        print("Vous avez perdu")



Game()
