liste=[136,543,50,606,97,606,167,543,558,543,50,608,606,338,50,543,606,167,50,136,543,50,137,136,262,606,50,645,287,608,167]
liste2=[]
liste3=[696,647,223,317,618,317,704,647,545,647,223,517,317,39,223,647,317,704,223,696,647,223,656,696,206,317,223,668,274,517,704]
liste4=[]
for i in liste:
    a=i
    r=a**11%689
    print(chr(r))
    liste2.append(chr(r))
print(liste2)

def RSAdecryptage(X,Y,Z):
    """X=valeur,Y=valeurcode,Z=liste valeurs à traduire"""
    for i in Z:
        a=i
        r=a**X%Y
        print(chr(r))
        liste4.append(chr(r))
    return(liste4)


Y=793

print(RSAdecryptage(17,Y,liste3))
