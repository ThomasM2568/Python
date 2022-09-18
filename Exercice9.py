acide="AGWPSGGASAGLAILWGASAIMPGALW"
alp="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
h={"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0}
def Compteur(liste):
    for i in liste:
        for j in alp:
            if j==i:
                h[i]+=1
    for a in alp:
        if h[a]==0:
            h.pop(a)
    return(h)
print(Compteur(acide))
