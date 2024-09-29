import pygame
import time
from jeu.model.Type_case import TypeCase


class View:
    def __init__(self, width, height, controller):
        self.width = width
        self.height = height
        self.cell_size = 100
        self.sidebar_width = 300  # Largeur de la bande blanche
        self.controller = controller  # Le contrôleur est passé en paramètre

        pygame.init()
        self.screen = pygame.display.set_mode((self.width + self.sidebar_width, self.height))
        pygame.display.set_caption("Affichage du Plateau")
        self.clock = pygame.time.Clock()
        self.temps_avant_changement=0

        # Chargement des images
        self.images = {
            TypeCase.VIDE: pygame.image.load('jeu/assets/carre_noir.png'),
            TypeCase.MAISON: pygame.image.load('jeu/assets/house_image.png'),
            TypeCase.ROUTE: pygame.image.load('jeu/assets/road_image.png')
        }

        # Initialisation du texte
        self.font = pygame.font.Font(None, 36)

    def draw_plateau(self, grille):
        for i, row in enumerate(grille):
            for j, value in enumerate(row):
                image = self.get_image(value)
                self.screen.blit(image, (j * self.cell_size, i * self.cell_size))

    def draw_sidebar(self, argent):
        # Dessiner la bande blanche à droite
        pygame.draw.rect(self.screen, (255, 255, 255), (self.width, 0, self.sidebar_width, self.height))


        # Afficher les textes de jeu
        self.font = pygame.font.Font(None, 36)
        argent_text = self.font.render(f"Argent: {argent}", True, (0, 0, 0))
        self.screen.blit(argent_text, (self.width + 20, 20))  # Affiche le texte dans la bande blanche
        self.font = pygame.font.Font(None, 20)
        temps_text = self.font.render(f"Temps avant changement: {int(4-self.temps_avant_changement)}", True, (0, 0, 0))
        self.screen.blit(temps_text, (self.width + 20, 60))  # Affiche le texte dans la bande blanche

    def get_image(self, value):
        return self.images.get(value, self.images[TypeCase.VIDE])

    def handle_click(self, grille):
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] < self.width:  # Vérifier si le clic est sur le plateau et non dans la bande blanche
            x = mouse_pos[0] // self.cell_size
            y = mouse_pos[1] // self.cell_size
            self.controller.on_case_click_grille(x, y)

    def view_run(self, grille, argent):
        running = True
        last_update_time = time.time()  # Initialiser le temps de la dernière mise à jour
        update_interval = 3  # Intervalle de mise à jour en secondes

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:  # Gérer les clics de souris
                    self.handle_click(grille)

            current_time = time.time()
            if current_time - last_update_time >= update_interval:
                self.controller.mise_a_jour_reguliere_grille()
                print("on met à jour la carte")
                last_update_time = current_time  # Mettre à jour le temps de la dernière mise à jour

            self.screen.fill((0, 0, 0))
            self.draw_plateau(grille)  # Dessiner le plateau
            self.temps_avant_changement=current_time - last_update_time
            self.draw_sidebar(self.controller.getArgentjoueur())  # Dessiner la bande blanche et l'argent
            self.clock.tick(60)
            pygame.display.flip()

        pygame.quit()

