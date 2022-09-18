text="FJUURTGDJGJFGMSWULYSWENBBBQOXVRBSDDJNUGHAJPGX"
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
    if rang_carac>=rang_cle:
        textcrypte+=chr( (rang_carac-rang_cle)   + 64)
    else:
        textcrypte+=chr( 26-(rang_cle-rang_carac)  + 64)


print(textcrypte)

