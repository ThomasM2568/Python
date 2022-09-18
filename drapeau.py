'''
Yohan Fourel
Thomas Mirbey

Drapeau Americain (bannière étoilée)

Il se compose de treize bandes horizontales rouges et blanches d’égale largeur,
disposées alternativement et d’un canton supérieur (côté mât) de couleur bleue parsemé de cinquante petites étoiles
blanches à cinq pointes arrangées selon neuf rangées horizontales.
'''

from turtle import *

# fonction rectangle : dessine un rectangle plein
# parametres :
# x,y - position
# hauteur - hauteur du rectangle
# longueur - longueur du rectangle
# couleur - couleur du rectangle
def rectangle(x, y, hauteur, longueur, couleur):
    goto(x,y)
    pendown()
    color(couleur)
    begin_fill()
    for i in range(0,2):
        forward(longueur)
        right(90)
        forward(hauteur)
        right(90)
    end_fill()
    penup()

# fonction bandes_drapeau : dessine nb bandes (rectangles) sur le fond du drapeau
# parametres :
# nb - nombre de bandes
# x,y - position du drapeau
# espacement - espacement entre les bandes
# couleur - couleur des bandes
def bandes_drapeau(nb,x,y,espacement,longueur,couleur):
    # on decale la 1er bande
    y=y-espacement
    for ligne in range(nb):
        rectangle(x, y, espacement, longueur, couleur)
        # on se déplace dans le coin inférieur gauche du rectangle
        y=y-espacement
        # on saute une bande
        y=y-espacement

# fonction etoile : dessine une etoile avec 5 pointes
# parametres :
# x,y - position étoile
# couleur - couleur etoile
# longueur - longueur etoile
def etoile(x,y,couleur,longueur) :
    goto(x,y)
    pendown()
    begin_fill()
    color(couleur)
    for cote in range(0,5) :
        # une branche
        forward(longueur)
        # 360°/5 = 72° * 2 = 144°
        right(144)
        forward(longueur)
        # 360°/5 = 72° * 2 = 144°
        right(144)
    end_fill()
    penup()

# fonction lignes6etoiles : dessine 5 lignes de 6 etoiles
# parametres :
# tailleetoile - taille de l'etoile
# espacement - espacement entre etoiles
# couleur - couleur etoile
# x,y - coordonnées drapeau
def ligne6etoiles(tailleetoile,espacement,couleur,x,y):
    espacemententreetoiles = 30
    espacemententreleslignes = espacement + 6
    y = y - espacement
    # x1 debut de chaque ligne
    x1 = x + espacement
    # 5 lignes
    for ligne in range(0,5) :
        x = x1
        # de 6 etoiltes
        for e in range (0,6) :
            etoile(x, y, couleur, 10)
            x = x + espacemententreetoiles
        y = y - espacemententreleslignes

# fonction lignes6etoiles : dessine 4 lignes de 5 etoiles
# parametres :
# tailleetoile - taille de l'etoile
# espacement - espacement entre etoiles
# couleur - couleur etoile
# x,y - coordonnées drapeau
def ligne5etoiles(tailleetoile,espacement,couleur,x,y):
    espacemententreetoiles = 30
    espacemententreleslignes = espacement + 6
    y = y - espacement*1.7
    # x1 debut de chaque ligne
    x1 = x + espacement*1.7
    # 4 lignes
    for ligne in range(0,4) :
        x = x1
        # de 5 etoiles
        for e in range (0,5) :
            etoile(x, y, couleur, 10)
            x = x + espacemententreetoiles
        y = y - espacemententreleslignes

# fonction genérique nlignemetoiles remplaçant ligne5etoiles et ligne6etoiles
# dessine n lignes de m étoiles
# parametres :
# tailleetoile - taille de l'etoile
# espacement - espacement entre etoile
# couleur - couleur etoile
# x,y - coordonnées drapeau
# n - nombre de lignes
# m - nombre etoiles
# coef - permettant décalage des lignes d'etoiles
#  1 = pas de décalage, commence en x,y
#  1,x = décalage de 1,x

def nlignemetoiles(tailleetoile,espacement,couleur,x,y,n,m,coef):
    espacemententreetoiles = 30
    espacemententreleslignes = espacement + 6
    y = y - espacement*coef
    # x1 debut de chaque ligne
    x1 = x + espacement*coef
    # n lignes
    for ligne in range(0,n) :
        x = x1
        # de m etoiles
        for e in range (0,m) :
            etoile(x, y, couleur, 10)
            x = x + espacemententreetoiles
        y = y - espacemententreleslignes

# programme principal

# fond d'ecran noir
bgcolor("black")
# titre
title("Drapeau USA")
# vitesse rapide
speed(0)


# position drapeau x,y
x=-200
y=200

# taille du drapeau : rectangle longueur 475 hauteur 250
longueur=475
hauteur=250

# largeur d'une bande ou espacement entre bande rouge et bande blanche
# au total 13 bandes = hauteur du drapeau / 13
espacement=hauteur/13
#taille des etoiles
tailleetoile=10

# etape 1 : on fait un rectangle rouge de la taille du drapeau
rectangle(x,y,hauteur,longueur,'red')

# etape 2 : on place 6 bandes blanches (6 rectangles blancs)
bandes_drapeau(6,x,y,espacement,longueur,'white')
# on a maintenant 7 bandes rouges et 6 bandes blanches

# etape 3 : on place le canton superieur bleu (rectangle bleu)
rectangle(x, y, espacement*7, longueur*0.42, 'navy')

# etape 4 : On place les 50 étoiles dans le canton bleu
# etape 4.1 : 5 lignes de 6 etoiles = 30
#ligne6etoiles(tailleetoile,espacement,'white',x,y)
nlignemetoiles(tailleetoile,espacement,'white',x,y,5,6,1)

# etape 4.2 : 4 lignes de 5 etoiles = 20
#ligne5etoiles(tailleetoile,espacement,'white',x,y)
nlignemetoiles(tailleetoile,espacement,'white',x,y,4,5,1.7)
# au total 50 etoiles disposées en 9 rangées pour 50 états

hideturtle()
exitonclick()
