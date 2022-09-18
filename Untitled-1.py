from random import *
L=[randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9)]
n=len(L)
compteur=0
for i in range (1,n):
    element=L[i]
    decalage=0
    if i+decalage!=0 :
        compteur+=1

    while not ((L[i+decalage-1]<=element) or (i+decalage==0)):
        decalage-=1
        L[i+decalage+1]=L[i+decalage]
        L[i+decalage]=element
        print (L,element,decalage)
        if i+decalage!=0 :
            compteur+=1

print(L,"compteur =",compteur)