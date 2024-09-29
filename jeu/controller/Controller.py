from jeu.model.Plateau import Plateau
from jeu.view.View import View
from jeu.model.Type_case import TypeCase
from jeu.model.Joueur import Joueur
import pygame

class Controller:
    def __init__(self, largeur_fenetre_voulue, hauteur_fenetre_voulue):
        self.view = View(largeur_fenetre_voulue, hauteur_fenetre_voulue, self)
        self.plateau = Plateau(int(largeur_fenetre_voulue / 100), int(hauteur_fenetre_voulue / 100))
        self.joueur = Joueur(1000)
        self.nombre_modif=0


        self.plateau.setthiscase(4, 7, TypeCase.MAISON)
        self.joueur.ajouter_dette(self.plateau.valeur_dette_maison)
        self.plateau.setthiscase(1, 3, TypeCase.ROUTE)


    def getArgentjoueur(self):
        return self.joueur.getArgent()

    def controller_run(self):
            self.view.view_run(self.plateau.getGrille(), self.joueur.getArgent())

    def on_case_click_grille(self, x, y):
        print(f"Case cliquée : ({x}, {y})")
        if(self.plateau.mise_a_jour_case(x, y, self.joueur)):
            #print("Case mise à jour")
            self.nombre_modif+=1

    def get_last_update_grille(self):
        return self.plateau.getlast_update_time()

    def mise_a_jour_reguliere_grille(self):
        self.plateau.mise_a_jour_reguliere_grille()
        self.joueur.mise_a_jour_reguliere_joueur()


