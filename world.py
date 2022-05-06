"""
View file. Deals with all rendering and displaying tasks.
"""

from abc import ABC, abstractmethod
from numpy import character
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

        # Initialize the game over screen
        self.game_over = pygame.image.load("Sprites/gameover.png")
        self.game_over = pygame.transform.scale(self.game_over, (500,400))

        # Initialize the instructions screen
        self.instructions = pygame.image.load("Sprites/instructionsscreen.png")
        self.instructions = pygame.transform.scale(self.instructions, (400,400))

        # Set up font for score display
        self.font = pygame.font.Font(None, 32)

        # Initialize game icon
        self.maorun_icon = pygame.image.load("Sprites/game_icon.png")
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
    def __init__(self, character):
        """
        Insert Docstring
        """
        super().__init__(character)

        # Initialize a screen
        self.screen = pygame.display.set_mode((800,400))
        # infoObject = pygame.display.Info()
        # self.screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
        pygame.display.set_caption('Mao Run')
        pygame.display.set_icon(self.maorun_icon)

    def display_intro (self):
        """
        Insert Docstring
        """
        self.screen.fill("black")
        self.screen.blit(self.intro,(200,0))
        self.clock.tick(60)
        pygame.display.update()

    def display_instructions(self):
        """
        Insert Docstring
        """
        self.screen.fill("black")
        self.screen.blit(self.instructions,(200,0))
        self.clock.tick(60)
        pygame.display.update()

    def display_score(self, score):
        """
        Insert Docstring
        """
        self.text = self.font.render(score, False, 'Green')
        self.screen.blit(self.text,(365,300))
        self.clock.tick(60)

    def display_game_over(self):
        """
        Insert Docstring
        """
        self.screen.fill("#5C5755")
        self.screen.blit(self.game_over,(150,0))
        self.clock.tick(60)
    
    def display_restart(self):
        """
        Insert Docstring
        """
        self.screen.fill("black")
        self.screen.blit(self.restart, (200,0))
        self.clock.tick(60)
        pygame.display.update()
    
    def display_sprites(self, obstacle):
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
        self.player.update()
        self.clock.tick(60)

    def display(self):
        """
        Insert Docstring
        """
        self.screen.blit(self.background,(0,0))
        self.clock.tick(60)
