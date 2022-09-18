# Programme Python pour l'implémentation du tri par insertion
test=[]
def tri_insertion(test):
    # Parcour de 1 à la taille du tab
    for i in range(1, len(test)):
        k = test[i]
        j = i-1
        while j >= 0 and k < test[j] :
                test[j + 1] = test[j]
                j -= 1
        test[j + 1] = k
# Programme principale pour tester le code ci-dessus
test = [98, 22, 15, 32, 2, 74, 63, 70]
tri_insertion(test)
print ("Le tableau trié est:")
for i in range(len(test)):
    print ("% d" % test[i])


def er(test2):
    for i in range(1,len(test2)):
        t=test2[i]
        z=i-1
        while z >= 0 and t < test2[z]:
            test2[z+1]=test2[z]
            z-=1
        test2[z+1]=t


test2 = [98, 22, 15, 32, 2, 74, 63, 70]
er(test2)
print ("Le tableau trié est:")
for i in range(len(test)):
    print ("% d" % test[i])
