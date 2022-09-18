#partie écrite
def maximum(noeud):
    maxi=0
    while noeud.droite.valeur!=None:
        noeud=noeud.droite
        maxi=noeud.droite
    return maxi


liste=()
def parcours_infixe(noeud,liste):
    if noeud.gauche.valeur!=None and noeud.valeur>noeud.gauche.valeur:
        return(parcours_infixe(noeud_gauche))
    liste.append(noeud.valeur)
    if noeud.droite.valeur!=None:
        return(parcours_infixe(noeud.droite))


result=0
def somme(noeud,result):
    if noeud.valeur!=None:
        result+=noeud.valeur
    if noeud.droite!=None:
        return(somme(noeud.droite,result))
    if noeud.gauche!=None:
        return(somme(noeud.gauche,result))
    if noeud.valeur==None:
        return(result)

#partie code

ABR=None

for i in l:
    ABR=ajouter(ABR,i)

def nombre_absents(arbre):
    return(1+nombre_absents(arbre.gauche)+nombre_absents(arbre.droite))

