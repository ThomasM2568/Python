"""r=[1,2,5,10,20,50,100,200]
l=[]

def rendu(montant,r):
    reste=montant
    r.reverse()
    somme=0
    while reste>=min(r):
        for i in range(len(r)):

            if reste>=r[i]:
                reste=reste-r[i]
                valeur=r[i]
                l.append(valeur)

    return(l)

montant=int(input("Entrez le montant à remettre"))
print(rendu(montant,r))
"""
P=[1,2,5,10,20,50,100,200]
#P=[1,3,6,12,24,30]

S=int(input("Entrer la somme à rendre"))
L=[]

i=len(P)-1

while S>=P[0] :
    if S>=P[i] :
        L.append(P[i])
        S-=P[i]
    else :
        i-=1

if S==0 :
    print("Rendu effectué :",L)
else :
    print("Rendu incomplet :",L)