poids=float(input("entrez votre poids :"))
k=float(input("Entrez votre coefficient, 1.23 pour un homme et 1.04 pour une femme :"))
age=float(input("entrez votre age :"))
Cr=float(input("Entrez votre quantité de créatinine"))
Clcr=(140-age)/Cr*poids*k
if Clcr < 70:print("Vous êtes en insuffisance rénale")
else:print("vous n'êtes pas en insuffisance rénale")


