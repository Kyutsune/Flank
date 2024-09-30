class Joueur:
    def __init__(self, _argent):
        self.argent = _argent
        self.dette = 0

    def getArgent(self):
        return self.argent
    def getDette(self):
        return self.dette

    def ajouter_argent(self, _argent):
        self.argent += _argent

    def ajouter_dette(self, _dette):
        self.dette += _dette

    def achat_maison(self,_argent,_dette):
        self.ajouter_argent(_argent)
        self.ajouter_dette(_dette)

    def mise_a_jour_reguliere_joueur(self, grille):
        self.ajouter_argent(-self.dette)
        self.ajouter_argent(grille.calcul_rente_grille())

