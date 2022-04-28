import pygame

class World:

    def __init__(self):
        

        # Necessary to control frame rate for consistency across
        # different devices
        self.clock = pygame.time.Clock()

        title_font = pygame.font.Font(None, 100)
        
        # Initialize a sky surface
        self.sky_surface = pygame.Surface((800,300))
        self.sky_surface.fill('Blue')

        # Initialize a ground surface
        self.ground_surface = pygame.Surface((800,100))
        self.ground_surface.fill('Green')

        self.title_surface = title_font.render('Mao Run', False, 'Brown')

    def display():
        pass
