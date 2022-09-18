note1=float(input("entrez votre première note :"))

note2=float(input("entrez votre deuxième note :"))

moyenne=(note1+note2)/2

print(moyenne)

if moyenne < 8:
    print("Vous êtes recalé")
elif 8 < f < 10:
    print("Vous passez le rattrapage")
else :
    print("Vous êtes reçu")