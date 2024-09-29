from jeu.model.Type_case import TypeCase


# Classe Terrain qui va représenter mon terrain de jeu
class Plateau:
    def __init__(self, _taillelargeur, _taillehauteur):
        self.largeur = _taillelargeur
        self.hauteur = _taillehauteur
        # Initialiser la grille avec l'élément par défaut VIDE
        self.grille = [[TypeCase.VIDE for _ in range(self.largeur)] for _ in range(self.hauteur)]

    def getLargeur(self):
        return self.largeur

    def setLargeur(self, _largeur):
        self.largeur = _largeur
        self.grille = [[TypeCase.VIDE for _ in range(self.largeur)] for _ in range(self.hauteur)]

    def getHauteur(self):
        return self.hauteur

    def setHauteur(self, _hauteur):
        self.hauteur = _hauteur
        self.grille = [[TypeCase.VIDE for _ in range(self.largeur)] for _ in range(self.hauteur)]

    def getGrille(self):
        grille_str = ""
        for i in range(self.hauteur):
            for j in range(self.largeur):
                grille_str += str(self.grille[i][j].value)  # Convertir l'int en str
            grille_str += "\n"
        return grille_str
