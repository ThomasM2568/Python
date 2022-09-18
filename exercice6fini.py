from thomasm import tri_insertion as tri
l=[6,9,5,7,63,2,45,7,8,25]
tri(l)
e1=int(len(l)/2)
l1=l[:e1]
l2=l[e1:]
w=0
n=int(input('Entrez la valeur à chercher'))

def recherche(n,l):
    global w
    while w<(len(l)/2):
        if n>=l2[0]:
            if n==l2[w]:
                texte="Element "+str(n)+ " trouvé en position " + str(l1[w]-1)+" de L2 :"+str(l2)
                return texte
            else:
                w+=1
                recherche(n,l2)
        elif n<=l2[0]:
            if n==l1[w]:
                texte="Element "+str(n)+ " trouvé en position " + str(l1[w]-1)+" de L1 :"+str(l1)
                return texte
            else:
                w+=1
                recherche(n,l1)
        else:
            return -1
    return -1

print(recherche(n,l))
