# 1. Importer le module random avec l’instruction from random import*. 
from random import *

#2. De quelle manière est définie la variable a ci-dessous ? 
a=random()
print (a)
# random donne une valeur aléatoire entre 0 et 1

# fonction y=x²
def f(x):
    return(x**2)

# initialisation des valeurs pour compter les points au dessus et au dessous de la courbe
dessus=0
dessous=0

# 5. En utilisant une boucle, construire 1000 points placés aléatoirement dans le carré et compter le nombre de points appartenant au domaine
for i in range(0,1000):
    # 3. Créer deux variables xA et yA de telle façon qu’elles définissent les coordonnées d’un point A placé aléatoirement dans le carré défini dans l'instruction
    xA=random()
    yA=random()
    # y=f(xA)
    y=f(xA)
    # 4. instruction doit-on saisir pour vérifier que le point A est situé dans le domaine hachuré
    if ( yA < y):
        dessous=dessous+1
    else:
        dessus=dessus+1
        
    print("Point {i} xA={xA} yA={yA} f(xA)={y} nb dessus {dessus} nb dessous {dessous}".format(i=i+1,xA=xA,yA=yA,y=y,dessus=dessus,dessous=dessous))


# 6. En déduire alors la proportion de points situés dans ce domaine par rapport à l’ensemble des points, et conclure quant au problème posé. 
print ("valeure approchee={v}".format(v=dessous/1000))


