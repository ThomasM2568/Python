import thomasm as tm
from time import *
mois={"January":1,"Frebruary":2,"March":3,"April":4,"Mai":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}
parole="Bob"
chaine=""
test=tm.Creer_file_vide()
while chaine!="fin":

     chaine=input(parole+" :")
     jour=str(strftime("%d"))
     for j in mois.get(values):
        if j==(strftime("%B")):
            c=mois.get(j)
     annee=strftime("%Y")
     date=str(jour)+"/"+str(c)+"/"+str(annee)
     heure=str(strftime("%H:%M:%S"))
     dialogue="["+date+" "+str(heure)+"]"+" "+parole+" : "+chaine
     test.append(dialogue)
     if parole=="Bob":
        parole="John"
     else:
        parole="Bob"

for a in test:
    print(a)
