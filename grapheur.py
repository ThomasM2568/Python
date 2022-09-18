from turtle import *


nombre=int(input("Entrez le nombre de points à tracer"))

def fonction_graphique(nombre):

    goto(0,0)
    for i in range(nombre):
        x=float(input("Entrez la valeur de x"))
        y=float(input("Entrez la valeur de y"))
        goto(x,y)

def axes(limitex,limitey):
    penup()
    goto(0,0)
    pendown()
    goto(0,limitey)
    pendown()
    goto(limitex,0)

limitex=int(input("Entrez la limite de X"))
limitey=int(input('Entrez la limite de Y'))

print(axes(limitex,limitey))

print(fonction_graphique(nombre))