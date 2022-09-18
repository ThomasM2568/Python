from math import *
a=float(input("Entrez la valeur de a :"))
b=float(input("Entrez la valeur de b :"))

if a < 0 or b < 0:
    print("Le triangle n'est pas réalisable, a ou b n'est pas positif")
elif a==b:
    print("Le Triangle n'est pas rectangle, a est égal à b")
elif b>a:
   print("Le Triangle n'est pas réalisable, b est plus grand que a")
elif asin(b/a)*180/pi >45:
    print("L'angle est supérieur à 45°, l'angle vaut",asin(b/a)*180/pi,"°")
else:
    print("L'angle est inférieur à 45°, l'angle vaut",asin(b/a)*180/pi,"°")
