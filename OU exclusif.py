nombre=float(input("Entrez une valeur"))
if (nombre%3==0 and not nombre%5==0 and not nombre%7==0) or (nombre%5==0 and not nombre%3==0 and not nombre%7==0) or (nombre%7==0 and not nombre%3==0 and not nombre%5==0):
    print("Gagné")
else:
    print("Perdu")
