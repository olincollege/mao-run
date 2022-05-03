"""
View file. Deals with all rendering and displaying tasks.
"""

from abc import ABC, abstractmethod
import pygame

class world(ABC):
    """
    Insert Docstring
    """
    def __init__(self, player):
        """
        Insert Docstring
        """
        # Initialize the intro screen
        self.intro = pygame.image.load("Sprites/introscreen.png")
        self.intro = pygame.transform.scale(self.intro, (400,400))

        # Initialize the background screen
        self.background = pygame.image.load("Sprites/backgroundscreen.png")
        self.background = pygame.transform.scale(self.background, (800,400))

        # Initialize the restart screen
        self.restart = pygame.image.load("Sprites/restartscreen.png")
        self.restart = pygame.transform.scale(self.restart, (400,400))

        # Initialize a player
        self.player = player

        # Initialize sprites
        self.hearts = pygame.image.load("Sprites/hearts.png")
        self.heart_rect = self.hearts.get_rect(midbottom = (400,300))

        self.spades = pygame.image.load("Sprites/spades.png")
        self.spades_rect = self.spades.get_rect(midbottom = (300,300))

        self.clubs = pygame.image.load("Sprites/clubs.png")
        self.clubs_rect = self.clubs.get_rect(midbottom = (300,300))

        self.diamonds = pygame.image.load("Sprites/diamonds.png")
        self.diamonds_rect = self.diamonds.get_rect(midbottom = (300,300))

        # Initialize a game over screen
        self.game_over = pygame.image.load("Sprites/gameover.png")
        self.game_over = pygame.transform.scale(self.game_over, (500,400))
        
        self.clock = pygame.time.Clock()
    
    @abstractmethod
    def display():
        """
        An abstract method that does nothing.
        """
        pass

class MaoRun(world):
    """
    Insert Docstring
    """
    def __init__(self, Character):
        """
        Insert Docstring
        """
        super().__init__(Character)

        # Initialize a screen
        self.screen = pygame.display.set_mode((800,400))
        pygame.display.set_caption('Mao Run')

    def display_intro (self):
        """
        Insert Docstring
        """
        self.screen.fill("black")
        self.screen.blit(self.intro,(200,0))
        self.clock.tick(60)
        pygame.display.update()

    def display_game_over(self):
        """
        Insert Docstring
        """
        self.screen.fill("#5C5755")
        self.screen.blit(self.game_over,(150,0))
        self.clock.tick(60)
        pygame.display.update()
    
    def display_restart(self):
        """
        Insert Docstring
        """
        self.screen.fill("black")
        self.screen.blit(self.restart, (200,0))
        self.clock.tick(60)
        pygame.display.update()
    
    def display_obstacles(self, obstacle):
        """
        Insert Docstring
        """
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
        self.player.draw(self.screen)
        self.clock.tick(60)

    def display(self):
        """
        Insert Docstring
        """
        self.screen.blit(self.background,(0,0))
        self.clock.tick(60)
