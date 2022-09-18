def pretraitement(motif):
    global dictionnaire
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
            print(dictionnaire)
        else:
            print("valeur "+str(cle)+" déjà présente, remplacement par la valeur précédente")
    return(dictionnaire)

motif="diamant"
chaine="l'amant aimant donnant un diamant"



#------------------------------------------------

def recherche(motif,chaine):
    global dictionnaire
    dico=pretraitement(motif)

    mot=chaine[:len(motif)]
    N=0
    e=0
    decalage=0
    if mot==motif:
        return 0
    else:
        while mot!=motif:
            x=0
            for e in range(0,len(motif))[::-1]:
                if mot[e]==motif[e]:
                    N+=1
                else:
                    if x==0:
                        x=e
                        if chaine[e] not in dico:
                            decalage=len(mot)-N
                            mot=''
                            for v in range(len(motif)):
                                mot=mot+chaine[v+decalage]
                            print(mot)
                        else:
                            decalage=dictionnaire.get(motif[e])
                            decalage=decalage-N










"""print("l'element "+str(x)+" est le première lettre à ne pas correspondre"+" ("+str(chaine[x])+")")
            y=dictionnaire.get(motif[x])
            print(y)
            print(len(motif))
            decalage=len(motif)-N
            print(decalage)"""







print(recherche(motif,chaine))
