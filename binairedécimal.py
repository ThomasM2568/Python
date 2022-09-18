def deci_bin(q):
    result = ""
    while q != 0 :
        r=q%2
        q=q//2
        #print ( "q {q} r {r}".format(q=q,r=r))
        result=str(r)+result
    return(result)



def bin_deci(q):

    L=len(q)-1
    total=0

    for c in q:
        total=int(c)*(2**L)+total
        L=L-1

    return(total)

nb=42
convbin=deci_bin(42)
print("conversion de {nombre} en binaire {resultat}".format(nombre=nb,resultat=convbin))
print("conversion de {nombre} en base10 {resultat}".format(nombre=convbin,resultat=bin_deci(convbin)))




