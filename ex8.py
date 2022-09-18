texte="FJKQEBFHZEBFHIJAZ3OTFIOAEMHFIAEHFIODHQFOPAE"
dictionnaire={}

for lettre in texte:
    print (lettre)
    if lettre in dictionnaire.keys():
        dictionnaire[lettre]+=1
    else:
        dictionnaire[lettre]=1

print(dictionnaire)



