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