# Projet_Tapatan
# Jeremy ZORIC
# Zachary MARIANI

Projet d'IN200 Jeu tapatan

Projet de jeu de Tapatan codé en python 3 :

Ce projet a été réalisé par Jeremy ZORIC et Zachary MARIANI exclusivement, les autres membres du groupe n'ayant à aucun moment participé à aucune modification
ou réflexion autour de ce projet, c'est pourquoi le projet peut comporter des bugs, qui restent néanmoins très rares, ou tout simplement des fonctionnalités manquantes.

Déroulement du jeu :

Lors du début de la partie, les deux joueurs placent tour à tour leurs pions sur le plateau, chaque joueur peut placer 3 pions.
Une fois que tous les pions ont été placés, l'alternance des tours se poursuit mais les joueurs doivent déplacer les pions sur le plateau, pour cela il faut cliquer 
sur le pion à déplacer puis cliquer sur l'emplacement sur lequel on veut déplacer le pion sélectionné.
Lorsqu'un joueur a aligné 3 pions, il marque un point. La partie s'arrête lorsqu'un joueur a marqué 3 points.

Vous avez la possibilité de sauvegarder la partie dans un fichier externe et de la recharger à n'importe quel moment.
Attention à ne sauvegarder que lorsqu'aucun pion n'est sélectionné car cela peut occasionner des bugs.
L'intelligence artificielle n'est pas encore prête et par conséquent ne sera pas intégrée.

Le bouton "recommencer" efface tous les pions du plateau et recommence la manche mais ne réinitialise pas le compteur de points. Cependant, lorsqu'un joueur gagne les 3 manches, c'est-à-dire la partie, une fenêtre apparaît et permet de réinitialiser complètement la partie (score ainsi que position des pions).

Composition de la fenêtre :

En résumé, le programme se compose d'une fenêtre affichant la disposition du jeu du tapatan. La possibilité de mettre six jetons sur ce même jeu ( trois de couleur bleue et trois de couleur rouge). A la droite de ce jeu vous pourrez trouver deux compteurs bleu et rouge affichant le score de chacun des joueurs. Lorsqu'un des joueurs arrive à trois manches gagnées, le compteur affiche win et une fenêtre pour redémarrer se lance. Notre jeu dispose aussi de quatre boutons. Le premier sert à charger un fichier déjà créé, le deuxième sert à sauvegarder la partie en cours, le troisième permet de recommencer la manche en cours sans remplacer les scores et le dernier permet d'arrêter complètement le jeu (fermeture de la fenêtre de jeu).

ATTENTION : par manque de temps et de moyens du fait que ce projet n'a été réalise que par deux personnes, il n'est pas encore possible de désélectionner un pion,
c'est pourquoi il faut faire attention à ne sélectionner que des pions qui ont la possibilité de se déplacer sinon le jeu est bloqué et il faut le relancer. De plus, l'IA n'a pas été ajouté car elle n'était pas terminée et ne marchait donc pas correctement.
