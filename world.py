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

        # Initialize the instructions screen
        self.instructions = pygame.image.load("Sprites/instructionsscreen.png")

        # Initialize the background screen
        self.background = pygame.image.load("Sprites/backgroundscreen.png")

        # Initialize the restart screen
        self.restart = pygame.image.load("Sprites/restartscreen.png")

        # Initialize the game over screen
        self.game_over = pygame.image.load("Sprites/gameover.png")

        # Set up font for score display
        self.font = pygame.font.Font(None, 32)

        # Initialize a player
        self.player = player

        # Initialize sprites
        self.hearts = pygame.image.load("Sprites/hearts.png")

        self.spades = pygame.image.load("Sprites/spades.png")

        self.clubs = pygame.image.load("Sprites/clubs.png")

        self.diamonds = pygame.image.load("Sprites/diamonds.png")

        # Initialize game icon
        self.maorun_icon = pygame.image.load("Sprites/game_icon.png")
        self.clock = pygame.time.Clock()

    @abstractmethod
    def display(self):
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
        self.infoObject = pygame.display.Info()
        self.screen = pygame.display.set_mode((self.infoObject.current_w, self.infoObject.current_h))

        self.intro = pygame.transform.scale(self.intro, (self.infoObject.current_h, self.infoObject.current_h))
        self.instructions = pygame.transform.scale(self.instructions, (self.infoObject.current_h, self.infoObject.current_h))
        self.background = pygame.transform.scale(self.background, (self.infoObject.current_w, self.infoObject.current_h))
        self.restart = pygame.transform.scale(self.restart, (self.infoObject.current_h, self.infoObject.current_h))
        self.game_over = pygame.transform.scale(self.game_over, (self.infoObject.current_h,self.infoObject.current_h))

        self.hearts = pygame.transform.scale(self.hearts, (pygame.display.Info().current_w/13, pygame.display.Info().current_h/7))
        self.spades = pygame.transform.scale(self.spades, (pygame.display.Info().current_w/13, pygame.display.Info().current_h/7))
        self.clubs = pygame.transform.scale(self.clubs, (pygame.display.Info().current_w/13, pygame.display.Info().current_h/7))
        self.diamonds = pygame.transform.scale(self.diamonds, (pygame.display.Info().current_w/13, pygame.display.Info().current_h/7))

        pygame.display.set_caption('Mao Run')
        pygame.display.set_icon(self.maorun_icon)

    def display_intro(self):
        """
        Insert Docstring
        """
        self.screen.fill("black")
        self.screen.blit(self.intro,self.intro.get_rect(midtop = (self.infoObject.current_w/2,0)))
        self.clock.tick(60)
        pygame.display.update()

    def display_instructions(self):
        """
        Insert Docstring
        """
        self.screen.fill("black")
        self.screen.blit(self.instructions,self.instructions.get_rect(midtop = (self.infoObject.current_w/2,0)))
        self.clock.tick(60)
        pygame.display.update()

    def display_restart(self):
        """
        Insert Docstring
        """
        self.screen.fill("black")
        self.screen.blit(self.restart,self.restart.get_rect(midtop = (self.infoObject.current_w/2,0)))
        self.clock.tick(60)
        pygame.display.update()

    def display_game_over(self):
        """
        Insert Docstring
        """
        self.screen.fill("#5C5755")
        self.screen.blit(self.game_over,self.game_over.get_rect(midtop = (self.infoObject.current_w/2,0)))
        self.clock.tick(60)

    def display_score(self, score):
        """
        Insert Docstring
        """
        self.text = self.font.render(score, False, 'Green')
        self.screen.blit(self.text,self.text.get_rect(midtop = (self.infoObject.current_w *.53,self.infoObject.current_h* .73)))
        self.clock.tick(60)
    
    def display_sprites(self, obstacle):
        """
        Insert Docstring
        """
        if obstacle.sprite == "spades":
            self.screen.blit(self.spades, (obstacle.x_position,
                                           obstacle.y_position))
        elif obstacle.sprite == "diamonds":
            self.screen.blit(self.diamonds, (obstacle.x_position,
                                             obstacle.y_position))
        elif obstacle.sprite == "clubs":
            self.screen.blit(self.clubs, (obstacle.x_position,
                                          obstacle.y_position))
        elif obstacle.sprite == "hearts":
            self.screen.blit(self.hearts, (obstacle.x_position,
                                           obstacle.y_position))
        self.player.draw(self.screen)
        self.player.update()
        self.clock.tick(60)

    def display(self):
        """
        Insert Docstring
        """
        self.screen.blit(self.background, (0, 0))
        # _font = pygame.font.SysFont("chalkduster.ttf", 20, True)
        # _img = _font.render('Esc', True, "WHITE", "BLUE")
        # self.screen.blit(_img, (670, 369))
        # _font = pygame.font.SysFont("chalkduster.ttf", 20)
        # _img = _font.render('Press', True, "BLUE")
        # self.screen.blit(_img, (630, 370))
        # _img = _font.render('to End Game', True, "BLUE")
        # self.screen.blit(_img, (700, 370))
        # _rect = _img.get_rect()
        # pygame.draw.rect(_img, "BLUE", _rect, 1)
        self.clock.tick(60)
