for nombre in range(1,101):
    if nombre%5==0 or nombre%7==0:
        print(nombre)

compteur=0
for nb in range(1,101):
    if nb%5==0 or nb%7==0:
        print(nb)
        compteur=compteur+1
        print("Il y a",compteur,"multiples")
