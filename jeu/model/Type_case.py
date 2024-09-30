from enum import Enum


# Définir l'énumération pour les types d'éléments dans la grille
class TypeCase(Enum):
    VIDE = 0
    MAISON = 1
    ROUTE = 2
    MAGASIN = 3
