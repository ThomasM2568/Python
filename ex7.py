tab=[65,156,5,43,64,451534,86,48,5313,86,85]
maxi=tab[0]
pos=0
compteur=0
def recherche(tab,maxi,pos,compteur):
    while compteur+1<len(tab):

        if tab[pos+1]>maxi:
            compteur+=1
            maxi=tab[pos+1]
            pos=pos+1
            recherche(tab,maxi,pos,compteur)

        else:
            compteur+=1
            pos+=1

            recherche(tab,maxi,pos,compteur)
    return maxi


print(recherche(tab,maxi,pos,compteur))
