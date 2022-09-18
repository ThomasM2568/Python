from random import choice
def mdp():
    return choice('azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCBVBN123456789')

a=''
nb=int(input("Entrez le nombre de valeur souhaité"))
for i in range(nb):
    a=a+mdp()
print("Le mot de passe est " + a)