#########################################
# groupe MPCI 2
# Zachary MARIANI
# Jeremy ZORIC
# Baptiste PARIS
# Mohamed AKARKACH
# Pascal CHRISTOPHE
# El guehoudi Wacil

# https://github.com/uvsq22004748/Projet-incendie
#########################################

# On importe tkinter

import tkinter as tk

racine = tk.Tk()

X = 100
Y = 100
COLORS = ['blue', 'red']
nombre_de_jetons = 0

# cette liste evolue en meme temps que le plateau mais elle est interpretable par l'interpreteur python 

place = [[0,0,0],[0,0,0],[0,0,0]]



def lancement():
    ''' On definit une fonction qui va permettre de lancer le schéma du jeu du tapatan '''
    carre = canvas.create_rectangle(X, Y, 600 - X, 600 - Y, outline='white')
    ligne_verticale = canvas.create_line(3 * X, Y, 3 * X, 5 * Y, fill='white')
    ligne_horizontale = canvas.create_line(X, 3 * Y, 5 * X, 3 * Y, fill='white')
    diagonale1 = canvas.create_line(X, Y, 5 * X, 5 * Y, fill='white')
    diagonale2 = canvas.create_line(X, 5 * Y, 5 * X, Y, fill='white')


##################### PLACEMENT DES JETONS AU DEBUT DE LA PARTIE #####################

def clique(event):

    ''' Cette fonction va permettre de générer les jetons sur le schéma du jeu '''

    global nombre_de_jetons
    global couleur
    if nombre_de_jetons % 2 == 0 :
        couleur = 'blue'
        pion = 1
    elif nombre_de_jetons % 2 == 1 :
        couleur = 'red'
        pion = -1
    couleurs = couleur

    """ cette partie de la fonction permet de placer les jetons en fonction de l'endroit ou l'on clique, il 
        n'est pas possible de placer un jeton au dessus d'un autre """

    if (50 <= event.x <= 150) and (50 <= event.y <= 150) and (nombre_de_jetons <= 5):

        if place [0][0] == 0 :
            cercle1 = canvas.create_oval(X, Y, X, Y, fill = couleurs, outline = couleurs, width=20)
            nombre_de_jetons += 1
            place [0][0] = pion
        victoire ()
        gagne ()

    if (250 <= event.x <= 350) and (50 <= event.y <= 150) and (nombre_de_jetons <= 5):
        
        if place [0][1] == 0 :
            cercle2 = canvas.create_oval(3 * X, Y, 3 * X, Y, fill=couleurs, outline=couleurs, width=20)
            nombre_de_jetons += 1
            place [0][1] = pion
        victoire ()
        gagne ()

    if (450 <= event.x <= 550) and (50 <= event.y <= 150) and (nombre_de_jetons <= 5):
        
        if place [0][2] == 0 :
            cercle3 = canvas.create_oval(5 * X, Y, 5 * X, Y, fill=couleurs, outline=couleurs, width=20)
            nombre_de_jetons += 1
            place [0][2] = pion
        victoire ()
        gagne ()

    if (50 <= event.x <= 150) and (250 <= event.y <= 350) and (nombre_de_jetons <= 5):
        
        if place [1][0] == 0 :
            cercle4 = canvas.create_oval(X, 3 * Y, X, 3 * Y, fill=couleurs, outline=couleurs, width=20)
            nombre_de_jetons += 1
            place [1][0] = pion
        victoire ()
        gagne ()

    if (250 <= event.x <= 350) and (250 <= event.y <= 350) and (nombre_de_jetons <= 5):
        
        if place [1][1] == 0 :
            cercle5 = canvas.create_oval(3 * X, 3 * Y, 3 * X, 3 * Y, fill=couleurs, outline=couleurs, width=20)
            nombre_de_jetons += 1
            place [1][1] = pion
        victoire ()
        gagne ()

    if (450 <= event.x <= 550) and (250 <= event.y <= 350) and (nombre_de_jetons <= 5):
        
        if place [1][2] == 0 :
            cercle6 = canvas.create_oval(5 * X, 3 * Y, 5 * X, 3 * Y, fill=couleurs, outline=couleurs, width=20)
            nombre_de_jetons += 1
            place [1][2] = pion
        victoire ()
        gagne ()

    if (50 <= event.x <= 150) and (450 <= event.y <= 550) and (nombre_de_jetons <= 5):
        
        if place [2][0] == 0 :
            cercle7 = canvas.create_oval(X, 5 * Y, X, 5 * Y, fill=couleurs, outline=couleurs, width=20)
            nombre_de_jetons += 1
            place [2][0] = pion
        victoire ()
        gagne ()

    if (250 <= event.x <= 350) and (450 <= event.y <= 550) and (nombre_de_jetons <= 5):
        
        if place [2][1] == 0 :
            cercle8 = canvas.create_oval(3 * X, 5 * Y, 3 * X, 5 * Y, fill=couleurs, outline=couleurs, width=20)
            nombre_de_jetons += 1
            place [2][1] = pion
        victoire ()
        gagne ()

    if (450 <= event.x <= 550) and (450 <= event.y <= 550) and (nombre_de_jetons <= 5):
        
        if place [2][2] == 0 :
            cercle9 = canvas.create_oval(5 * X, 5 * Y, 5 * X, 5 * Y, fill=couleurs, outline=couleurs, width=20)
            nombre_de_jetons += 1
            place [2][2] = pion
        victoire ()
        gagne ()

    print (place) 


################# VICTOIRE ##################

def victoire (): 
    global win
    win = 0
    if place[0][0] + place [0][1] + place [0][2]==3 :
        win += 1   
    if place[1][0] + place [1][1] + place [1][2]==3 :
        win += 1   
    if place[2][0] + place [2][1] + place [2][2]==3 :
        win += 1    
    if place[0][0] + place [1][0] + place [2][0]==3 :
        win += 1       
    if place[0][1] + place [1][1] + place [2][1]==3 :
        win += 1        
    if place[0][2] + place [1][2] + place [2][2]==3 :
        win += 1        
    if place[0][0] + place [1][1] + place [2][2]==3 :
        win += 1        
    if place[0][2] + place [1][1] + place [2][0]==3 :
        win += 1

    if place[0][0] + place [0][1] + place [0][2]==-3 :
        win -= 1   
    if place[1][0] + place [1][1] + place [1][2]==-3 :
        win -= 1   
    if place[2][0] + place [2][1] + place [2][2]==-3 :
        win -= 1    
    if place[0][0] + place [1][0] + place [2][0]==-3 :
        win -= 1       
    if place[0][1] + place [1][1] + place [2][1]==-3 :
        win -= 1        
    if place[0][2] + place [1][2] + place [2][2]==-3 :
        win -= 1        
    if place[0][0] + place [1][1] + place [2][2]==-3 :
        win -= 1        
    if place[0][2] + place [1][1] + place [2][0]==-3 :
        win -= 1
    return (win)        

def gagne () : 
    """cette fonction detect si 3 pions sont allignés"""
    global win
    if win == 1 :
        print ("Victoire des Bleu")
        blue_win = tk.Canvas (racine, width=150, height=50, bg='blue')
        blue_win.grid(row = 0, column = 3)
    if win == -1 :
        print ("Victoire des Rouges")
        red_win = tk.Canvas (racine, width=150, height=50, bg='red')
        red_win.grid(row = 0, column = 3)


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


def arreter():
    ''' Cette fonction va arreter le programme en cours '''
    racine.destroy()


canvas = tk.Canvas(racine, width=600, height=600, bg='black')
lancement = tk.Button(racine, text='Lancement', bg='grey', command=lancement)
arreter = tk.Button(racine, text='Arrêter', bg='grey', command=arreter)
canvas.bind('<Button-1>', clique)

canvas.grid(row=0, column=0, columnspan=3)
lancement.grid(row=1, column=0)
arreter.grid(row=1, column=2)


racine.mainloop()
