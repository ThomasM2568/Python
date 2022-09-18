def est_premier(n):
    liste_diviseurs=[1]
    for i in range(2,n+1):
        if n%i==0: liste_diviseurs.append(i)
        if len(liste_diviseurs)>2: return False
    return True

def diviseurs_premiers(n):
    liste_diviseurs_premiers=[]
    for i in range(2,n+1):
        if n%i==0 and est_premier(i):
            liste_diviseurs_premiers.append(i)
    return liste_diviseurs_premiers

def recherche_pq(n):
    L=diviseurs_premiers(n)
    for nombre1 in L:
        for nombre2 in L:
            if nombre1*nombre2==n :
                return (nombre1,nombre2)
    return -1

def recherche_d(c,p,q):
    d=1
    while (c*d)%((p-1)*(q-1))!=1:
        d+=1
    return d
