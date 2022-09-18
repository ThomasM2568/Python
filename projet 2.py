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

def deci_héxa(q):
    result = ""
    while q != 0 :
        r=q%16
        q=q//16
        result=str(r)+result
    if q==0:
        result='0'+result
    elif r==10:
        result='a'+result
    elif r==11:
        result='b'+result
    elif r==12:
        result='c'+result
    elif r==13:
        result='d'+result
    elif r==14:
        result='e'+result
    elif r==15:
        result='f'+result
    elif r==16:
        result='10'+result


    return(result)

def hexa_deci(q):

    L=len(q)-1
    total=0

    for c in q:
        total=int(c)*(16**L)+total
        L=L-1



valeur=int(input("Entrez une valeur"))
base=int(input("Entrez la base correspondante à cette valeur"))
convertir=int(input("Entrez la base dans laquelle vous souhaitez convertir la valeur"))



def conversion(valeur,base,convertir):
    if base==2 and convertir==10:
        print(bin_deci(valeur))
    elif base==10 and convertir==2:
        print(deci_bin(valeur))
    elif base==16 and convertir==10:
        print(hexa_deci(valeur))
    elif base==10 and convertir==16:
        print(deci_héxa(valeur))

