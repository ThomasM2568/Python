D={}
p="AGWPSGGASAGLAILWGASAIMPGALW"
for J in p:
    if J in D:
        D[J]+=1
    else:
        D[J]=1