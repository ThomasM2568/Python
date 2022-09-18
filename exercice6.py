def recherche(n,l):
    e1=int(len(l)/2)
    l1=l[:e1]
    l2=l[e1:]
    if l2[0]>n:
        for i in l1:
            if i==n:
                print(l1)
                texte="Element trouvé dans la première partie de la liste en position "+str((l1.index(i)))
                return texte
    else:
        for z in l2:
            if z==n:
                print(l2)
                texte1="Element trouvé dans la deuxième partie de la liste en position "+str((l2.index(z)))
                return texte1
    if not n in l:
        return -1

liste=[1,2,3,4,5,6]
print(recherche(2,liste))

