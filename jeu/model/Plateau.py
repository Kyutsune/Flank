from jeu.model.Type_case import TypeCase
import time


# Classe Terrain qui va représenter mon terrain de jeu
class Plateau:
    def __init__(self, _taillelargeur, _taillehauteur):
        self.largeur = _taillelargeur
        self.hauteur = _taillehauteur
        # Initialiser la grille avec l'élément par défaut VIDE
        self.grille = [[TypeCase.VIDE for _ in range(self.largeur)] for _ in range(self.hauteur)]
        self.last_update_time = time.time()  # Temps de la dernière mise à jour
        self.update_interval = 5  # Intervalle en secondes pour appeler une fonction

        self.valeur_maison = 100
        self.valeur_dette_maison=50

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

    def Affiche_Grille(self):
        grille_str = ""
        for i in range(self.hauteur):
            for j in range(self.largeur):
                grille_str += str(self.grille[i][j].value)  # Convertir l'int en str
            grille_str += "\n"
        return grille_str

    def getGrille(self):
        return self.grille

    def getthiscase(self, x, y):
        return self.grille[x][y]

    def getvaleurmaison(self):
        return self.valeur_maison

    def setvaleurmaison(self, _valeur):
        self.valeur_maison = _valeur

    def getvaleur_dette_maison(self):
        return self.valeur_dette_maison

    def setvaleur_dette_maison(self, _valeur):
        self.valeur_dette_maison = _valeur

    def setthiscase(self, x, y, value):
        self.grille[x][y] = value

    # Fonction pour mettre à jour une case de la grille en fonction de l'argent du joueur passé en paramètre
    def mise_a_jour_case(self, x, y, joueur):
        if self.grille[y][x] == TypeCase.VIDE:
            if joueur.getArgent() >= self.valeur_maison:
                self.grille[y][x] = TypeCase.MAISON
                joueur.achat_maison(-self.valeur_maison,self.valeur_dette_maison)
                return True
        return False

    # Fonction pour mettre à jour la grille en fonction du temps
    def mise_a_jour_reguliere_grille(self):
        self.last_update_time = time.time()

    def getlast_update_time(self):
        return self.last_update_time
