x=int(input("nombre"))

L=[]
def f(X):
    if X>0:
        for Y in range(1,X):
            if X%Y==0:
                L.append(Y)
    if len(L)==2 :
        return("le nombre x est un nombre premier car il possède que deux diviseurs :",L)
    else :
        return("le nombre x n'est pas un nombre premier car il ne possède pas uniquement que deux diviseurs mais :",L)









print(f(x))
