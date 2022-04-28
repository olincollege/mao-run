"""
View file. Deals with all rendering and displaying tasks.
"""

from abc import ABC, abstractmethod
import pygame

class world(ABC):

    def __init__(self):
        # title_font = pygame.font.Font(None, 100)
        
        # Initialize a sky surface
        self.sky_surface = pygame.Surface((800,300))
        self.sky_surface.fill('Blue')

        # Initialize a ground surface
        self.ground_surface = pygame.Surface((800,100))
        self.ground_surface.fill('Green')
        # self.title_surface = title_font.render('Mao Run', False, 'Brown')

        self.clock = pygame.time.Clock()
    
    @abstractmethod
    def display():
        """
        An abstract method that does nothing.
        """
        pass

class MaoRun(world):
    def __init__(self):
        super().__init__()

        # Initialize a screen
        self.screen = pygame.display.set_mode((800,400))
        pygame.display.set_caption('Mao Run')

    def display(self):
        self.screen.blit(self.sky_surface,(0,0))
        self.screen.blit(self.ground_surface,(0,300))
        # self.screen.blit(self.title_surface,(250,120))
        # self.screen.blit(self.player_surface,self.player_rect)

        pygame.display.update()
        self.clock.tick(60)
