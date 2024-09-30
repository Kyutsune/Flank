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

        #Idéalement on devrait placer toutes ses informations dans une classe à part voir une classe par type de constructions
        self.valeur_maison = 100
        self.valeur_dette_maison=50
        self.valeur_magasin=300
        self.cout_entretient_route=10

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

    def getvaleur_magasin(self):
        return self.valeur_magasin

    def getCoutEntretientRoute(self):
        return self.cout_entretient_route

    def setvaleur_magasin(self, _valeur):
        self.valeur_magasin = _valeur

    def setvaleur_dette_maison(self, _valeur):
        self.valeur_dette_maison = _valeur

    def setthiscase(self, x, y, value):
        self.grille[x][y] = value

    # Fonction pour mettre à jour une case de la grille en fonction de l'argent du joueur passé en paramètre
    def mise_a_jour_case(self, x, y, joueur, type_case):
        if self.grille[y][x] == TypeCase.VIDE:
            if joueur.getArgent() >= self.valeur_maison and type_case == TypeCase.MAISON:
                self.grille[y][x] = TypeCase.MAISON
                joueur.achat_maison(-self.valeur_maison,self.valeur_dette_maison)
                return True
            if joueur.getArgent() >= 10 and type_case == TypeCase.ROUTE: #on dit que le prix d'une route est de 10 pour l'instant
                self.grille[y][x] = TypeCase.ROUTE
                joueur.ajouter_argent(-10)
                return True
            if joueur.getArgent() >= self.valeur_magasin and type_case == TypeCase.MAGASIN:
                self.grille[y][x] = TypeCase.MAGASIN
                joueur.ajouter_argent(-self.valeur_magasin)
                return True
        return False

    # Fonction pour mettre à jour la grille en fonction du temps
    def mise_a_jour_reguliere_grille(self):
        self.last_update_time = time.time()

    def getlast_update_time(self):
        return self.last_update_time

    def calcul_rente_grille(self):
        rente = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Haut, bas, gauche, droite

        for i in range(self.hauteur):
            for j in range(self.largeur):
                if self.grille[i][j] == TypeCase.MAISON:
                    for direction in directions:
                        ni, nj = i + direction[0], j + direction[1]  # Calcul des coordonnées du voisin
                        if 0 <= ni < self.hauteur and 0 <= nj < self.largeur:
                            if self.grille[ni][nj] == TypeCase.MAGASIN:
                                rente += 60
                if self.grille[i][j] == TypeCase.ROUTE:
                    rente -= self.cout_entretient_route
        return rente

