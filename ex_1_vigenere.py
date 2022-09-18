cle="TERMINALE"
texte="FJUURTGDJGJFGMSWULYSWENBBBQOXVRBSDDJNUGHAJPGX"
#les décalages de la clé
decalage_cle=[]
for caract in cle:
    decalage_cle.append(ord(caract)-64)
#decodage du texte
print(decalage_cle)

texte_decod=""
for i in range(len(texte)):
    print("i ",i, texte[i])
    rang_carac=ord(texte[i])-64
    print("rang_carac", rang_carac)

    rang_cle=decalage_cle[i%(len(cle))]
    print("carac cle", rang_cle, i%(len(cle)))
    print("rang-cle",rang_cle)
    if rang_carac>=rang_cle:
        texte_decod+=chr( (rang_carac-rang_cle)   + 64)
    else:
        texte_decod+=chr( 26-(rang_cle-rang_carac)  + 64)

print(texte_decod)