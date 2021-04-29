#########################################
# groupe MPCI 2
# Zachary MARIANI
# Jeremy ZORIC
# Baptiste PARIS
# Mohamed AKARKACH
# Pascal CHRISTOPHE
# El guehoudi Wacil

# https://github.com/uvsq22004748/Projet_Tapatan
#########################################

# On importe tkinter

import tkinter as tk
import pickle as pickle

racine = tk.Tk()

X = 100
Y = 100
COLORS = ['blue', 'red']
nombre_de_jetons = 0
depla = 0
vient_de_deplacer = 0
selection = 0

# cette liste evolue en meme temps que le plateau mais elle est interpretable par l'interpreteur python 

place = [[0,0,0],[0,0,0],[0,0,0]]


def arreter():
    ''' Cette fonction va arreter le programme en cours '''
    racine.destroy()

##################### PLACEMENT DES JETONS AU DEBUT DE LA PARTIE #####################

def clique(event):
    ''' Cette fonction va permettre de générer les jetons sur le schéma du jeu '''
    global nombre_de_jetons
    global couleur
    global depla
    global vient_de_deplacer
    global selection 
    global pion_selectionne

    global cercle1
    global cercle2
    global cercle3
    global cercle4
    global cercle5
    global cercle6
    global cercle7
    global cercle8
    global cercle9

    global cercle1_1
    global cercle2_1
    global cercle3_1
    global cercle4_1
    global cercle5_1
    global cercle6_1
    global cercle7_1
    global cercle8_1
    global cercle9_1

    if nombre_de_jetons % 2 == 0 :
        couleur = 'blue'
        pion = 1
    elif nombre_de_jetons % 2 == 1 :
        couleur = 'red'
        pion = -1
    couleurs = couleur
    """ cette partie de la fonction permet de placer les jetons en fonction de l'endroit ou l'on clique, il 
        n'est pas possible de placer un jeton au dessus d'un autre """

    if (50 <= event.x <= 150) and (50 <= event.y <= 150) and (nombre_de_jetons < 6):
        if place [0][0] == 0 :
            cercle1 = canvas.create_oval(X, Y, X, Y, fill = couleurs, outline = couleurs, width=20)
            nombre_de_jetons += 1
            place [0][0] = pion
        victoire ()
        gagne ()

    if (250 <= event.x <= 350) and (50 <= event.y <= 150) and (nombre_de_jetons < 6):        
        if place [0][1] == 0 :
            cercle2 = canvas.create_oval(3 * X, Y, 3 * X, Y, fill=couleurs, outline=couleurs, width=20)
            nombre_de_jetons += 1
            place [0][1] = pion
        victoire ()
        gagne ()

    if (450 <= event.x <= 550) and (50 <= event.y <= 150) and (nombre_de_jetons < 6):        
        if place [0][2] == 0 :
            cercle3 = canvas.create_oval(5 * X, Y, 5 * X, Y, fill=couleurs, outline=couleurs, width=20)
            nombre_de_jetons += 1
            place [0][2] = pion
        victoire ()
        gagne ()

    if (50 <= event.x <= 150) and (250 <= event.y <= 350) and (nombre_de_jetons < 6):        
        if place [1][0] == 0 :
            cercle4 = canvas.create_oval(X, 3 * Y, X, 3 * Y, fill=couleurs, outline=couleurs, width=20)
            nombre_de_jetons += 1
            place [1][0] = pion
        victoire ()
        gagne ()

    if (250 <= event.x <= 350) and (250 <= event.y <= 350) and (nombre_de_jetons < 6):        
        if place [1][1] == 0 :
            cercle5 = canvas.create_oval(3 * X, 3 * Y, 3 * X, 3 * Y, fill=couleurs, outline=couleurs, width=20)
            nombre_de_jetons += 1
            place [1][1] = pion
        victoire ()
        gagne ()

    if (450 <= event.x <= 550) and (250 <= event.y <= 350) and (nombre_de_jetons < 6):        
        if place [1][2] == 0 :
            cercle6 = canvas.create_oval(5 * X, 3 * Y, 5 * X, 3 * Y, fill=couleurs, outline=couleurs, width=20)
            nombre_de_jetons += 1
            place [1][2] = pion
        victoire ()
        gagne ()

    if (50 <= event.x <= 150) and (450 <= event.y <= 550) and (nombre_de_jetons < 6):       
        if place [2][0] == 0 :
            cercle7 = canvas.create_oval(X, 5 * Y, X, 5 * Y, fill=couleurs, outline=couleurs, width=20)
            nombre_de_jetons += 1
            place [2][0] = pion
        victoire ()
        gagne ()

    if (250 <= event.x <= 350) and (450 <= event.y <= 550) and (nombre_de_jetons < 6):       
        if place [2][1] == 0 :
            cercle8 = canvas.create_oval(3 * X, 5 * Y, 3 * X, 5 * Y, fill=couleurs, outline=couleurs, width=20)
            nombre_de_jetons += 1
            place [2][1] = pion
        victoire ()
        gagne ()

    if (450 <= event.x <= 550) and (450 <= event.y <= 550) and (nombre_de_jetons < 6):        
        if place [2][2] == 0 :
            cercle9 = canvas.create_oval(5 * X, 5 * Y, 5 * X, 5 * Y, fill=couleurs, outline=couleurs, width=20)
            nombre_de_jetons += 1
            place [2][2] = pion
        victoire ()
        gagne ()

##################################### DEPLACEMENT ################################

    """dans la deuxieme partie de la fonction principale on code le deplacement de chaques pions. lorque l'on clique sur un \
        pion deja existant on le selectionne, ensuite on clique a l'endroit ou l'on veut le deplacer. Chaque deplacement est ecrit \
            indidviduellement car pour le moment c'est la seule methode qui fonctionne."""

### place 1

    if (50 <= event.x <= 150) and (50 <= event.y <= 150) and (nombre_de_jetons >= 6):
        selection = 1
        pion_selectionne = 1
        if vient_de_deplacer == 0 :
            if place [0][0] != 0:
                cercle1_1 = canvas.create_oval(X, Y, X, Y, fill = "yellow", outline = "yellow", width=25)
                depla = 1
        if vient_de_deplacer == 1 :
            vient_de_deplacer -= 1
            return (vient_de_deplacer)
        


    if (250 <= event.x <= 350) and (50 <= event.y <= 150) and (depla == 1) and (place [0][1] == 0) and (pion_selectionne == 1):
        if place [0][0] == 1 :
            couleurs = "blue"
            color = 1
        if place [0][0] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle1)
        canvas.delete (cercle1_1)
        cercle2 = canvas.create_oval(3 * X, Y, 3 * X, Y, fill=couleurs, outline=couleurs, width=20)
        depla = 0
        place [0][0] = 0
        place [0][1] = color
        vient_de_deplacer = 1
        selection = 0

    if (250 <= event.x <= 350) and (250 <= event.y <= 350) and (depla == 1) and (place [1][1] == 0) and (pion_selectionne == 1):
        if place [0][0] == 1 :
            couleurs = "blue"
            color = 1
        if place [0][0] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle1)
        canvas.delete (cercle1_1)
        cercle5 = canvas.create_oval(3 * X, 3 * Y, 3 * X, 3 * Y, fill=couleurs, outline=couleurs, width=20)
        depla = 0
        place [0][0] = 0
        place [1][1] = color
        vient_de_deplacer = 1
        selection = 0

    if (50 <= event.x <= 150) and (250 <= event.y <= 350) and (depla == 1) and (place[1][0] == 0) and (pion_selectionne == 1):
        if place [0][0] == 1 :
            couleurs = "blue"
            color = 1
        if place [0][0] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle1)
        canvas.delete (cercle1_1)
        cercle4 = canvas.create_oval(X, 3 * Y, X, 3 * Y, fill=couleurs, outline=couleurs, width=20)
        depla = 0
        place [0][0] = 0
        place [1][0] = color
        vient_de_deplacer = 1
        selection = 0

### place 2

    if (250 <= event.x <= 350) and (50 <= event.y <= 150) and (nombre_de_jetons >= 6):
        selection = 1
        pion_selectionne = 2
        if vient_de_deplacer == 0 :
            if place [0][1] != 0:
                cercle2_1 = canvas.create_oval(3 * X, Y, 3 * X, Y, fill = "yellow", outline = "yellow", width=25)
                depla = 1
        if vient_de_deplacer == 1 :
            vient_de_deplacer -= 1
            return (vient_de_deplacer)


    if (50 <= event.x <= 150) and (50 <= event.y <= 150) and (depla == 1) and (place [0][0] == 0) and (pion_selectionne == 2):
        if place [0][1] == 1 :
            couleurs = "blue"
            color = 1
        if place [0][1] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle2)
        canvas.delete (cercle2_1)
        cercle1 = canvas.create_oval(X, Y, X, Y, fill = couleurs, outline = couleurs, width=20)
        depla = 0
        place [0][1] = 0
        place [0][0] = color
        vient_de_deplacer = 1

    if (250 <= event.x <= 350) and (250 <= event.y <= 350) and (depla == 1) and (place [1][1] == 0) and (pion_selectionne == 2):
        if place [0][1] == 1 :
            couleurs = "blue"
            color = 1
        if place [0][1] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle2)
        canvas.delete (cercle2_1)
        cercle5 = canvas.create_oval(3 * X, 3 * Y, 3 * X, 3 * Y, fill=couleurs, outline=couleurs, width=20)
        depla = 0
        place [0][1] = 0
        place [1][1] = color
        vient_de_deplacer = 1

    if (450 <= event.x <= 550) and (50 <= event.y <= 150) and (depla == 1) and (place [1][2] == 0) and (pion_selectionne == 2):
        if place [0][1] == 1 :
            couleurs = "blue"
            color = 1
        if place [0][1] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle2)
        canvas.delete (cercle2_1)
        cercle3 = canvas.create_oval(5 * X, Y, 5 * X, Y, fill=couleurs, outline=couleurs, width=20)
        depla = 0
        place [0][1] = 0
        place [1][2] = color
        vient_de_deplacer = 1

### place 3

    if (450 <= event.x <= 550) and (50 <= event.y <= 150) and (nombre_de_jetons >= 6):
        selection = 1
        pion_selectionne = 3
        if vient_de_deplacer == 0 :
            if place [0][2] != 0:
                cercle3_1 = canvas.create_oval(5 * X, Y, 5 * X, Y, fill = "yellow", outline = "yellow", width=25)
                depla = 1
        if vient_de_deplacer == 1 :
            vient_de_deplacer -= 1
            return (vient_de_deplacer)

    if (250 <= event.x <= 350) and (50 <= event.y <= 150) and (depla == 1) and (place [0][0] == 0) and (pion_selectionne == 3):
            if place [0][2] == 1 :
                couleurs = "blue"
                color = 1
            if place [0][2] == -1 :
                couleurs = "red"   
                color = -1
            canvas.delete (cercle3)
            canvas.delete (cercle3_1)
            cercle2 = canvas.create_oval(3 * X, Y, 3 * X, Y, fill=couleurs, outline=couleurs, width=20)
            depla = 0
            place [0][2] = 0
            place [0][1] = color
            vient_de_deplacer = 1

        


    print (place)

     
################# VICTOIRE ##################

def victoire (): 
    global win
    win = 0

    if place[0][0] + place [0][1] + place [0][2]==3 or place[1][0] + place [1][1] + place [1][2]==3 or \
         place[2][0] + place [2][1] + place [2][2]==3 or place[0][0] + place [1][0] + place [2][0]==3 or \
              place[0][1] + place [1][1] + place [2][1]==3 or place[0][2] + place [1][2] + place [2][2]==3 or \
                   place[0][0] + place [1][1] + place [2][2]==3 or place[0][2] + place [1][1] + place [2][0]==3 :
        win += 1

    if place[0][0] + place [0][1] + place [0][2]==-3 or place[1][0] + place [1][1] + place [1][2]==-3 or \
         place[2][0] + place [2][1] + place [2][2]==-3 or place[0][0] + place [1][0] + place [2][0]==-3 or \
              place[0][1] + place [1][1] + place [2][1]==-3 or place[0][2] + place [1][2] + place [2][2]==-3 or \
                   place[0][0] + place [1][1] + place [2][2]==-3 or place[0][2] + place [1][1] + place [2][0]==-3 :
        win -= 1

    return (win)        

def gagne () : 
    """cette fonction detect si 3 pions sont allignés"""
    global win
    if win == 1 :
        print ("Victoire des Bleu")
        blue_win = tk.Canvas (racine, width=200, height=50, bg='blue')
        blue_win.grid(row = 0, column = 4)
    if win == -1 :
        print ("Victoire des Rouges")
        red_win = tk.Canvas (racine, width=200, height=50, bg='red')
        red_win.grid(row = 0, column = 4)


def sauvegarder () :
    """Sauvegarde les valeurs dans la liste dans le fichier sauvegarde.txt"""
    pickle.dump (place, open("sauvegarde.p", "wb"))


def charger () : 
    global place
    global nombre_de_jetons
    global cercle1, cercle2, cercle3, cercle4, cercle5, cercle6, cercle6, cercle7, cercle8, cercle9

    place = pickle.load (open("sauvegarde.p", "rb"))
    
    if place [0][0] == 1 :
        cercle1 = canvas.create_oval(X, Y, X, Y, fill = "blue", outline = "blue", width=20)
    if place [0][0] == -1 :
        cercle1 = canvas.create_oval(X, Y, X, Y, fill = "red", outline = "red", width=20)

    if place [0][1] == 1 :
        cercle2 = canvas.create_oval(3 * X, Y, 3 * X, Y, fill="blue", outline="blue", width=20)
    if place [0][1] == -1 :
        cercle2 = canvas.create_oval(3 * X, Y, 3 * X, Y, fill="red", outline="red", width=20)

    if place [0][2] == 1 :
        cercle3 = canvas.create_oval(5 * X, Y, 5 * X, Y, fill="blue", outline="blue", width=20)
    if place [0][2] == -1 :
        cercle3 = canvas.create_oval(5 * X, Y, 5 * X, Y, fill="red", outline="red", width=20)

    if place [1][0] == 1 :
        cercle4 = canvas.create_oval(X, 3 * Y, X, 3 * Y, fill="blue", outline="blue", width=20)
    if place [1][0] == -1 :
        cercle4 = canvas.create_oval(X, 3 * Y, X, 3 * Y, fill="red", outline="red", width=20)

    if place [1][1] == 1 :
        cercle5 = canvas.create_oval(3 * X, 3 * Y, 3 * X, 3 * Y, fill="blue", outline="blue", width=20)
    if place [1][1] == -1 :
        cercle5 = canvas.create_oval(3 * X, 3 * Y, 3 * X, 3 * Y, fill="red", outline="red", width=20)

    if place [1][2] == 1 :
        cercle6 = canvas.create_oval(5 * X, 3 * Y, 5 * X, 3 * Y, fill="blue", outline="blue", width=20)
    if place [1][2] == -1 :
        cercle6 = canvas.create_oval(5 * X, 3 * Y, 5 * X, 3 * Y, fill="red", outline="red", width=20)

    if place [2][0] == 1 :
        cercle7 = canvas.create_oval(X, 5 * Y, X, 5 * Y, fill="blue", outline="blue", width=20)
    if place [2][0] == -1 :
        cercle7 = canvas.create_oval(X, 5 * Y, X, 5 * Y, fill="red", outline="red", width=20)

    if place [2][1] == 1 :
        cercle8 = canvas.create_oval(3 * X, 5 * Y, 3 * X, 5 * Y, fill="blue", outline="blue", width=20)
    if place [2][1] == -1 :
        cercle8 = canvas.create_oval(3 * X, 5 * Y, 3 * X, 5 * Y, fill="red", outline="red", width=20)

    if place [2][2] == 1 :
        cercle9 = canvas.create_oval(5 * X, 5 * Y, 5 * X, 5 * Y, fill="blue", outline="blue", width=20)
    if place [2][2] == -1 :
        cercle9 = canvas.create_oval(5 * X, 5 * Y, 5 * X, 5 * Y, fill="red", outline="red", width=20)
    
    nombre_de_jetons = 6

    return (place)

def recommencer () :
    global place, nombre_de_jetons
    if place [0][0] != 0 :
        canvas.delete (cercle1)
    if place [0][1] != 0 :
        canvas.delete (cercle2)
    if place [0][2] != 0 :
        canvas.delete (cercle3)
    if place [1][0] != 0 :
        canvas.delete (cercle4)
    if place [1][1] != 0 :
        canvas.delete (cercle5)
    if place [1][2] != 0 :
        canvas.delete (cercle6)
    if place [2][0] != 0 :
        canvas.delete (cercle7)
    if place [2][1] != 0 :
        canvas.delete (cercle8)
    if place [2][2] != 0 :
        canvas.delete (cercle9)
    nombre_de_jetons = 0
    place = [[0,0,0],[0,0,0],[0,0,0]]
            
    

"""
    fic = open ("sauvegarde.txt", "r")
    print (fic)
"""

"""
L1 = place[0][0] + place [0][1] + place [0][2]
L2 = place[1][0] + place [1][1] + place [1][2]
L3 = place[2][0] + place [2][1] + place [2][2]
C1 = place[0][0] + place [1][0] + place [2][0]
C2 = place[0][1] + place [1][1] + place [2][1]
C3 = place[0][2] + place [1][2] + place [2][2]
D1 = place[0][0] + place [1][1] + place [2][2]
D2 = place[0][2] + place [1][1] + place [2][0]
"""


canvas = tk.Canvas(racine, width=600, height=600, bg='black')
arreter = tk.Button(racine, text='Arrêter', bg='grey', command=arreter)
sauvegarde = tk.Button(racine, text= "Sauvegarder", bg = "grey", command=sauvegarder)
charger = tk.Button(racine, text= "Charger", bg = "grey", command=charger)
canvas.bind('<Button-1>', clique)

############ PLATEAU #################
carre = canvas.create_rectangle(X, Y, 600 - X, 600 - Y, outline='white')
ligne_verticale = canvas.create_line(3 * X, Y, 3 * X, 5 * Y, fill='white')
ligne_horizontale = canvas.create_line(X, 3 * Y, 5 * X, 3 * Y, fill='white')
diagonale1 = canvas.create_line(X, Y, 5 * X, 5 * Y, fill='white')
diagonale2 = canvas.create_line(X, 5 * Y, 5 * X, Y, fill='white')

canvas.grid(row=0, column=0, columnspan=4)
arreter.grid(row=1, column=4)
sauvegarde.grid(row=1, column=2)
charger.grid(row=1, column=1)

#cela sert juste a créer un espace a droite du canvas de base
espace = tk.Canvas(racine,width=200, height=1, bg='white')
espace.grid (column=4)

racine.mainloop()
