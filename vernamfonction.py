def deci_to_bin(q):
    """En 8bits"""
    result = ""
    while q != 0 :
        r=q%2
        q=q//2
        #print ( "q {q} r {r}".format(q=q,r=r))
        result=str(r)+result
        nvresult=""

    return(result)

def decoupage(mot):
    liste=[]
    for i in str(mot):
        liste.append(i)
    return(liste)

def valeurs_decoupage(liste):
    liste2=[]
    for i in liste:
        liste2.append(ord(i))
    return(liste2)

def conversion_mot_binaire(motbinaire):
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

def inverse_ou_exclusif(l1cle,l2mot):
    #Utilisation de listes équilibrées en taille
    l3binaire=[]
    for i in range(len(l1cle)):
        valeur=int(l1cle[i])-int(l2mot[i])
        if valeur==-1:
            l3binaire.append(1)
        else:
            l3binaire.append(valeur)
    return(l3binaire)


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


def Vernam(mot,cle):
    l3=[]
    mot=mot.upper()
    l1=decoupage(mot)
    l2=valeurs_decoupage(l1)
    for i in l2:
        l3+=conversion_mot_binaire(i)
    nvmot=[]
    listecle3=decoupage(cle)
    print(l3)
    for u in l3:
        if len(l3)!=0:
            if len(l3)>len(listecle3):
                for a in listecle3:
                    if len(l3)!=len(listecle3):
                        listecle3.append(a)
    print("l3 = ",l3)
    print("Listecle3 = ",listecle3)
    liste4=ou_exclusif(l3,listecle3)
    return("Voici le mot codé ",liste4)
"""
mot=str(input("Entrez un mot à coder"))
"""
cle=11010101
"""
print(Vernam(mot,cle))
"""

def inverseVernam(motadecoder,cle):
    l3=[]
    motadecoder=motadecoder.upper()
    l1=decoupage(motadecoder)
    l2=valeurs_decoupage(l1)
    for i in l2:
        l3+=conversion_mot_binaire(i)
    nvmotadecoder=[]
    listecle3=decoupage(cle)
    print(l3)
    for u in l3:
        if len(l3)!=0:
            if len(l3)>len(listecle3):
                for a in listecle3:
                    if len(l3)!=len(listecle3):
                        listecle3.append(a)
    """print("l3 = ",l3)
    print("Listecle3 = ",listecle3)"""
    liste4=ou_exclusif(l3,listecle3)
    return("Voici le motadecoder codé ",liste4)

print(inverseVernam("100111111","11010101"))