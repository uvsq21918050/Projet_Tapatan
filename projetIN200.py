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

# on importe tkinter

import tkinter as tk 

# creation de la fenetre de base

root = tk.Tk()

# creation et placemebt du pemier canevas qui sera le plateau de jeu

CANVAS = tk.Canvas(root, width=400, height=400, bg="light grey")
CANVAS.grid(row=0, rowspan=2, column=0, columnspan=2)

# Dessin du plateau de jeu 

CANVAS.create_line(20, 20, 200, 20, fill= 'yellow', width=2)
CANVAS.create_line(200, 20, 380, 20, fill= 'yellow', width=2)

CANVAS.create_line(20, 380, 380, 380, fill= 'blue', width=2)
CANVAS.create_line(20, 380, 380, 380, fill= 'blue', width=2)

CANVAS.create_line(20, 20, 20, 200, fill= 'red', width=2)
CANVAS.create_line(20, 200, 20, 380, fill= 'red', width=2)

CANVAS.create_line(20, 20, 200, 200, fill= 'green', width=2)
CANVAS.create_line(200, 200, 380, 380, fill= 'green', width=2)

CANVAS.create_line(20, 380, 200, 200, fill= 'sky blue', width=2)
CANVAS.create_line(200, 200, 380, 20, fill= 'sky blue', width=2)

CANVAS.create_line(380, 20, 380, 200, fill= 'violet', width=2)
CANVAS.create_line(380, 200, 380, 380, fill= 'violet', width=2)

CANVAS.create_line(200, 20, 200, 200, fill= 'Turquoise', width=2)
CANVAS.create_line(200, 200, 200, 380, fill= 'Turquoise', width=2)

CANVAS.create_line(20, 200, 200, 200, fill= 'orange', width=2)
CANVAS.create_line(200, 200, 380, 200, fill= 'orange', width=2)



# fonctions

def fermer_fenetre (): 
    """cette fonction est reliée au bouton qui arrete le programme, elle ferme tout simplement la fenetre"""
    root.destroy()


# création des differents boutons 

DEMARER = tk.Button(root, text="Démarer / Recommencer", bg="grey")
DEMARER.grid (row=2, column=0)
ARRETER = tk.Button(root, text="Arrêter", bg="grey", command=fermer_fenetre)
ARRETER.grid (row=2, column=1)

root.mainloop()