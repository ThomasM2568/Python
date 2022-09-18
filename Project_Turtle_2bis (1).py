from tkinter import*
from sys import*
from PIL import*


def déci_to_bin(x) :
    """if x==x :
        return(x)
    else:"""
    arctis=int(x)
    corsair=''
    while arctis!=0 :
        razer=arctis%2
        arctis=arctis//2
        corsair=str(razer)+corsair
    return(int(corsair))

def bin_to_déci(x) :
    if x==x :
        return(x)
    else:
        l=len(x)
        total=0
        for i in range(l) :
            c=x[-i-1]
            if c=='1' :
                total=total+2**i
    return(total)

#arctis : nombre en déci puis quotient des division successives de arctis par 16
#corsair : résultat (reste des divisions successives de 'arctis' par 16)
#razer : reste d'une division de arctis par 16
def déci_to_hexa(x) :
    """if x==x :
        return(x)"""
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

def hexa_to_déci(x):
    """if x==x :
        return(x)
    else :"""
    L=len(x)-1
    total=0
    for c in x:
        total=int(c)*(16**L)+total
        L=L-1
    return(total)

def bin_to_hexa(x):
    """if x==x :
        return(x)
    else :"""
    return(déci_to_hexa(bin_to_déci(x)))

def hexa_to_bin(x):
    """if x==x :
        return(x)
    else :"""
    return(hexa_to_déci(déci_to_bin(x)))


def résultat(x,base,convertir_en):
    if base=="base 2":
        if convertir_en=="2" :
            return(x)
        elif convertir_en=="10" :
            return(bin_to_déci(x))
        else :
            return(bin_to_hexa(x))
    elif base=="base 10" :
        if convertir_en=="2" :
            return(déci_to_bin(x))
        elif convertir_en=="10" :
            return(x)
        else :
            return(déci_to_hexa(x))
    else :
        if convertir_en=="2" :
            return(hexa_to_bin(x))
        elif convertir_en=="10" :
            return(hexa_to_déci(x))
        else :
            return(x)

RR=int(input("Composante rouge de la fenêtre graphique entre 0 et 255"))
GG=int(input("Composante vert de la fenêtre graphique entre 0 et 255"))
BB=int(input("Composante bleue de la fenêtre graphique entre 0 et 255"))

if RR>255 or RR<0 or GG>255 or GG<0 or BB>255 or BB<0 :
    exit("Choisissez un nombre entre 0 et 255 !")

def RVB(octogone) :
    geonaute=déci_to_hexa(octogone)
    resultat=''
    if len(geonaute)==1 :
        resultat='0'+geonaute
        return(resultat)
    elif len(geonaute)==0 :
        resultat='0'+geonaute
        return(resultat)
    else :
        return(geonaute)

color='#'+RVB(RR)+RVB(GG)+RVB(BB)


v2=''
v3=''

def vA1(V2):
    V2='base 2'
    return(V2)

def vA2(V2):
    V2='base 10'
    return(V2)

def vA3(V2):
    V2='base 16'
    return(V2)

def vB1(V3):
    V3='2'
    return(V3)

def vB2(V3):
    V3='10'
    return(V3)

def vB3(V3):
    V3='16'
    return(V3)


def play():
    label_résultat= Label(window, text='')
    label_résultat.configure(text=answer)
    label_résultat.grid(row=8)




#fenêtre Tkinter
window= Tk()
window.title("My multi-base converter high-tech")
height=window.winfo_screenheight()
width=window.winfo_screenwidth()
window.minsize(height,width)
#window.iconbitmap("th1C83FK5V.ico")
window.config(background=color)
window.state('zoomed')


def fullscreen():
    window.attributes('-fullscreen',1)
def windowed():
    window.attributes('-fullscreen',0)
    window.state('zoomed')


#les Frames
"""
frame = Frame(window, bg=color, bd=1)
frame.grid(row=20)
"""


#titre et texte de la fenêtre
label_title = Label(window, text="Bienvenue sur le convertisseur multibase de haute technologie!", font=("Helvetica", 34), bg=color, fg='white')
label_title.grid(row=0,padx=YES)



#boutons pour interagir avec la fenêtre
bouton_fullscreen= Button(window, text="■", font=("Helvetica", 20), bg='white', fg='black', command=fullscreen)
bouton_fullscreen.grid(pady=1, row=0,column=1,sticky='ne')

bouton_windowed= Button(window, text="□", font=("Helvetica", 20), bg='white', fg='black', command=windowed)
bouton_windowed.grid(pady=1, row=0,column=2,sticky='ne')

bouton_quit=Button(window, text=" X ", font=("Helvetica", 15), bg='red', fg='black', command=window.destroy)
bouton_quit.grid(pady=1, row=0,column=3,sticky='ne')


bouton_résultat=Button(window, text="►", font=("Helvetica",20), bg='green', fg='black',command=play)
bouton_résultat.grid()

#champ de saisie -> interaction entre l'utilisateur et la fenêtre
var_user = IntVar()
ligne_texte = Entry(window,textvariable=var_user, width=40)
ligne_texte.grid(pady=5,sticky='n')

#créer des check buttons interactifs

choix_2 = Radiobutton(window, text="base 2", font=("Helvetica", 15),indicatoron=0,value="base 2")
choix_10 = Radiobutton(window, text="base 10", font=("Helvetica", 15), indicatoron=0,value="base 10")
choix_16 = Radiobutton(window, text="base 16", font=("Helvetica", 15), indicatoron=0,value="base 16")

choix_2.grid(pady=5,row=4,sticky='w')
choix_10.grid(pady=5,row=5,sticky='w')
choix_16.grid(pady=5,row=6,sticky='w')

choix_2.bind('<Button-1>',vA1)
choix_10.bind('<Button-1>',vA2)
choix_16.bind('<Button-1>',vA3)


answer_2 = Radiobutton(window, text="base 2", variable=ligne_texte,font=("Helvetica", 15), indicatoron=0,value="2")
answer_10 = Radiobutton(window, text="base 10", variable=ligne_texte,font=("Helvetica", 15), indicatoron=0,value="10")
answer_16 = Radiobutton(window, text="base 16", variable=ligne_texte,font=("Helvetica", 15), indicatoron=0,value="16")

answer_2.grid(pady=5,row=4,sticky='e')
answer_10.grid(pady=5,row=5,sticky='e')
answer_16.grid(pady=5,row=6,sticky='e')

answer_2.bind('<Button-1>',vB1)
answer_10.bind('<Button-1>',vB2)
answer_16.bind('<Button-1>',vB3)

Ωvar=var_user.get()
answer=résultat(int(Ωvar),v2,v3)

window.mainloop()
