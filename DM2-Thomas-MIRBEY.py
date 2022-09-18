def Longueur(n) :
    if ( n >= 2) :
        total=1
        for n in range(2,n) :
            #print(n)
            total=total+1/n

        return ( 7 + 3.5 * total)
    else :
        print ("Erreur n >= 2")




def Seuil(M) :
    n = 2
    trouve = False

    while trouve == False :
        L = Longueur(n)
        #print (n, L, M)
        if L > M:
            trouve = True
            #print ("trouve")
            return (n)
        n=n+1

def Seuil2(M) :
    n = 2
    while Longueur(n) < M :
        n+=1
    return(n)

for i in range (2,32+1):
    print(i, Longueur(i))

print(32,Longueur(32))
print(1000,Longueur(1000))

print(Seuil(11))
print(Seuil2(21))