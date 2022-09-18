def pretraitement(motif):
    d=[]
    d2=[]
    dictionnaire={}
    for i in motif:
        d.append(i)
    print(d)
    for k in range(len(d)-1):
        valeur=(int(len(d))-int(k))-1
        d2.append(valeur)
    for a in range(1,2):
        d2.append(len(motif))
    print(d2)
    d.reverse()
    d2.reverse()
    for j in range(len(d)):
        cle=d[j]
        value=d2[j]
        if cle not in dictionnaire:
            dictionnaire[cle]=value
        else:
            print("valeur "+str(cle)+" déjà présente, remplacement par la valeur précédente")

motif="diamant"
chaine="l'amant aimant donnant un diamant"



#------------------------------------------------

def recherche(motif,chaine):
    """
    pretraitement(motif)
    """
    mot=chaine[:len(motif)]
    N=0
    e=0
    if mot==motif:
        return 0
    else:
        for e in range(0,len(motif))[::-1]:
            print(e,mot[e],motif[e])
            if mot[e]==motif[e]:
                N+=1
            else:
                x=e
                print("l'element "+str(x)+" ne correspond pas")
                return(N)

            e-=1
    decalage=-8
    if decalage<0:
        decalage=1
        mot=chaine[decalage,:len(motif)+decalage]
        print(mot)


print(recherche(motif,chaine))
