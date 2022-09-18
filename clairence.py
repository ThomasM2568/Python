def clairence (age, creatininemie, poids, k):
    clairence=((140-age)/creatininemie)*poids*k
    return(clairence)
print(clairence(35,100,75,1.23))
