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

# creation et placement du pemier canevas qui sera le plateau de jeu

CANVAS = tk.Canvas(root, width=400, height=400, bg="light grey")
CANVAS.grid(row=0, rowspan=3, column=0, columnspan=2)

# creation d'un autre canvas qui permettra d'afficher le score 

SCORE = tk.Canvas(root, width=100, height=200, bg="darkgrey")
SCORE.grid(row=1, column=2)
SCORE.create_line(0, 100, 100, 100, fill="black", width=2)

# Dessin du plateau de jeu 
"""chaque ligne est en deux parties pour faciliter le calcul des coordonnées
lors des deplacement des pions sur le plateau"""

"""la couleur sera amenée a etre changée"""

CANVAS.create_line(20, 20, 200, 20, fill= 'orange', width=2)
CANVAS.create_line(200, 20, 380, 20, fill= 'orange', width=2)

CANVAS.create_line(20, 380, 380, 380, fill= 'orange', width=2)
CANVAS.create_line(20, 380, 380, 380, fill= 'orange', width=2)

CANVAS.create_line(20, 20, 20, 200, fill= 'orange', width=2)
CANVAS.create_line(20, 200, 20, 380, fill= 'orange', width=2)

CANVAS.create_line(20, 20, 200, 200, fill= 'orange', width=2)
CANVAS.create_line(200, 200, 380, 380, fill= 'orange', width=2)

CANVAS.create_line(20, 380, 200, 200, fill= 'orange', width=2)
CANVAS.create_line(200, 200, 380, 20, fill= 'orange', width=2)

CANVAS.create_line(380, 20, 380, 200, fill= 'orange', width=2)
CANVAS.create_line(380, 200, 380, 380, fill= 'orange', width=2)

CANVAS.create_line(200, 20, 200, 200, fill= 'orange', width=2)
CANVAS.create_line(200, 200, 200, 380, fill= 'orange', width=2)

CANVAS.create_line(20, 200, 200, 200, fill= 'orange', width=2)
CANVAS.create_line(200, 200, 380, 200, fill= 'orange', width=2)


# fonctions

def fermer_fenetre (): 
    """cette fonction est reliée au bouton qui arrete le programme, elle ferme tout simplement la fenetre"""
    root.destroy()


# création des differents boutons 

DEMARER = tk.Button(root, text="Démarer / Recommencer", bg="grey")
DEMARER.grid (row=3, column=0)
ARRETER = tk.Button(root, text="Arrêter", bg="grey", command=fermer_fenetre)
ARRETER.grid (row=3, column=1)

root.mainloop()
