joueur=0
liste1=[]
liste2=[]
def init_joueurs(nombre_joueurs_nouveau_jeu):
    for i in range(nombre_joueurs_nouveau_jeu):
        noms_joueurs=str(input("Entrez un nom pour le joueur"))
        liste1.append(noms_joueurs)
    return(liste1)

def init_scores(nombre_joueurs_score):
    for total in range(nombre_joueurs_score):
        liste2.append(0)
    return(liste2)

def ajoute_points(numero_joueur,nombre_de_points):
    liste2[numero_joueur]+=nombre_de_points
    return liste2

def affiche_scores():
    return(liste1)
    return(liste2)

def gagnant():
    m=liste2[0]
    p=0
    for n in range(1,len(liste2)):
        if liste2[n]>m:
            m=liste2[n]
            p=n
    return(p)


nombre=int(input("Entrez un nombre de joueurs"))

print(init_joueurs(nombre))

print(init_scores(nombre))

p=int(input("Entrez un nombre de points"))

while p>=0:
    ajoute_points(joueur,p)
    joueur+=1
    if joueur==len(liste1):
        joueur=0
    affiche_scores()
    p=int(input("Entrez un nombre de points"))
print(liste1[gagnant()],' a gagné')
