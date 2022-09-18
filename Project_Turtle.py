# Projet Converstisseur multibase avec Tkinter
# Thomas Mirbey & Maxence Desmonteix

from tkinter.messagebox import *
from tkinter import*

# Fonctions de conversion

# fonction deci_to_bin
# conversion decimal en binaire
# paramètre en entrée : q - nombre decimal à convertir
# paramètre en sortie : result - nombre binaire converti
def deci_to_bin(q):
    result = ""
    while q != 0 :
        r=q%2
        q=q//2
        #print ( "q {q} r {r}".format(q=q,r=r))
        result=str(r)+result
    return(result)

# fonction bin_to_deci
# conversion binaire à décimal
# paramètre en entrée : q - nombre binaire à convertir
# paramètre en sortie : total - nombre décimal converti
def bin_to_deci(q):

    L=len(q)-1
    total=0
    for c in q:
        total=int(c)*(2**L)+total
        L=L-1

    return(total)

# fonction deci_to_hexa
# conversion decimal à hexadecimal
# paramètre en entrée : x - nombre décimal à convertir
# paramètre en sortie : total - nombre hexa converti
def deci_to_hexa(x) :
    #arctis : nombre en déci puis quotient des division successives de arctis par 16
    #corsair : résultat (reste des divisions successives de 'arctis' par 16)
    #razer : reste d'une division de arctis par 16
    arctis=int(x)
    corsair=''
    if arctis==0 :
        razer='0'
        corsair=str(razer)
    else :
        while arctis!=0 :
            razer=arctis%16
            if razer==0 :
                razer='0'
            elif razer==10 :
                razer='a'
            elif razer==11 :
                razer='b'
            elif razer==12 :
                razer='c'
            elif razer==13 :
                razer='d'
            elif razer==14 :
                razer='e'
            elif razer==15 :
                razer='f'
            elif razer==16 :
                razer='10'
            arctis=arctis//16
            corsair=str(razer)+corsair
    return(corsair)

# fonction hexa_to_deci
# conversion hexadimal à decimal
# paramètre en entrée : x - nombre hexadecimal à convertir
# paramètre en sortie : total - nombre decimal converti
def hexa_to_deci(x):
    L=len(x)-1
    total=0
    for c in x:
        if c == "F" or c =="f":
            car=15
        elif c == "E" or c == 'e':
            car=14
        elif c == "D" or c == "d":
            car=13
        elif c == "C" or c == "c":
            car=12
        elif c == "B" or c == "b":
            car=11
        elif c == "A" or c == "a":
            car=10
        else:
             car=c
        total=int(car)*(16**L)+total
        L=L-1
    return(total)

# fonction convertir
# fonction permettant de convertir un nombre en base 2,10,16
# paramètres en entrée : nombre - nombre à convertir
#                        basesource - base du nombre à convertir
#                        basedestination - base du nombre converti

def convertir(nombre, basesource, basedestination):
    if basesource == basedestination:
        # 0 - conversion en même base ... message d'erreur
        showerror("Error", "Conversion en même base")
        return(0)
    else:
        # 1 - conversion en binaire vers ...
        if basesource == 2 and basedestination == 10:
            print ("*** conversion base2 vers base10")
            if estUnNombreBinaire(nombre):
                return(bin_to_deci(nombre))
            else:
                showerror("Error", "Le nombre saisi n'est pas un nombre binaire")
        elif basesource == 2 and basedestination == 16:
            print ("*** conversion base2 vers base16")
            if estUnNombreBinaire(nombre):
                return(deci_to_hexa(bin_to_deci(nombre)))
            else:
                showerror("Error", "Le nombre saisi n'est pas un nombre binaire")
        # 2 - conversion base 10 vers ...
        elif basesource == 10 and basedestination == 2:
            print ("*** conversion base10 vers base2")
            if estUnNombreDecimal(nombre):
                return(deci_to_bin(int(nombre)))
            else:
                showerror("Error", "Le nombre saisi n'est pas un nombre decimal")
        elif basesource == 10 and basedestination == 16:
            print ("*** conversion base10 vers base16")
            if estUnNombreDecimal(nombre):
                return (deci_to_hexa(nombre))
            else:
                showerror("Error", "Le nombre saisi n'est pas un nombre decimal")
        # 3 - conversion base 16 vers ...
        elif basesource == 16 and basedestination == 2:
            print ("*** conversion base16 vers base2")
            if estUnNombreHexadecimal(nombre):
                return(deci_to_bin(hexa_to_deci(nombre)))
            else :
                showerror("Error", "Le nombre saisi n'est pas un nombre hexadecimal")
        elif basesource == 16 and basedestination == 10:
            print ("*** conversion base16 vers base10")
            if estUnNombreHexadecimal(nombre):
                return(hexa_to_deci(nombre))
            else:
                showerror("Error", "Le nombre saisi n'est pas un nombre hexadecimal")
        # 4 - une des bases n'est pas selectionnée ... Error
        elif basesource == 0 or basedestination == 0:
            showerror("Error", "merci de choisir une base source et une base destination")

# fonction estUnNombreBinaire
# détermine si une chaine de caractère est un nombre binaire
# paramètre en entrée : nombre - nombre à tester
# paramètre en sortie : True - les caractères de la chaine en entrée correspondent à un nombre binaire
#                       False - les caractères de la chaine en entrée ne correspondent pas à un nombre binaire
def estUnNombreBinaire(nombre):
    for c in nombre:
        if c != "0" and c != "1":
            return False
    return True

# fonction estUnNombreDecimal
# détermine si une chaine de caractère est un nombre Decimal
# paramètre en entrée : nombre - nombre à tester
# paramètre en sortie : True - les caractères de la chaine en entrée correspondent à un nombre decimal
#                       False - les caractères de la chaine en entrée ne correspondent pas à un nombre decimal
def estUnNombreDecimal(nombre):
    for c in nombre:
        if c not in "0123456789":
            return False
    return True

# fonction estUnNombreHexaecimal
# détermine si une chaine de caractère est un nombre Hexaecimal
# paramètre en entrée : nombre - nombre à tester
# paramètre en sortie : True - les caractères de la chaine en entrée correspondent à un nombre hexadecimal
#                       False - les caractères de la chaine en entrée ne correspondent pas à un nombre hexadecimal
def estUnNombreHexadecimal(nombre):
    for c in nombre:
        if c not in "aAbBcCdDeEfF0123456789":
            return False
    return True

#
# fonctions tkinter associées aux boutons
#

# fonction conversion
# lancement de la conversion appelée lorsqu'un clique sur le bouton bouton_resultat
# pas de paramètre

def conversion():
    print("Conversion")
    # contrôle des paramètres
    print ("Base de conversion source = Base {varsource}".format(varsource=varsource.get()))
    print ("Base de conversion destination = Base {vardest}".format(vardest=vardest.get()))
    print ("Nombre à convertir = {nombreaconvertir}".format(nombreaconvertir=nombreaconvertir.get()))
    # lancement de la conversion
    answer=convertir(nombreaconvertir.get(),varsource.get(),vardest.get())
    # affichage du résultat
    label_resultat= Label(window, text='', font=("Helvetica", 20), bg='yellow')
    print ("Résultat de la conversion = {answer}".format(answer=answer))
    print("")
    label_resultat.configure(text="               "+str(answer)+"              ")
    label_resultat.grid(row=8)

# fonction fullscreen
# permet de passer la fenêtre en plein ecran
# pas de paramètre
def fullscreen():
    window.attributes('-fullscreen',1)

# fonction windowed
# permet de réduire la fenêtre
# pas de paramètre
def windowed():
    window.attributes('-fullscreen',0)
    window.state('zoomed')


# Pogramme principal
#fenêtre Tkinter
color='black'
window= Tk()
window.title("My multi-base converter high-tech")
height=window.winfo_screenheight()
width=window.winfo_screenwidth()
window.minsize(height,width)
#window.iconbitmap("th1C83FK5V.ico")
window.config(background=color)
window.state('zoomed')

#titre et texte de la fenêtre
label_title = Label(window, text="Bienvenue sur le convertisseur multibase \nde haute technologie!", font=("Helvetica", 34), bg=color, fg='white')
label_title.grid(row=0,padx=YES)

#boutons pour interagir avec la fenêtre
# bouton fullscreen
bouton_fullscreen= Button(window, text="■", font=("Helvetica", 20), bg='white', fg='black', command=fullscreen)
bouton_fullscreen.grid(pady=1, row=0,column=1,sticky='ne')

# bouton windowed
bouton_windowed= Button(window, text="□", font=("Helvetica", 20), bg='white', fg='black', command=windowed)
bouton_windowed.grid(pady=1, row=0,column=2,sticky='ne')

# bouton quit
bouton_quit=Button(window, text=" X ", font=("Helvetica", 15), bg='red', fg='black', command=window.destroy)
bouton_quit.grid(pady=1, row=0,column=3,sticky='ne')

# bouton résultat pour lancer la conversion
bouton_resultat=Button(window, text="Convertir", font=("Helvetica",20), bg='green', fg='black',command=conversion)
bouton_resultat.grid()

# champ de saisie -> interaction entre l'utilisateur et la fenêtre
# nombre à convertir
nombreaconvertir = StringVar()
ligne_texte = Entry(window,textvariable=nombreaconvertir, width=40)
ligne_texte.grid(pady=5,sticky='n')

# création des check buttons interactifs

# source
varsource=IntVar()
choix_2 = Radiobutton(window, text="base 2", variable=varsource, font=("Helvetica", 15),indicatoron=0,value=2)
choix_10 = Radiobutton(window, text="base 10", variable=varsource, font=("Helvetica", 15), indicatoron=0,value=10)
choix_16 = Radiobutton(window, text="base 16", variable=varsource, font=("Helvetica", 15), indicatoron=0,value=16)

choix_2.grid(pady=5,row=4,sticky='w')
choix_10.grid(pady=5,row=5,sticky='w')
choix_16.grid(pady=5,row=6,sticky='w')

# destination
vardest=IntVar()
answer_2 = Radiobutton(window, text="base 2", variable=vardest,font=("Helvetica", 15), indicatoron=0,value=2)
answer_10 = Radiobutton(window, text="base 10", variable=vardest,font=("Helvetica", 15), indicatoron=0,value=10)
answer_16 = Radiobutton(window, text="base 16", variable=vardest,font=("Helvetica", 15), indicatoron=0,value=16)

answer_2.grid(pady=5,row=4,sticky='e')
answer_10.grid(pady=5,row=5,sticky='e')
answer_16.grid(pady=5,row=6,sticky='e')

window.mainloop()
