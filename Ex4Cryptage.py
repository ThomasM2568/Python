def traitement(mot):
    l=[]
    for i in mot:
        l.append(i)
    return(l)

def listetomot(liste):
    mot=""
    for i in liste:
        mot+=i
    return(mot)

def ou_exclusif(l1binaire,l2binaire):
    #Utilisation de listes équilibrées en taille
    l3binaire=[]
    for i in range(len(l1binaire)):
        valeur=int(l1binaire[i])+int(l2binaire[i])
        if valeur==2:
            l3binaire.append(0)
        else:
            l3binaire.append(valeur)
    return(l3binaire)

def convert(p):
    w=traitement(p)
    return(w)


def shift(p,n,compteur,w):
    """p est un mot
    n est un entier"""
    if compteur==0:
        w=convert(p)
        longueur=len(w)
    if compteur<n:
        deleted=w.pop(-1)
        w.insert(0,deleted)
        compteur+=1
        print(w)
        return(shift(p,n,compteur,w))
    nv=listetomot(w)
    return(nv)

def bin_to_deci(q):

    L=len(q)-1
    total=0
    for c in q:
        total=int(c)*(2**L)+total
        L=L-1

    return(total)

def deci_to_bin(q):
    #en 8 bits
    result = ""
    while q != 0 :
        r=q%2
        q=q//2
        #print ( "q {q} r {r}".format(q=q,r=r))
        result=str(r)+result
    if len(result)<8:
        mot=""
        for i in range(8-len(result)):
            mot+="0"
        mot+=result
    return(mot)

def somme(p1,p2):
    #En 128bits
    a1=bin_to_deci(str(p1))
    a2=bin_to_deci(str(p2))
    a3=a1+a2
    a4=deci_to_bin(a3)
    if len(str(a4))<128:
        dif=128-len(a4)
        value=''
        for i in range(dif):
            value+=str(0)
        valeur=str(value)+str(a4)
        return(valeur,len(valeur))

compteur=0
li=[]
print(shift("101110",2,compteur,li))
print(ou_exclusif('1010','0110'))

def conversion_mot_binaire(motbinaire):
    #ord de mot binaire conseillé mais marche quand même sinon
    if type(motbinaire)!=int:
        motbinaire=ord(motbinaire)
    liste=[]
    nvresult=[]
    for i in str(deci_to_bin(motbinaire)):
        liste.append(i)
    if len(liste)<8:
        nbzero=8-len(liste)
        for i in range(nbzero):
            nvresult.append(0)
        for y in liste:
            nvresult.append(y)
    return(nvresult)

def remplissage(liste):
    #128 bits
    for i in range(128):
        liste.append(1)
    return(liste)


def hachage(donnee):
    listetermes=""
    for i in donnee:
        listetermes+=deci_to_bin(ord(i))
    print(listetermes)
    div=len(listetermes)/512



"""
    #Définition des listes vides puis remplies de 128 fois 1
    paquet1=[]
    paquet2=[]
    paquet3=[]
    paquet4=[]
    paquet1=remplissage(paquet1)
    paquet2=remplissage(paquet2)
    paquet3=remplissage(paquet3)
    paquet4=remplissage(paquet4)"""







