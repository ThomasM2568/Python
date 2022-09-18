def est_bissextile (année):
    return(année)
année=est_bissextile(1900)
if année%400==0:
    print("L'année est bissextile")
elif année%4==0 and not année%100==0:
    print("L'année est bissextile")
else:
    print("L'année n'est pas bissextile")


