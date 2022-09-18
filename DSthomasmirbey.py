from random import randint
#1)
message="LATTAQUEESTPOURDEMAIN"

clef="FUSREBJFYDZMPHYDALDIU"

def lettre_chiffre(texte):
    textechiffre=[]
    for i in range(len(texte)):
        valeur=ord(texte[i])-64
        if valeur>26:
            valeur-=26

            textechiffre.append(valeur)
        else:
            textechiffre.append(valeur)
    return(textechiffre)

def somme(texte1,texte2):
    newtexte=[]
    for i in range(len(texte1)):
        v1=texte1[i]
        v2=texte2[i]
        v3=v1+v2
        if v3>26:
            v3-=26
        newtexte.append(v3)
    return(newtexte)

def conversion(texte1):
    texte=""
    for i in range(len(texte1)):
        v1=texte1[i]+64
        v1bis=chr(v1)
        texte+=str(v1bis)
    return(texte)

def decalage(message,clef):
    a,b=lettre_chiffre(message),lettre_chiffre(clef)
    c=somme(a,b)
    print(c)
    print(conversion(c), "Voici le resultat du chiffrage de ", message, " avec la clef ",clef)
    return('Done')

print(decalage(message,clef))
#2)

def generationcle(longueur):
    valeur=""
    for i in range(longueur):
        v=(randint(1,26))+64
        valeur+=chr(v)
    print(len(valeur), "= longueur de la clef suivante")
    return(valeur)

print(generationcle(100))