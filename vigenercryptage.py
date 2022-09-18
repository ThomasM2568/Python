text="LECHIFFREMENTDEVIGENERENAPLUSDESECRETPOURVOUS"
clef="TERMINALE"
new_clef=""

while len(new_clef) < len (text):
    print("ddd")
    new_clef+=clef
    print(new_clef)

new_clef+=clef

new_clef=new_clef[0:len(text)]

print (new_clef)
print (text)

textcrypte=""

for i in range(len(text)):
    rang_carac=ord(text[i])-64
    rang_cle=ord(new_clef[i])-64
    print('rang_carac',rang_carac)
    print('rang_cle',rang_cle)
    somme = rang_carac + rang_cle
    if somme > 26 :
        n=somme-26
    else:
        n=somme
    textcrypte+=chr(n+64)



print(textcrypte)

#FJUURTGDJGJFGMSWULYSWENBBBQOXVRBSDDJNUGHAJPGX