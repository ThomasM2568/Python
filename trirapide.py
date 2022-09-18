import sys
sys.setrecursionlimit(10000)

def tri_rapide(liste):
    c=0
    if len(liste)==0:
        print("La liste est déjà vide")
        return(liste)
    else:
        e=liste[0]
        L1=[]
        L2=[]
        for valeurs in liste[1:]:
            c+=1
            if valeurs>=e:
                L2.append(valeurs)
            else:
                L1.append(valeurs)
    L1=tri_rapide(L1)
    L2=tri_rapide(L2)
    print("c",c)
    return L1+[e]+L2

from random import *
liste2=[]
for i in range(1000):
    value=i
    if value not in liste2:
        liste2.append(value)

print(liste2)

print(tri_rapide(liste2))

