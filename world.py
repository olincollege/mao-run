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
        
        self.joker = pygame.image.load("Sprites/joker2.png")
        self.joker_rect = self.joker.get_rect(midbottom = (80,300))

        self.hearts = pygame.image.load("Sprites/hearts.png")
        # self.heart_rect = self.heart.get_rect(midbottom = (300,300))

        self.spades = pygame.image.load("Sprites/spades.png")
        self.spades_rect = self.spades.get_rect(midbottom = (300,300))

        self.clubs = pygame.image.load("Sprites/clubs.png")
        self.clubs_rect = self.clubs.get_rect(midbottom = (300,300))

        self.diamonds = pygame.image.load("Sprites/diamonds.png")
        self.diamonds_rect = self.diamonds.get_rect(midbottom = (300,300))

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

    def display(self, obstacle):
        self.screen.blit(self.sky_surface,(0,0))
        self.screen.blit(self.ground_surface,(0,300))
        self.screen.blit(self.joker,(80,200))
        # self.screen.blit(self.title_surface,(250,120))
        # self.screen.blit(self.player_surface,self.player_rect)

        if obstacle.sprite == "spades":
            self.screen.blit(self.spades, (obstacle.x_position, \
                obstacle.y_position))
        elif obstacle.sprite == "diamonds":
            self.screen.blit(self.diamonds, (obstacle.x_position, \
                obstacle.y_position))
        elif obstacle.sprite == "clubs":
            self.screen.blit(self.clubs, (obstacle.x_position, \
                obstacle.y_position))
        elif obstacle.sprite == "hearts":
            self.screen.blit(self.hearts, (obstacle.x_position, \
                obstacle.y_position))

        pygame.display.update()
        self.clock.tick(60)

    # def obstacle_display(self, obstacle):
    #     if obstacle.sprite == "spades":
    #         self.screen.blit(self.spades, (obstacle.x_position, \
    #             obstacle.y_position))
    #     elif obstacle.sprite == "diamonds":
    #         self.screen.blit(self.diamonds, (obstacle.x_position, \
    #             obstacle.y_position))
    #     elif obstacle.sprite == "clubs":
    #         self.screen.blit(self.clubs, (obstacle.x_position, \
    #             obstacle.y_position))
    #     elif obstacle.sprite == "hearts":
    #         self.screen.blit(self.hearts, (obstacle.x_position, \
    #             obstacle.y_position))