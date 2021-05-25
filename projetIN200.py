#########################################
# groupe MPCI 2
# Zachary MARIANI
# Jeremy ZORIC
# Baptiste PARIS (absent)
# Mohamed AKARKACH (absent)
# Pascal CHRISTOPHE
# El guehoudi Wacil (absent)

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
selection = 0
selection_bleu = 0
selection_rouge = 1
pion_selectionne = 0
victoire_bleu = 0
victoire_rouge = 0
Tours = 0
# cette liste evolue en meme temps que le plateau mais elle est interpretable par l'interpreteur python 

place = [[0,0,0],[0,0,0],[0,0,0]]


def arreter():
    ''' Cette fonction va arreter le programme en cours '''
    racine.destroy()

##################### PLACEMENT DES JETONS AU DEBUT DE LA PARTIE #####################

def clique(event):
    ''' Cette fonction va permettre de générer les jetons sur le schéma du jeu et de les deplacer. La premiere partie sert a placer les pions sur le plateau,\
         la seconde partie permet de les deplacer, chaque deplacement est ecrit individuellement : lorsque l'on clique sur un pion, on le selectionne \
             ensuite il faut cliquer a l'endroit ou nous voulons le deplacer'''
             
    global cercle1, cercle2, cercle3, cercle4, cercle5, cercle6, cercle7, cercle8, cercle9, cercle1_1, cercle2_1, cercle3_1, cercle4_1, cercle5_1, cercle6_1, cercle7_1, cercle8_1, cercle9_1
    global suite, selection_bleu, selection_rouge, pion_selectionne, nombre_de_jetons, couleur, selection

    if nombre_de_jetons % 2 == 0 :
        couleur = 'blue'
        pion = 1
    elif nombre_de_jetons % 2 == 1 :
        couleur = 'red'
        pion = -1
    couleurs = couleur


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

    if nombre_de_jetons == 6 :
        suite = tk.Button (racine,text='cliquez ici pour continuer', width=40, height=20, command=phase_deux)
        suite.grid(row=2, column=2)


##################################### DEPLACEMENT ################################

### place 1

    if (50 <= event.x <= 150) and (50 <= event.y <= 150) and (nombre_de_jetons > 6) and (place [0][0] != 0) and (selection == 0):
        if (selection_bleu == 0) and (place [0][0] == 1) :
            cercle1_1 = canvas.create_oval(X, Y, X, Y, fill = "yellow", outline = "yellow", width=25)
            selection_bleu = 1
            selection_rouge = 0
            pion_selectionne = 1
            selection = 1
        if (selection_rouge == 0) and (place [0][0] == -1) :
            cercle1_1 = canvas.create_oval(X, Y, X, Y, fill = "yellow", outline = "yellow", width=25)
            selection_rouge = 1
            selection_bleu = 0
            pion_selectionne = 1
            selection = 1

    if (250 <= event.x <= 350) and (50 <= event.y <= 150) and (place [0][1] == 0) and (pion_selectionne == 1):
        if place [0][0] == 1 :
            couleurs = "blue"
            color = 1
        if place [0][0] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle1, cercle1_1)
        cercle2 = canvas.create_oval(3 * X, Y, 3 * X, Y, fill=couleurs, outline=couleurs, width=20)
        place [0][0] = 0
        place [0][1] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
        

    if (250 <= event.x <= 350) and (250 <= event.y <= 350) and (place [1][1] == 0) and (pion_selectionne == 1):
        if place [0][0] == 1 :
            couleurs = "blue"
            color = 1
        if place [0][0] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle1, cercle1_1)
        cercle5 = canvas.create_oval(3 * X, 3 * Y, 3 * X, 3 * Y, fill=couleurs, outline=couleurs, width=20)
        place [0][0] = 0
        place [1][1] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
        

    if (50 <= event.x <= 150) and (250 <= event.y <= 350) and (place [1][0] == 0) and (pion_selectionne == 1):
        if place [0][0] == 1 :
            couleurs = "blue"
            color = 1
        if place [0][0] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle1, cercle1_1)
        cercle4 = canvas.create_oval(X, 3 * Y, X, 3 * Y, fill=couleurs, outline=couleurs, width=20)
        place [0][0] = 0
        place [1][0] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
       

### place 2

    if (250 <= event.x <= 350) and (50 <= event.y <= 150) and (nombre_de_jetons > 6) and (place [0][1] != 0) and (selection == 0):
        if (selection_bleu == 0) and (place [0][1] == 1) :
            cercle2_1 = canvas.create_oval(3 * X, Y, 3 * X, Y, fill = "yellow", outline = "yellow", width=25)
            selection_bleu = 1
            selection_rouge = 0
            pion_selectionne = 2
            selection = 1
        if (selection_rouge == 0) and (place [0][1] == -1) :
            cercle2_1 = canvas.create_oval(3 * X, Y, 3 * X, Y, fill = "yellow", outline = "yellow", width=25)
            selection_rouge = 1
            selection_bleu = 0
            pion_selectionne = 2
            selection = 1

    if (50 <= event.x <= 150) and (50 <= event.y <= 150) and (place [0][1] == 0) and (pion_selectionne == 2):
        if place [0][1] == 1 :
            couleurs = "blue"
            color = 1
        if place [0][1] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle2, cercle2_1)
        cercle1 = canvas.create_oval(X, Y, X, Y, fill = couleurs, outline = couleurs, width=20)
        place [0][1] = 0
        place [0][0] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
        

    if (250 <= event.x <= 350) and (250 <= event.y <= 350) and (place [1][1] == 0) and (pion_selectionne == 2):
        if place [0][1] == 1 :
            couleurs = "blue"
            color = 1
        if place [0][1] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle2, cercle2_1)
        cercle5 = canvas.create_oval(3 * X, 3 * Y, 3 * X, 3 * Y, fill=couleurs, outline=couleurs, width=20)
        place [0][1] = 0
        place [1][1] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
       

    if (450 <= event.x <= 550) and (50 <= event.y <= 150) and (place [0][2] == 0) and (pion_selectionne == 2):
        if place [0][1] == 1 :
            couleurs = "blue"
            color = 1
        if place [0][1] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle2, cercle2_1)
        cercle3 = canvas.create_oval(5 * X, Y, 5 * X, Y, fill=couleurs, outline=couleurs, width=20)
        place [0][1] = 0
        place [0][2] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
        

### place 3

    if (450 <= event.x <= 550) and (50 <= event.y <= 150) and (nombre_de_jetons > 6) and (place [0][2] != 0) and (selection == 0):
        if (selection_bleu == 0) and (place [0][2] == 1) :
            cercle3_1 = canvas.create_oval(5 * X, Y, 5 * X, Y, fill = "yellow", outline = "yellow", width=25)
            selection_bleu = 1
            selection_rouge = 0
            pion_selectionne = 3
            selection = 1
        if (selection_rouge == 0) and (place [0][2] == -1) :
            cercle3_1 = canvas.create_oval(5 * X, Y, 5 * X, Y, fill = "yellow", outline = "yellow", width=25)
            selection_rouge = 1
            selection_bleu = 0
            pion_selectionne = 3
            selection = 1

    if (250 <= event.x <= 350) and (50 <= event.y <= 150) and (place [0][1] == 0) and (pion_selectionne == 3):
        if place [0][2] == 1 :
            couleurs = "blue"
            color = 1
        if place [0][2] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle3, cercle3_1)
        cercle2 = canvas.create_oval(3 * X, Y, 3 * X, Y, fill=couleurs, outline=couleurs, width=20)
        place [0][2] = 0
        place [0][1] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
       

    if (250 <= event.x <= 350) and (250 <= event.y <= 350) and (place [1][1] == 0) and (pion_selectionne == 3):
        if place [0][2] == 1 :
            couleurs = "blue"
            color = 1
        if place [0][2] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle3, cercle3_1)
        cercle5 = canvas.create_oval(3 * X, 3 * Y, 3 * X, 3 * Y, fill=couleurs, outline=couleurs, width=20)
        place [0][2] = 0
        place [1][1] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
        

    if (450 <= event.x <= 550) and (250 <= event.y <= 350) and (place [1][2] == 0) and (pion_selectionne == 3):
        if place [0][2] == 1 :
            couleurs = "blue"
            color = 1
        if place [0][2] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle3, cercle3_1)
        cercle6 = canvas.create_oval(5 * X, 3 * Y, 5 * X, 3 * Y, fill=couleurs, outline=couleurs, width=20)
        place [0][2] = 0
        place [1][2] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
        

### place 4 

    if (50 <= event.x <= 150) and (250 <= event.y <= 350) and (nombre_de_jetons > 6) and (place [1][0] != 0) and (selection == 0):
        if (selection_bleu == 0) and (place [1][0] == 1) :
            cercle4_1 = canvas.create_oval(X, 3 * Y, X, 3 * Y, fill = "yellow", outline = "yellow", width=25)
            selection_bleu = 1
            selection_rouge = 0
            pion_selectionne = 4
            selection = 1
        if (selection_rouge == 0) and (place [1][0] == -1) :
            cercle4_1 = canvas.create_oval(X, 3 * Y, X, 3 * Y, fill = "yellow", outline = "yellow", width=25)
            selection_rouge = 1
            selection_bleu = 0
            pion_selectionne = 4
            selection = 1

    if (50 <= event.x <= 150) and (50 <= event.y <= 150) and (place [0][0] == 0) and (pion_selectionne == 4):
        if place [1][0] == 1 :
            couleurs = "blue"
            color = 1
        if place [1][0] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle4, cercle4_1)
        cercle1 = canvas.create_oval(X, Y, X, Y, fill=couleurs, outline=couleurs, width=20)
        place [1][0] = 0
        place [0][0] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
        

    if (250 <= event.x <= 350) and (250 <= event.y <= 350) and (place [1][1] == 0) and (pion_selectionne == 4):
        if place [1][0] == 1 :
            couleurs = "blue"
            color = 1
        if place [1][0] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle4, cercle4_1)
        cercle5 = canvas.create_oval(3 * X, 3 * Y, 3 * X, 3 * Y, fill=couleurs, outline=couleurs, width=20)
        place [1][0] = 0
        place [1][1] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
        

    if (50 <= event.x <= 150) and (450 <= event.y <= 550) and (place [2][0] == 0) and (pion_selectionne == 4):
        if place [1][0] == 1 :
            couleurs = "blue"
            color = 1
        if place [1][0] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle4, cercle4_1)
        cercle7 = canvas.create_oval(X, 5 * Y, X, 5 * Y, fill=couleurs, outline=couleurs, width=20)
        place [1][0] = 0
        place [2][0] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
        

### place 5

    if (250 <= event.x <= 350) and (250 <= event.y <= 350) and (nombre_de_jetons > 6) and (place [1][1] != 0) and (selection == 0):
        if (selection_bleu == 0) and (place [1][1] == 1) :
            cercle5_1 = canvas.create_oval(3 * X, 3 * Y, 3 * X, 3 * Y, fill = "yellow", outline = "yellow", width=25)
            selection_bleu = 1
            selection_rouge = 0
            pion_selectionne = 5
            selection = 1
        if (selection_rouge == 0) and (place [1][1] == -1) :
            cercle5_1 = canvas.create_oval(3 * X, 3 * Y, 3 * X, 3 * Y, fill = "yellow", outline = "yellow", width=25)
            selection_rouge = 1
            selection_bleu = 0
            pion_selectionne = 5
            selection = 1

    if (50 <= event.x <= 150) and (50 <= event.y <= 150) and (place [0][0] == 0) and (pion_selectionne == 5):
        if place [1][1] == 1 :
            couleurs = "blue"
            color = 1
        if place [1][1] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle5, cercle5_1)
        cercle1 = canvas.create_oval(X, Y, X, Y, fill=couleurs, outline=couleurs, width=20)
        place [1][1] = 0
        place [0][0] = color
        selection = 0
        victoire ()
        draw()
        gagne ()

    if (250 <= event.x <= 350) and (50 <= event.y <= 150) and (place [0][1] == 0) and (pion_selectionne == 5):
        if place [1][1] == 1 :
            couleurs = "blue"
            color = 1
        if place [1][1] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle5, cercle5_1)
        cercle2 = canvas.create_oval(3 * X, Y, 3 * X, Y, fill=couleurs, outline=couleurs, width=20)
        place [1][1] = 0
        place [0][1] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
        

    if (450 <= event.x <= 550) and (50 <= event.y <= 150) and (place [0][2] == 0) and (pion_selectionne == 5):
        if place [1][1] == 1 :
            couleurs = "blue"
            color = 1
        if place [1][1] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle5, cercle5_1)
        cercle3 = canvas.create_oval(5 * X, Y, 5 * X, Y, fill=couleurs, outline=couleurs, width=20)
        place [1][1] = 0
        place [0][2] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
        

    if (450 <= event.x <= 550) and (250 <= event.y <= 350) and (place [1][2] == 0) and (pion_selectionne == 5):
        if place [1][1] == 1 :
            couleurs = "blue"
            color = 1
        if place [1][1] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle5, cercle5_1)
        cercle6 = canvas.create_oval(5 * X, 3 * Y, 5 * X, 3 * Y, fill=couleurs, outline=couleurs, width=20)
        place [1][1] = 0
        place [1][2] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
        

    if (450 <= event.x <= 550) and (450 <= event.y <= 550) and (place [2][2] == 0) and (pion_selectionne == 5):
        if place [1][1] == 1 :
            couleurs = "blue"
            color = 1
        if place [1][1] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle5, cercle5_1)
        cercle9 = canvas.create_oval(5 * X, 5 * Y, 5 * X, 5 * Y, fill=couleurs, outline=couleurs, width=20)
        place [1][1] = 0
        place [2][2] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
        

    if (250 <= event.x <= 350) and (450 <= event.y <= 550) and (place [2][1] == 0) and (pion_selectionne == 5):
        if place [1][1] == 1 :
            couleurs = "blue"
            color = 1
        if place [1][1] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle5, cercle5_1)
        cercle8 = canvas.create_oval(3 * X, 5 * Y, 3 * X, 5 * Y, fill=couleurs, outline=couleurs, width=20)
        place [1][1] = 0
        place [2][1] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
        

    if (50 <= event.x <= 150) and (450 <= event.y <= 550) and (place [2][0] == 0) and (pion_selectionne == 5):
        if place [1][1] == 1 :
            couleurs = "blue"
            color = 1
        if place [1][1] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle5, cercle5_1)
        cercle7 = canvas.create_oval(X, 5 * Y, X, 5 * Y, fill=couleurs, outline=couleurs, width=20)
        place [1][1] = 0
        place [2][0] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
        

    if (50 <= event.x <= 150) and (250 <= event.y <= 350) and (place [1][0] == 0) and (pion_selectionne == 5):
        if place [1][1] == 1 :
            couleurs = "blue"
            color = 1
        if place [1][1] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle5, cercle5_1)
        cercle4 = canvas.create_oval(X, 3 * Y, X, 3 * Y, fill=couleurs, outline=couleurs, width=20)
        place [1][1] = 0
        place [1][0] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
        

### place 6

    if (450 <= event.x <= 550) and (250 <= event.y <= 350) and (nombre_de_jetons > 6) and (place [1][2] != 0) and (selection == 0):
        if (selection_bleu == 0) and (place [1][2] == 1) :
            cercle6_1 = canvas.create_oval(5 * X, 3 * Y, 5 * X, 3 * Y, fill = "yellow", outline = "yellow", width=25)
            selection_bleu = 1
            selection_rouge = 0
            pion_selectionne = 6
            selection = 1
        if (selection_rouge == 0) and (place [1][2] == -1) :
            cercle6_1 = canvas.create_oval(5 * X, 3 * Y, 5 * X, 3 * Y, fill = "yellow", outline = "yellow", width=25)
            selection_rouge = 1
            selection_bleu = 0
            pion_selectionne = 6
            selection = 1

    if (450 <= event.x <= 550) and (50 <= event.y <= 150) and (place [0][2] == 0) and (pion_selectionne == 6):
        if place [1][2] == 1 :
            couleurs = "blue"
            color = 1
        if place [1][2] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle6, cercle6_1)
        cercle3 = canvas.create_oval(5 * X, Y, 5 * X, Y, fill=couleurs, outline=couleurs, width=20)
        place [1][2] = 0
        place [0][2] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
        

    if (250 <= event.x <= 350) and (250 <= event.y <= 350) and (place [1][1] == 0) and (pion_selectionne == 6):
        if place [1][2] == 1 :
            couleurs = "blue"
            color = 1
        if place [1][2] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle6, cercle6_1)
        cercle5 = canvas.create_oval(3 * X, 3 * Y, 3 * X, 3 * Y, fill=couleurs, outline=couleurs, width=20)
        place [1][2] = 0
        place [1][1] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
        

    if (450 <= event.x <= 550) and (450 <= event.y <= 550) and (place [2][2] == 0) and (pion_selectionne == 6):
        if place [1][2] == 1 :
            couleurs = "blue"
            color = 1
        if place [1][2] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle6, cercle6_1)
        cercle9 = canvas.create_oval(5 * X, 5 * Y, 5 * X, 5 * Y, fill=couleurs, outline=couleurs, width=20)
        place [1][2] = 0
        place [2][2] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
        

### place 7

    if (50 <= event.x <= 150) and (450 <= event.y <= 550) and (nombre_de_jetons > 6) and (place [2][0] != 0) and (selection == 0):
        if (selection_bleu == 0) and (place [2][0] == 1) :
            cercle7_1 = canvas.create_oval(X, 5 * Y, X, 5 * Y, fill = "yellow", outline = "yellow", width=25)
            selection_bleu = 1
            selection_rouge = 0
            pion_selectionne = 7
            selection = 1
        if (selection_rouge == 0) and (place [2][0] == -1) :
            cercle7_1 = canvas.create_oval(X, 5 * Y, X, 5 * Y, fill = "yellow", outline = "yellow", width=25)
            selection_rouge = 1
            selection_bleu = 0
            pion_selectionne = 7
            selection = 1

    if (50 <= event.x <= 150) and (250 <= event.y <= 350) and (place [1][0] == 0) and (pion_selectionne == 7):
        if place [2][0] == 1 :
            couleurs = "blue"
            color = 1
        if place [2][0] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle7, cercle7_1)
        cercle4 = canvas.create_oval(X, 3 * Y, X, 3 * Y, fill=couleurs, outline=couleurs, width=20)
        place [2][0] = 0
        place [1][0] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
        

    if (50 <= event.x <= 150) and (250 <= event.y <= 350) and (place [1][1] == 0) and (pion_selectionne == 7):
        if place [2][0] == 1 :
            couleurs = "blue"
            color = 1
        if place [2][0] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle7, cercle7_1)
        cercle5 = canvas.create_oval(3 * X, 3 * Y, 3 * X, 3 * Y, fill=couleurs, outline=couleurs, width=20)
        place [2][0] = 0
        place [1][1] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
        

    if (250 <= event.x <= 350) and (450 <= event.y <= 550) and (place [2][1] == 0) and (pion_selectionne == 7):
        if place [2][0] == 1 :
            couleurs = "blue"
            color = 1
        if place [2][0] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle7, cercle7_1)
        cercle8 = canvas.create_oval(3 * X, 5 * Y, 3 * X, 5 * Y, fill=couleurs, outline=couleurs, width=20)
        place [2][0] = 0
        place [2][1] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
        

### place 8

    if (250 <= event.x <= 350) and (450 <= event.y <= 550) and (nombre_de_jetons > 6) and (place [2][1] != 0) and (selection == 0):
        if (selection_bleu == 0) and (place [2][1] == 1) :
            cercle8_1 = canvas.create_oval(3 * X, 5 * Y, 3 * X, 5 * Y, fill = "yellow", outline = "yellow", width=25)
            selection_bleu = 1
            selection_rouge = 0
            pion_selectionne = 8
            selection = 1
        if (selection_rouge == 0) and (place [2][1] == -1) :
            cercle8_1 = canvas.create_oval(3 * X, 5 * Y, 3 * X, 5 * Y, fill = "yellow", outline = "yellow", width=25)
            selection_rouge = 1
            selection_bleu = 0
            pion_selectionne = 8
            selection = 1

    if (50 <= event.x <= 150) and (450 <= event.y <= 550) and (place [2][0] == 0) and (pion_selectionne == 8):
        if place [2][1] == 1 :
            couleurs = "blue"
            color = 1
        if place [2][1] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle8, cercle8_1)
        cercle7 = canvas.create_oval(X, 5 * Y, X, 5 * Y, fill=couleurs, outline=couleurs, width=20)
        place [2][1] = 0
        place [2][0] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
        

    if (250 <= event.x <= 350) and (250 <= event.y <= 350) and (place [1][1] == 0) and (pion_selectionne == 8):
        if place [2][1] == 1 :
            couleurs = "blue"
            color = 1
        if place [2][1] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle8, cercle8_1)
        cercle5 = canvas.create_oval(3 * X, 3 * Y, 3 * X, 3 * Y, fill=couleurs, outline=couleurs, width=20)
        place [2][1] = 0
        place [1][1] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
        

    if (450 <= event.x <= 550) and (450 <= event.y <= 550) and (place [2][1] == 0) and (pion_selectionne == 8):
        if place [2][1] == 1 :
            couleurs = "blue"
            color = 1
        if place [2][1] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle8, cercle8_1)
        cercle9 = canvas.create_oval(5 * X, 5 * Y, 5 * X, 5 * Y, fill=couleurs, outline=couleurs, width=20)
        place [2][1] = 0
        place [2][2] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
        

### place 9

    if (450 <= event.x <= 550) and (450 <= event.y <= 550) and (nombre_de_jetons > 6) and (place [2][2] != 0) and (selection == 0):
        if (selection_bleu == 0) and (place [2][2] == 1) :
            cercle9_1 = canvas.create_oval(5 * X, 5 * Y, 5 * X, 5 * Y, fill = "yellow", outline = "yellow", width=25)
            selection_bleu = 1
            selection_rouge = 0
            pion_selectionne = 9
            selection = 1
        if (selection_rouge == 0) and (place [2][2] == -1) :
            cercle9_1 = canvas.create_oval(5 * X, 5 * Y, 5 * X, 5 * Y, fill = "yellow", outline = "yellow", width=25)
            selection_rouge = 1
            selection_bleu = 0
            pion_selectionne = 9
            selection = 1

    if (250 <= event.x <= 350) and (450 <= event.y <= 550) and (place [2][1] == 0) and (pion_selectionne == 9):
        if place [2][2] == 1 :
            couleurs = "blue"
            color = 1
        if place [2][2] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle9, cercle9_1)
        cercle8 = canvas.create_oval(3 * X, 5 * Y, 3 * X, 5 * Y, fill=couleurs, outline=couleurs, width=20)
        place [2][2] = 0
        place [2][1] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
        

    if (250 <= event.x <= 350) and (250 <= event.y <= 350) and (place [1][1] == 0) and (pion_selectionne == 9):
        if place [2][2] == 1 :
            couleurs = "blue"
            color = 1
        if place [2][2] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle9, cercle9_1)
        cercle5 = canvas.create_oval(3 * X, 3 * Y, 3 * X, 3 * Y, fill=couleurs, outline=couleurs, width=20)
        place [2][2] = 0
        place [1][1] = color
        selection = 0
        victoire ()
        draw()
        gagne ()
        

    if (450 <= event.x <= 550) and (250 <= event.y <= 350) and (place [1][2] == 0) and (pion_selectionne == 9):
        if place [2][2] == 1 :
            couleurs = "blue"
            color = 1
        if place [2][2] == -1 :
            couleurs = "red"   
            color = -1
        canvas.delete (cercle9, cercle9_1)
        cercle6 = canvas.create_oval(5 * X, 3 * Y, 5 * X, 3 * Y, fill=couleurs, outline=couleurs, width=20)
        place [2][2] = 0
        place [1][2] = color
        selection = 0
        victoire ()
        draw()
        gagne ()


def phase_deux () :
    global nombre_de_jetons
    suite.destroy()
    nombre_de_jetons += 1

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
    """cette fonction detecte si 3 pions sont allignés"""
    global win, victoire_bleu, victoire_rouge, victoire_partie
    if win == 1 :
        print ("Victoire des Bleu")
        victoire_bleu += 1
        compteur_victoire_bleu['text'] = str(victoire_bleu)
        recommencer()
        if victoire_bleu == 3 :
            compteur_victoire_bleu['text'] = "win"
            texte_bleu = "Victoire des bleus (Cliquez pour recommencer)"
            victoire_partie = tk.Button(racine,text=texte_bleu, width=40, height=20, command=victoire_partie)
            victoire_partie.grid(row=2, column=2)
    if win == -1 :
        print ("Victoire des Rouges")
        victoire_rouge += 1
        compteur_victoire_rouge['text'] = str(victoire_rouge)
        recommencer()
        if victoire_rouge == 3 :
            compteur_victoire_rouge['text'] = "win"
            texte_rouge = "Victoires des rouges (Cliquez pour recommencer)"
            victoire_partie = tk.Button(racine,text=texte_rouge, width=40, height=20, command=victoire_partie)
            victoire_partie.grid(row=2, column=2)
    if win == 2 :
        print ("Match nul")
        recommencer()
        

def victoire_partie():
    global place, nombre_de_jetons, victoire_partie, victoire_bleu, victoire_rouge
    recommencer()
    victoire_bleu = 0
    compteur_victoire_bleu['text'] = str(victoire_bleu)
    victoire_rouge = 0
    compteur_victoire_rouge['text'] = str(victoire_rouge)
    victoire_partie.destroy()
################ Match nul ###############################################
def draw (): 
    global win
    global Tours
    """verifie si une partie du plateau est égale a zero et si elle l'est alors ajoute un au compteur."""
    if  place[0][0] + place [0][1] + place [0][2]!=3 or place[1][0] + place [1][1] + place [1][2]!=3 or \
        place[2][0] + place [2][1] + place [2][2]!=3 or place[0][0] + place [1][0] + place [2][0]!=3 or \
        place[0][1] + place [1][1] + place [2][1]!=3 or place[0][2] + place [1][2] + place [2][2]!=3 or \
        place[0][0] + place [1][1] + place [2][2]!=3 or place[0][2] + place [1][1] + place [2][0]!=3 :
                    if  place[0][0]==0 and place [0][1]== 0 and place [0][2]==0 or place[1][0]==0 and place [1][1]==0 and place [1][2]==0 or \
                        place[2][0]==0 and place [2][1]==0 and place [2][2]==0 or place[0][0]==0 and place [1][0]==0 and place [2][0]==0 or \
                        place[0][1]==0 and place [1][1]==0 and place [2][1]==0 or place[0][2]==0 and place [1][2]==0 and place [2][2]==0 or \
                        place[0][0]==0 and place [1][1]==0 and place [2][2]==0 or place[0][2]==0 and place [1][1]==0 and place [2][0]==0:
                        Tours+=1
                    elif place[0][0]==0 and place [0][1]== 0 and place [0][2]==0 or place[1][0]==0 and place [1][1]==0 and place [1][2]==0 or \
                        place[2][0]==0 and place [2][1]==0 and place [2][2]==0 or place[0][0]==0 and place [1][0]==0 and place [2][0]==0 or \
                        place[0][1]==0 and place [1][1]==0 and place [2][1]==0 or place[0][2]==0 and place [1][2]==0 and place [2][2]==0 or \
                        place[0][0]==0 and place [1][1]==0 and place [2][2]==0 or place[0][2]==0 and place [1][1]==0 and place [2][0]==0:
                        Tours+=1
    if Tours == 3 :
        win = 2
    print (Tours)
    return (win)


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
        nombre_de_jetons += 1
    if place [0][0] == -1 :
        cercle1 = canvas.create_oval(X, Y, X, Y, fill = "red", outline = "red", width=20)
        nombre_de_jetons += 1

    if place [0][1] == 1 :
        cercle2 = canvas.create_oval(3 * X, Y, 3 * X, Y, fill="blue", outline="blue", width=20)
        nombre_de_jetons += 1
    if place [0][1] == -1 :
        cercle2 = canvas.create_oval(3 * X, Y, 3 * X, Y, fill="red", outline="red", width=20)
        nombre_de_jetons += 1

    if place [0][2] == 1 :
        cercle3 = canvas.create_oval(5 * X, Y, 5 * X, Y, fill="blue", outline="blue", width=20)
        nombre_de_jetons += 1
    if place [0][2] == -1 :
        cercle3 = canvas.create_oval(5 * X, Y, 5 * X, Y, fill="red", outline="red", width=20)
        nombre_de_jetons += 1

    if place [1][0] == 1 :
        cercle4 = canvas.create_oval(X, 3 * Y, X, 3 * Y, fill="blue", outline="blue", width=20)
        nombre_de_jetons += 1
    if place [1][0] == -1 :
        cercle4 = canvas.create_oval(X, 3 * Y, X, 3 * Y, fill="red", outline="red", width=20)
        nombre_de_jetons += 1

    if place [1][1] == 1 :
        cercle5 = canvas.create_oval(3 * X, 3 * Y, 3 * X, 3 * Y, fill="blue", outline="blue", width=20)
        nombre_de_jetons += 1
    if place [1][1] == -1 :
        cercle5 = canvas.create_oval(3 * X, 3 * Y, 3 * X, 3 * Y, fill="red", outline="red", width=20)
        nombre_de_jetons += 1

    if place [1][2] == 1 :
        cercle6 = canvas.create_oval(5 * X, 3 * Y, 5 * X, 3 * Y, fill="blue", outline="blue", width=20)
        nombre_de_jetons += 1
    if place [1][2] == -1 :
        cercle6 = canvas.create_oval(5 * X, 3 * Y, 5 * X, 3 * Y, fill="red", outline="red", width=20)
        nombre_de_jetons += 1

    if place [2][0] == 1 :
        cercle7 = canvas.create_oval(X, 5 * Y, X, 5 * Y, fill="blue", outline="blue", width=20)
        nombre_de_jetons += 1
    if place [2][0] == -1 :
        cercle7 = canvas.create_oval(X, 5 * Y, X, 5 * Y, fill="red", outline="red", width=20)
        nombre_de_jetons += 1

    if place [2][1] == 1 :
        cercle8 = canvas.create_oval(3 * X, 5 * Y, 3 * X, 5 * Y, fill="blue", outline="blue", width=20)
        nombre_de_jetons += 1
    if place [2][1] == -1 :
        cercle8 = canvas.create_oval(3 * X, 5 * Y, 3 * X, 5 * Y, fill="red", outline="red", width=20)
        nombre_de_jetons += 1

    if place [2][2] == 1 :
        cercle9 = canvas.create_oval(5 * X, 5 * Y, 5 * X, 5 * Y, fill="blue", outline="blue", width=20)
        nombre_de_jetons += 1
    if place [2][2] == -1 :
        cercle9 = canvas.create_oval(5 * X, 5 * Y, 5 * X, 5 * Y, fill="red", outline="red", width=20)
        nombre_de_jetons += 1
    
    return (place)
            
def recommencer () :
    global place, nombre_de_jetons,Tours
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
    selection_bleu = 0
    selection_rouge = 1
    nombre_de_jetons = 0
    selection_bleu = 0
    selection_rouge = 1
    Tours = 0
    place = [[0,0,0],[0,0,0],[0,0,0]]



canvas = tk.Canvas(racine, width=600, height=600, bg='black')
arreter = tk.Button(racine, text='Arrêter', bg='grey', command=arreter)
sauvegarde = tk.Button(racine, text= "Sauvegarder", bg = "grey", command=sauvegarder)
charger = tk.Button(racine, text= "Charger", bg = "grey", command=charger)
restart = tk.Button(racine, text = "recommencer", bg = "grey", command = recommencer)

canvas.bind('<Button-1>', clique)

############ PLATEAU #################
carre = canvas.create_rectangle(X, Y, 600 - X, 600 - Y, outline='white')
ligne_verticale = canvas.create_line(3 * X, Y, 3 * X, 5 * Y, fill='white')
ligne_horizontale = canvas.create_line(X, 3 * Y, 5 * X, 3 * Y, fill='white')
diagonale1 = canvas.create_line(X, Y, 5 * X, 5 * Y, fill='white')
diagonale2 = canvas.create_line(X, 5 * Y, 5 * X, Y, fill='white')

canvas.grid(row=0, column=0, columnspan=4, rowspan=6)
arreter.grid(row=6, column=4)
sauvegarde.grid(row=6, column=2)
charger.grid(row=6, column=1)
restart.grid(row=6, column=3)

# Compteur affichant les manches gagnées par les deux équipes
compteur_victoire_bleu = tk.Label(racine, text=0, font=("Arial", 42), fg='blue')
compteur_victoire_bleu.grid (row=2,column=4)
compteur_victoire_rouge = tk.Label(racine, text=0, font=("Arial", 42), fg='red')
compteur_victoire_rouge.grid (row=3,column=4)

#cela sert juste a créer un espace a droite du canvas de base
espace = tk.Canvas(racine,width=200, height=1, bg='white')
espace.grid (column=4)

racine.mainloop()
