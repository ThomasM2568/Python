from random import *

grille1=[[randint(0,2),randint(0,2),randint(0,2)],[randint(0,2),randint(0,2),randint(0,2)],[randint(0,2),randint(0,2),randint(0,2)]]

def affichage(grille):
    for i in range(len(grille)):
        print(grille[i])



def jeu(grille):
    affichage(grille)
    if len(grille)!=3:
        print("Cette grille n'est pas valide")
    if grille[0][0]==grille[0][1]==grille[0][2]:
        return("gagné, joueur ",grille[0][0])
    elif grille[1][0]==grille1[1][1]==grille[1][2]:
        return("gagné, joueur ",grille[1][1])
    elif grille[2][0]==grille[2][1]==grille[2][2]:
        return("gagné, joueur ",grille[2][1])
    elif grille[0][0]==grille[1][0]==grille[2][0]:
        return("gagné, joueur ",grille1[1][0])
    elif grille[0][1]==grille[1][1]==grille[2][1]:
        return("gagné, joueur ",grille1[1][1])
    elif grille[0][2]==grille[1][2]==grille[2][2]:
        return("gagné",grille[0][2])
    elif grille[0][0]==grille[1][1]==grille[2][2]:
        return("gagné",grille1[0][0])
    elif grille[0][2]==grille[1][1]==grille[2][0]:
        return("gagné",grille[0][2])
    else:
        return("personne n'a gagné")


print(jeu(grille1))

