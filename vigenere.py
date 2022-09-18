"""import string
letter_count = dict( (key, 0) for key in string.ascii_lowercase )
print(letter_count)"""

dico={'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11,
 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21,
't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
"""
motachanger=str(input("Entrez un mot"))
motachanger=motachanger.lower()
"""
cle=str(input("Entrez une clé"))
cle=cle.lower()
lettresm=[]
lettresc=[]

def traitement(cle,mot,l1,l2):
    for i in mot:
        l2.append(dico[i])
    for y in cle:
        l1.append(dico[y])
    return(l2,l1)
"""
print(traitement(cle,motachanger,lettresc,lettresm))
"""
def find_key(v):
    for k, val in dico.items():
        if v == val:
            return k
    return "Clé n'existe pas"

def vigenere(cle,motachanger,lettresc,lettresm):
    nvlettres=[]
    nvmot=""
    for u in lettresm:
        if len(lettresm)!=0:
            if len(lettresm)>len(lettresc):
                for a in lettresc:
                    if len(lettresm)!=len(lettresc):
                        lettresc.append(a)
    print(lettresc)
    for b in range(len(lettresm)):
        print('m ',lettresm[b])
        print('c ',lettresc[b])
        valeur=lettresc[b]+lettresm[b]
        if valeur>26:
            valeur-=26
            nvlettres.append(valeur)
        else:
            nvlettres.append(valeur)

    print(nvlettres)

    for o in nvlettres:
        nvmot+=str(find_key(o))
    return(nvmot)
"""
print(vigenere(cle,motachanger,lettresc,lettresm))
"""
list1=[]
list2=[]

motatrouver="FJUURTGDJGJFGMSWULYSWENBBQOXVRBSDDJNUGHAJPGX"
motatrouver=motatrouver.lower()
print(len(motatrouver))
print(traitement(motatrouver,cle,list1,list2))
print("aa",list1,list2)

def vigenereinverse(cle,motatrouver,list1,list2):
    nvlettres=[]
    nvmot=""
    for u in list1:
        if len(list1)!=0:
            if len(list1)>len(list2):
                for a in list2:
                    if len(list1)!=len(list2):
                        list2.append(a)
    print("aa ",list2)
    for b in range(len(list2)):
        """print('m ',list2[b])
        print('c ',list1[b])"""
        valeur=list1[b]-list2[b]
        print(valeur,str(list1[b])," ",str(list2[b]),"   ",b)
        if valeur<0:
            valeur+=26
            """
            print(valeur)"""
            nvlettres.append(valeur)
        else:
            nvlettres.append(valeur)

    print(nvlettres,"nvlettres")
    print(nvlettres[:25],"Jusqu'a 25, len =",len(nvlettres[:25]))

    for o in nvlettres:
        nvmot+=str(find_key(o))
    return(nvmot)

print(vigenereinverse(motatrouver,cle,list1,list2))

