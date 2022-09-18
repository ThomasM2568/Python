import matplotlib.pyplot as plt
from math import *
from tri_par_insertion_thomas import tri_insertion

#Les fonctions------------------------
def import_des_donnees():
    fichier_csv=open("iris.csv", 'r')
    base=fichier_csv.readlines()
    fichier_csv.close()
    base_net=[]
    for i in range(1,len(base)):
        iris=[]
        chaine=base[i].split(",")
        iris.append(0)
        iris.append(float(chaine[0]))
        iris.append(float(chaine[1]))
        iris.append(chaine[2][:-1])
        base_net.append(iris)
    return base_net

def rep_graphique(D, k, x, y):
    iris_s_x=[]
    iris_s_y=[]
    iris_v_x=[]
    iris_v_y=[]
    iris_vi_x=[]
    iris_vi_y=[]
    #Constitution des listes de coordonnées pour chaque type d'iris
    for iris in D:
        if iris[3]=="Iris-setosa":
            iris_s_x.append(iris[1])
            iris_s_y.append(iris[2])
        elif iris[3]=="Iris-versicolor":
            iris_v_x.append(iris[1])
            iris_v_y.append(iris[2])
        else:
            iris_vi_x.append(iris[1])
            iris_vi_y.append(iris[2])
    plt.scatter(iris_s_x, iris_s_y, color='g', label='setosa', marker='+')
    plt.scatter(iris_vi_x, iris_vi_y, color='r', label='virginica', marker='+')
    plt.scatter(iris_v_x, iris_v_y, color='b', label='versicolor', marker='+')
    if (x!=0 and y!=0):
        plt.scatter(x,y,label='Iris trouve', color='k')
    if k!=0:
        for j in range(k):
            plt.arrow(x, y, D[j][1]-x, D[j][2]-y)
        #Gestion des égalités de longueurs avec les iris suivants k-1
        for j in range(0,len(D)):
            if D[j][0]==D[k-1][0] and j!=(k-1):
                plt.arrow(x, y, D[j][1]-x, D[j][2]-y, color='orange', ls=':')
            if  D[j][0]>D[k-1][0]:
                break
    plt.axis('equal')
    plt.xlim(0, 7)
    plt.xlabel("Longeur du pétale (cm)")
    plt.ylim(0.5,3)
    plt.ylabel("Largeur du pétale (cm)")
    plt.legend()
    plt.show()

def calcul_des_distances(donnees, x, y):
    for iris in donnees:
        xiris=iris[1]
        yiris=iris[2]
        distance=sqrt((xiris-x)**2+(yiris-y)**2)
        iris[0]=distance
        print(iris)

def identification(D, k, x, y):
    if k!=0:
        s=0
        vi=0
        v=0
        #Boucle while pour gérer les égalités avec la dernière valeur de distance
        i=0
        while D[i][0]<=D[k-1][0]:
            if D[i][3]=="Iris-setosa":
                s+=1
            elif D[i][3]=="Iris-virginica":
                vi+=1
            else:
                v+=1
            i+=1
        print("Setosa voisins :",s," - Virginica voisins :",vi," - Versicolor voisins :",v)
        if (s>vi and s>v):
            print ("L'iris trouve est de la variété Setosa")
        elif (vi>s and vi>v):
            print ("L'iris trouve est de la variété Virginica")
        elif (v>s and v>vi):
            print ("L'iris trouve est de la variété Versicolor")
        else:
            print ("Impossible de déterminer la variété de l'iris trouve")


def naif(L,element) :
    for x in range(len(L)) :
        print(x)
        if L[x]==element :
            return(x)
        if L[x]>element :
            return(-1)
    return(-1)


#Programme principal------------------
x=1
y=1
donnees=import_des_donnees()
#print(donnees)
print(calcul_des_distances(donnees,2,1))
print(tri_insertion(donnees))
L=[1,4,6,8,10,12,13,15,19,20,21,30,35,62,75,101,123,452,1000,1002,1102,2048]
identification(donnees,50,x,y)
rep_graphique(donnees,50,x,y)
print(naif(L,22))
