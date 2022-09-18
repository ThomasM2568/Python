# Créé par maxence.desmonteix, le 21/09/2020 en Python 3.7
L=[i for i in range (10000000)]
def recherche_dichotomique(L,N,index,comparisons) :
    index=0
    if len(L)>=1 :
        comparisons+=1
        print(comparisons)
        L1=L[0:int(len(L)/2)]
        L2=L[int(len(L)/2):]
        if N>L2[0]:
            index+=int(len(L)/2)
            return(recherche_dichotomique(L2,N,index,comparisons))
        elif N==L2[0]:
            return(index+int(len(L)/2))
        else :
            return(recherche_dichotomique(L1,N,index,comparisons))
    else :
        return(-1)
element=int(input("Saisissez un nombre entier entre 0 et 10000000"))
indice=0
comparaisons=0
print(recherche_dichotomique(L,element,indice,comparaisons))
