from random import *

def cle_aleatoire(n):
    cle=""
    for i in range(n):
        bit=randint(0,1)
        cle+=str(bit)
    return cle

def vernam(m, key):
    #conversion du message en binaire
    message_bin=""
    for lettre in m:
        code=ord(lettre)
        #code_bin=bin(code)[2::].zfill(8) #conversion binaire imposée sur 8 bits
        code_bin=format(code,'08b')
        message_bin+=code_bin
    #chiffrement
    message_chiffre=""
    for i in range(len(message_bin)):
        bit_crypte=int(message_bin[i])^int(key[i])
        message_chiffre+=str(bit_crypte)
    print("mess  ="+m)
    print("m_bin ="+message_bin)
    print("cle   ="+key)
    print("m_chif="+message_chiffre)
    return message_chiffre

#lecture du message dans le fichier message.txt
fichier_message=open('message.txt','r')
message=fichier_message.read()
fichier_message.close()
#Génération de la clé et inscription dans le fichier cle.txt
ma_cle=open('cle.txt','w')
cle=cle_aleatoire(len(message)*8)
ma_cle.write(cle)
ma_cle.close()
#chiffrement du message
chiffre=vernam(message,cle)
mon_fichier=open('message_chiffre.txt', 'w')
mon_fichier.write(chiffre)
mon_fichier.close()

