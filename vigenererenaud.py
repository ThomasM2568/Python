# Créé par renaud.joffrin, le 28/01/2021 en Python 3.7
alph={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
mot=input("Entrez le message")
clé=input("Entrez la clé")
code=input("Entrez le code")
mot=mot.lower()
clé=clé.lower()
code=code.lower()


def création(mot,clé,code):
    L1=[]
    L2=[]
    L3=[]
    for i in mot:
        L1.append(alph.get(i))
    for j in clé:
        L2.append(alph.get(j))
    for g in code:
        L3.append(alph.get(g))
    return (L1,L2,L3)

def vigenere (mot,clé,code):
    c=0
    nmot=""
    L1, L2, L3=création(mot,clé,code)
    for k in range (len(L1)):
        D=L1[k]+L2[c]
        if D>26:
            D-=26
        for f in alph:
            val=alph.get(f)
            if D==val:
                nmot=nmot+f
        if c>=len(L2)-1:
            c=0
        else:
            c+=1
    return nmot

print(vigenere(mot,clé,code))


def vigenerereverse (mot,clé,code):
    c=0
    nmot=""
    L1, L2, L3=création(mot,clé,code)
    for k in range (len(L3)):
        D=L3[k]-L2[c]
        if D<0:
            D=26+D
        for f in alph:
            val=alph.get(f)
            if D==val:
                nmot=nmot+f
        if c>=len(L2)-1:
            c=0
        else:
            c+=1
    return nmot

"print(vigenerereverse(mot,clé,code))"