from binarytree import *
n1=Noeud(6)
n2=Noeud(3)
n3=Noeud(9)
n4=Noeud(7)
n5=Noeud(12)
n1.gauche=n2
n1.droite=n3
n3.gauche=n4
n3.droite=n5


"""print(type(n1))
print(recherche(n1,4))
print(ajouter_liste(n1,9))"""





compteur=0
print(recherche2(n1,1567,compteur))


