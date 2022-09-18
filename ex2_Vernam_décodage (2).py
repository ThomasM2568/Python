#Récupération du message chiffré
message=open('message_chiffre.txt','r')
message_chiffre=message.read()
message.close()
#Récupération de la clé
fichier_cle=open('cle.txt', 'r')
cle=fichier_cle.read()
fichier_cle.close()
#Application de la clé pour déchiffrement
message_bin=""
for i in range(len(message_chiffre)):
    bit=int(message_chiffre[i])^int(cle[i])
    message_bin+=str(bit)
#Lecture des octets du message déchiffré avec décodage des caractères
message=""
for j in range(0,len(message_bin),8):
    octet=message_bin[j:j+8]
    code=int(octet,2)
    caractere=chr(code)
    message+=caractere
print(message)