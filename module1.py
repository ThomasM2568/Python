# Créé par renaud.joffrin, le 16/11/2020 en Python 3.7
# Créé par renaud.joffrin, le 16/11/2020 en Python 3.7
from random import*
c=0
a=0
class Noeud :
    def __init__(self,valeur_noeud):
        self.valeur=valeur_noeud
        self.gauche= None
        self.droite= None

def recherche(noeud,valeur_recherchee):
    global c
    if noeud==None:
        c=0
        return(False,c)
    if noeud.valeur==valeur_recherchee:
        c+=1
        return(True,c)
    else:
        if valeur_recherchee<noeud.valeur:
            c+=1
            return recherche(noeud.gauche,valeur_recherchee)
        c+=1
        return recherche(noeud.droite,valeur_recherchee)

def ajouter_liste(noeud,valeur_ajoutee):
        d=valeur_ajoutee
        if noeud==None:
            return(Noeud(valeur_ajoutee))
        if noeud.valeur==d:
            return(noeud)
        if int(d)<noeud.valeur:
            noeud.gauche=ajouter_liste(noeud.gauche, valeur_ajoutee)
            return(noeud)
        if int(d)>noeud.valeur:
            noeud.droite=ajouter_liste(noeud.droite, valeur_ajoutee)
            return(noeud)

arbre=Noeud(randint(1,100000))
def parcours_largeur(racine):
    file=[]
    total=[]
    if racine== None:
        return -1
    file.append(racine)
    while len(file)>0:
        d=file.pop(0)
        if d.gauche!=None:
            file.append(d.gauche)
        if d.droite!=None:
            file.append(d.droite)
        total.append(d.valeur)
    return total

for i in range (459):
    d=randint(1,100000)
    ajouter_liste(arbre,d)
parcours_largeur(arbre)

