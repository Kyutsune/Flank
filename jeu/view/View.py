import pygame
import time
from jeu.model.Type_case import TypeCase


class View:
    def __init__(self, width, height, controller):
        self.width = width
        self.height = height
        self.cell_size = 100
        self.sidebar_width = 400  # Largeur de la bande blanche
        self.controller = controller

        pygame.init()
        self.screen = pygame.display.set_mode((self.width + self.sidebar_width, self.height))
        pygame.display.set_caption("Affichage du Plateau")
        self.clock = pygame.time.Clock()
        self.temps_avant_changement = 0
        self.selected_type = controller.getTypeCasePosee()

        # Chargement des images
        self.images = {
            TypeCase.VIDE: pygame.image.load('jeu/assets/carre_noir.png'),
            TypeCase.MAISON: pygame.image.load('jeu/assets/house_image.png'),
            TypeCase.ROUTE: pygame.image.load('jeu/assets/road_image.png'),
            TypeCase.MAGASIN: pygame.image.load('jeu/assets/store_image.png')
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

        # Afficher l'argent
        argent_text = self.font.render(f"Argent: {argent}", True, (0, 0, 0))
        self.screen.blit(argent_text, (self.width + 20, 20))

        # Dessiner les icônes de maison et de route
        maison_pos = (self.width + 20, 300)  # Position de l'icône de maison
        route_pos = (self.width + 125, 300)  # Position de l'icône de route
        magasin_pos = (self.width + 230, 300)  # Position de l'icône de magasin

        # Afficher les icônes et affiche le prix de chaque construction
        self.screen.blit(self.images[TypeCase.MAISON], maison_pos)
        self.font = pygame.font.Font(None, 20)
        temps_text = self.font.render(f"Prix: {int(self.controller.getPrixmaison())}", True, (0, 0, 0))
        self.screen.blit(temps_text, (maison_pos[0], maison_pos[1] + 100))
        self.screen.blit(self.images[TypeCase.ROUTE], route_pos)
        temps_text = self.font.render("Prix: 10", True, (0, 0, 0))
        self.screen.blit(temps_text, (route_pos[0], route_pos[1] + 100))

        self.screen.blit(self.images[TypeCase.MAGASIN], magasin_pos)
        temps_text = self.font.render(f"Prix: {int(self.controller.getValeurMagasin())}", True, (0, 0, 0))
        self.screen.blit(temps_text, (magasin_pos[0], magasin_pos[1] + 100))


        # Surligner l'icône sélectionnée
        if self.selected_type == TypeCase.MAISON:
            pygame.draw.rect(self.screen, (255, 0, 0), (*maison_pos, 100, 100), 5)
        elif self.selected_type == TypeCase.ROUTE:
            pygame.draw.rect(self.screen, (255, 0, 0), (*route_pos, 100, 100), 5)
        elif self.selected_type == TypeCase.MAGASIN:
            pygame.draw.rect(self.screen, (255, 0, 0), (*magasin_pos, 100, 100), 5)

        # Afficher le temps avant changement
        self.font = pygame.font.Font(None, 20)
        temps_text = self.font.render(f"Temps avant changement: {int(4 - self.temps_avant_changement)}", True,
                                      (0, 0, 0))
        self.screen.blit(temps_text, (self.width + 20, 200))

    def get_image(self, value):
        return self.images.get(value, self.images[TypeCase.VIDE])

    def handle_click(self):
        mouse_pos = pygame.mouse.get_pos()

        # Vérifier si le clic est sur le plateau
        if mouse_pos[0] < self.width:
            x = mouse_pos[0] // self.cell_size
            y = mouse_pos[1] // self.cell_size
            self.controller.on_case_click_grille(x, y)
        else:
            maison_pos = (self.width + 20, 300)  # Position de l'icône de maison
            route_pos = (self.width + 125, 300)  # Position de l'icône de route
            magasin_pos = (self.width + 230, 300)  # Position de l'icône de magasin
            maison_rect = pygame.Rect(maison_pos[0], maison_pos[1], 100, 100)
            route_rect = pygame.Rect(route_pos[0], route_pos[1], 100, 100)
            magasin_rect = pygame.Rect(magasin_pos[0], magasin_pos[1], 100, 100)

            if maison_rect.collidepoint(mouse_pos):
                self.selected_type = TypeCase.MAISON
                self.controller.set_selected_type(TypeCase.MAISON)  # Transmettre au contrôleur
            if route_rect.collidepoint(mouse_pos):
                self.selected_type = TypeCase.ROUTE
                self.controller.set_selected_type(TypeCase.ROUTE)  # Transmettre au contrôleur
            if magasin_rect.collidepoint(mouse_pos):
                self.selected_type = TypeCase.MAGASIN
                self.controller.set_selected_type(TypeCase.MAGASIN)

    def view_run(self, grille):
        running = True
        last_update_time = time.time()  # Initialiser le temps de la dernière mise à jour
        update_interval = 3  # Intervalle de mise à jour en secondes

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:  # Gérer les clics de souris
                    self.handle_click()

            current_time = time.time()
            if float(current_time - last_update_time) >= update_interval:
                self.controller.mise_a_jour_reguliere_grille()
                print("on met à jour la carte")
                last_update_time = current_time  # Mettre à jour le temps de la dernière mise à jour

            self.screen.fill((0, 0, 0))
            self.draw_plateau(grille)  # Dessiner le plateau
            self.temps_avant_changement = current_time - last_update_time
            self.draw_sidebar(self.controller.getArgentjoueur())  # Dessiner la bande blanche et l'argent
            self.clock.tick(60)
            pygame.display.flip()

        pygame.quit()
