class Noeud :
    def __init__(self,nom):
        self.valeur=nom
        self.gauche= None
        self.droite= None

def ajouter(noeud,nom):
        if noeud==None:
            return(Noeud(nom))
        if noeud.valeur==nom:
            return(noeud)
        if nom<noeud.valeur:
            noeud.gauche=ajouter(noeud.gauche, nom)
            return(noeud)
        if nom>noeud.valeur:
            noeud.droite=ajouter(noeud.droite, nom)
            return(noeud)

def verif_presence(noeud,nom,compteur):
    if noeud==None:
        compteur+=1
        print(compteur)
        return False
    if nom==noeud.valeur:
        compteur+=1
        print(compteur)
        return True
    elif nom > noeud.valeur:
        return verif_presence(noeud.droite,nom,compteur+1)
    else:
        return verif_presence(noeud.gauche,nom,compteur+1)



def nombre_absents(noeud):
    global total
    if noeud==None:
        return -1
    if noeud.droite.valeur!=None:
        total+=1
        return(nombre_absents(noeud.droite))
    if noeud.gauche.valeur!=None:
        total+=1
        return(nombre_absents(noeud.droite))
    return(total)





L=["houdin",'bassot','sadoul','feret','paquin',"bardin","rapace","salande","lecerf","gardet"]
ABR=Noeud(L[1])
for i in range(1,len(L)):
    print(L[i])
    ajouter(ABR,L[i])

compteur=0
print(verif_presence(ABR,"nomatester",compteur)) #Si l'élève est présent, la fonction retourne True, sinon False"""
total=0
print(nombre_absents(ABR))

#e) Cela permet de gagner du temps puisque l'arbre est organisé en fonction de l'ordre alphabetique, valeurgauche<racine<valeurdroite
#Si on sait que le nom est après la racine, on part d'un côté, sinon de l'autre.