#Importation du module random
from random import *

#Les fonctions utiles pour les files
def Creer_file_vide(m):
    global max
    max=m
    F=[]
    return F

def Est_vide(F):
    if len(F)==0:
        return True
    return False

def Est_pleine(F):
    global max
    if len(F)>=max:
        return True
    return False

def Enfiler(F, d):
    if not Est_pleine(F):
        F.insert(0, d)
        return F
    print("Votre file est pleine")
    return F

def Defiler(F):
    if not Est_vide(F):
        d=F.pop()
        return d, F
    print("Impossible de défiler une file vide")
    return None, F

#Votre programme
cartes=[1,2,3,4,5,6,7,8]

def melange(listecartes):
    milieu=int(len(listecartes)/2)
    l1=listecartes[:milieu]
    l2=listecartes[milieu:]
    liste=Creer_file_vide(len(listecartes))
    while len(liste)!=len(listecartes):
        nombre=randint(0,milieu-1)
        print(nombre)
        a=l1[nombre]
        b=l2[nombre]
        if a not in liste:
            liste.append(a)
        if b not in liste:
            liste.append(b)
    return(liste)

print(melange([1,2,3,4,5,6,7,8]))

F1=melange(cartes)
F2=melange(cartes)
print(F1,F2)

def partie(F1,F2):
        if len(F1)==0 and len(F2)==0:
            return "Egalité"
        elif len(F1)==0:
            return "Joueur2 a gagné"
        elif len(F2)==0:
            return "Joueur1 a gagné"
        else:
            if F1[0]>F2[0]:
                print(F1[0])
                carte=F2[0]
                Enfiler(F1,carte)
                Defiler(F2)
                print(partie(F1,F2))
            elif F1[0]<F2[0]:
                carte=F1[0]
                Enfiler(F2,carte)
                Defiler(F1)
                print(partie(F1,F2))
            else:
                for i in range(4):
                    if len(F1)==2:
                        valeur=randint(0,len(F1)-1)
                        F2.append(valeur)


                    else:
                        valeur=randint(0,len(F1)-1)
                        F1.append(valeur)
                    print(partie(F1,F2))



print(partie(F1,F2))






