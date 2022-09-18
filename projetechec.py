#Créé par Renaud, Nathan et Thomas
from tkinter import *


def lire_grille(texte):
    #Taille de 8*8
    #Beige - > Brun etc
    #roi blanc sur case noire et inverse
    #Beige = 00
    #Brun = 01
    #Pion1blanccn = 02
    #Pion1blanccb = 03
    #Cavalierblanccn = 04
    #
    grille = open('grille.txt', 'r')
    return(grille)

#Dico pour pions, avec position = liste

def deppos(direct):
    global nbcle
    if direct=="bas":
        if lines[posy+1][posx]=='0' or int(lines[posy+1][posx])>= 3:
            return('True')
        if lines[posy+1][posx]=='2' and nbcle>0:
            nbcle-=1
            return('True')
    if direct=="haut":
        if lines[posy-1][posx]=='0' or int(lines[posy-1][posx])>= 3:
            return('True')
        if lines[posy-1][posx]=='2'and nbcle>0:
            nbcle-=1
            return('True')
    if direct=="droite":
        if lines[posy][posx+1]=='0' or int(lines[posy][posx+1])>= 3:
            return('True')
        if lines[posy][posx+1]=='2'and nbcle>0:
            nbcle-=1
            return('True')
    if direct=="gauche":
        if lines[posy][posx-1]=='0' or int(lines[posy][posx-1])>= 3:
            return('True')
        if lines[posy][posx-1]=='2'and nbcle>0:
            nbcle-=1
            return('True')


def droite(event):
    global posx,posy,fenetre,player,deplacements
    if deppos("droite")=='True':
        posx+=1
        canvas.delete(player)
        case()
        deplacements+=1
def gauche(event):
    global posx,posy,fenetre,player,deplacements
    if deppos("gauche")=='True':
        posx-=1
        canvas.delete(player)
        case()
        deplacements+=1
def haut(event):
    global posx,posy,fenetre,player,deplacements
    if deppos("haut")=='True':
        posy-=1
        canvas.delete(player)
        case()
        deplacements+=1
def bas(event):
    global posx,posy,fenetre,player,deplacements
    if deppos("bas")=='True':
        posy+=1
        canvas.delete(player)
        case()
        deplacements+=1
