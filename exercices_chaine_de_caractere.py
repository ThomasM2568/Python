"""
mot=input('Entrer un mot en minuscules')
nombre=int(input('Entrer un nombre'))
motcode=''
for lettre in mot:
    n=ord(lettre)
    n+=nombre
    if n>122:
        n=n-26
    motcode=motcode+chr(n)
print(motcode)
"""
"""
t='bonjour'
for n in range(len(t)):
    if n%2:
        print(n,t[n])
"""
#Exercice 1
'''
nombre=0
mot=input()
for lettre in mot:
    nombre+=1
    if nombre%2==0:
        print(lettre)
    else:
        lettre='*'
        print(lettre)
'''

#Exercice 2
'''nombre=0
mot=input()
for lettre in mot:
    nombre+=1
    valeur_lettre=ord(lettre)
    caractere=chr(valeur_lettre+nombre)
    print(caractere)
'''

#Exercice 3
'''n1=int(input("n1="))
n2=int(input("n2="))
mot=input("mot=")
nombre=0
for lettre in mot:
    nombre+=1
    if nombre%2==0:
        caractere=ord(lettre)+n1
        print(chr(caractere))
    else:
        caractere=ord(lettre)+n2
        print(chr(caractere))
'''
#Exercice 4
'''mot='bonjour'
nombre=0
for lettre in mot:
    nombre+=1
    if nombre%2==0:
        print(lettre.upper())
    else:
        print(lettre)
'''
#Exercice 5
'''
mot='abcdefghijklmnopqrstuvwxyz'
nombre=0
for lettre in mot:
    nombre+=1
    if ord(lettre)<(ord('n')-1):
        valeur=ord(lettre)+2
        print(chr(valeur))
    else:
        valeur=ord(lettre)+4
        print(chr(valeur).upper())
'''



