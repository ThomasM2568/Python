def pretraitement(motif):
    d=[]
    d2=[]
    dictionnaire={}
    for i in motif:
        d.append(i)
    print(d)
    for k in range(len(d)-1):
        valeur=(int(len(d))-int(k))-1
        d2.append(valeur)
    for a in range(1,2):
        d2.append(len(motif))
    print(d2)
    d.reverse()
    d2.reverse()
    for j in range(len(d)):
        cle=d[j]
        value=d2[j]
        if cle not in dictionnaire:
            dictionnaire[cle]=value
            print(dictionnaire)
        else:
            print("valeur "+str(cle)+" déjà présente, remplacement par la valeur précédente")
    return(dictionnaire)

#------------------------------------------------


def nombreelementcommun(decalage,mot,motif):
    n=0
    x=0
    for e in range(0,len(motif))[::-1]:
        if mot[e]==motif[e]:
            n+=1
        else:
            if x==0:
                x=e

    return x,n
#------------------------------------------------

def compare(chaine,mot,motif,dictionnaire):
    for e in range(0,len(motif))[::-1]:

        if mot[e]!=motif[e]:
            elementquicorrespondpas=mot[e]
            if elementquicorrespondpas in dictionnaire:
                print(str(elementquicorrespondpas) +" dans le dico")
                for valeurlettre in range(0,len(motif))[::-1]:
                    if elementquicorrespondpas == motif[valeurlettre]:
                        return ( e-valeurlettre)
        return(len(motif))

#------------------------------------------------
def recherche2(motif,chaine):
    dico=pretraitement(motif)

    mot=chaine[:len(motif)]
    print (mot)
    decalage=0
    position,nbegal=nombreelementcommun(decalage,mot,motif)
    print ("position de la valeur qui ne correspond pas "+str(position))
    print ("nb de valeur en commun "+str(nbegal))
    #while decalage<len(chaine):
    decalage=len(motif)-nbegal
    print(decalage)
    mot=''
    print ("etape 1")
    etape=1
    for i in range(decalage,len(motif)+decalage):
        mot=mot+str(chaine[i])


    print(mot)
    #for e in range(0,len(motif))[::-1]:
    #    if mot[e]==motif[e]:
    nb=0
    while mot != motif and decalage < len(chaine)-len(motif):
        etape+=1
        print("etape " + str(etape) )
        print (chaine)
        print (mot)
        res=compare(chaine,mot,motif,dico)
        if res <0:
            decalage=decalage+1
        else:
            decalage=decalage+res
        print(decalage)
        mot=''
        for i in range(decalage,len(motif)+decalage):
            mot=mot+str(chaine[i])
        print(mot)
    if mot == motif :
        return ("mot "+str(motif)+" trouvé en position "+str(decalage))
    else:
        return(-1)

#------------------------------------------------
def conversion(texte,dictionnaire):
    resultat=""
    for c in texte:
        resultat=resultat+"-"+dictionnaire[c]
    return resultat




motif="diamant"
chaine="aimant donnant un diamant"
print(recherche2(motif,chaine))



"""

Liste des acides aminés

A	Alanine	Ala
C	Cystéine	Cys
D	Acide aspartique	Asp
E	Acide glutamique	Glu
F	Phénylalanine	Phe
G	Glycine	Gly
H	Histidine	His
I	Isoleucine	Ile
K	Lysine	Lys
L	Leucine	Leu
M	Méthionine	Met
N	Asparagine	Asn
O	Pyrrolysine	Pyl
P	Proline	Pro
Q	Glutamine	Gln
R	Arginine	Arg
S	Sérine	Ser
T	Thréonine	Thr
U	Sélénocystéine	Sec
V	Valine	Val
W	Tryptophane	Trp
Y	Tyrosine	Tyr

"""

# dictionnaire des acides aminés
acidesamines={}
acidesamines["A"]="Ala"
acidesamines["C"]="Cys"
acidesamines["D"]="Asp"
acidesamines["E"]="Glu"
acidesamines["F"]="Phe"
acidesamines["G"]="Gly"
acidesamines["H"]="His"
acidesamines["I"]="Ile"
acidesamines["K"]="Lys"
acidesamines["L"]="Leu"
acidesamines["M"]="Met"
acidesamines["N"]="Asn"
acidesamines["O"]="Pyl"
acidesamines["P"]="Pro"
acidesamines["Q"]="Gln"
acidesamines["R"]="Arg"
acidesamines["S"]="Ser"
acidesamines["T"]="Thr"
acidesamines["U"]="Sec"
acidesamines["V"]="Val"
acidesamines["W"]="Trp"
acidesamines["Y"]="Tyr"


#print(acidesamines)

mon_fichier = open("adn.txt", "r")
contenu = mon_fichier.read()
#print(contenu)


mon_fichier.close()

#Renaud, Thomas et Clément















