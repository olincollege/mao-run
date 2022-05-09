"""
View file. Deals with all rendering and displaying tasks.
"""

from abc import ABC, abstractmethod
import pygame


class world(ABC):
    """
    An abstract-base class representing the view of Mao Run. Load all
    the necessary images and texts that appear on the game screen.

    Attributes:
        maorun_icon: A pygame surface that represents the app icon
        intro: A pygame surface that represents the Introduction screen
        clock: A clock object that controls the frames of the game
        _fps: An integer representing frames per second
        instructions: A pygame surface that represents the Instructions screen
        background: A pygame surface that represents the
            background when the game is active
        restart: A pygame surface that represents the Restart screen
        game_over: A pygame surface that represents the Game Over screen
        score_font: A pygame font set for score display
        esc_font: A pygame font set for "Esc" message display
        esc_font_bold: A pygame font set for bolded "Esc"
            message display
        press: A text surface that says "Press"
        esc: A text surface that says "Esc"
        to_end_game: A text surface that says "to end game"
        player: A Character instance
        hearts: A pygame surface that represents a heart obstacle
        spades: A pygame surface that represents a spade obstacle
        clubs: A pygame surface that represents a club obstacle
        diamonds: A pygame surface that represents a diamond obstacle
    """

    def __init__(self, player):
        """
        Create a world instance.

        Args:
            player (Character): A Character instance representing the player
        """
        # Initialize game icon
        self.maorun_icon = pygame.image.load("Sprites/game_icon.png")
        self.clock = pygame.time.Clock()
        self._fps = 60

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
        self.score_font = pygame.font.Font(None, 32)

        # Set up font for "Esc" instructions
        self.esc_font = pygame.font.SysFont("chalkduster.ttf", 20)
        self.esc_font_bold = pygame.font.SysFont("chalkduster.ttf", 20, True)

        # Set up content for "Esc" instructions
        self.press = self.esc_font.render('Press', True, "BLUE")
        self.esc = self.esc_font_bold.render('Esc', True, "WHITE", "BLUE")
        self.to_end_game = self.esc_font.render('to end game', True, "BLUE")

        # Initialize a player
        self.player = player

        # Initialize sprites
        self.hearts = pygame.image.load("Sprites/hearts.png")
        self.spades = pygame.image.load("Sprites/spades.png")
        self.clubs = pygame.image.load("Sprites/clubs.png")
        self.diamonds = pygame.image.load("Sprites/diamonds.png")

    @property
    def fps(self):
        """
        Return the FPS of the game.
        """
        return self._fps

    @abstractmethod
    def display_intro(self):
        """
        An abstract method that passes the display_intro function.
        """
        pass

    @abstractmethod
    def display_instructions(self):
        """
        An abstract method that passes the display_instructions
        function.
        """
        pass

    @abstractmethod
    def display_restart(self):
        """
        An abstract method that passes the display_restart function.
        """
        pass

    @abstractmethod
    def display_game_over(self):
        """
        An abstract method that passes the display_game_over
        function.
        """
        pass

    @abstractmethod
    def display_score(self, score):
        """
        An abstract method that passes the display_score
        function.
        """
        pass

    @abstractmethod
    def display_sprites(self, obstacle):
        """
        An abstract method that passes the display_sprites
        function.
        """
        pass

    @abstractmethod
    def display_esc_instructions(self):
        """
        An abstract method that passes the display_esc_instructions
        function.
        """
        pass

    @abstractmethod
    def display(self):
        """
        An abstract method that passes the display function.
        """
        pass


class MaoRun(world):
    """
    Display the Mao Run world.

    Attributes:
        info_screen (Vidinfo): Player's display information
        screen_width (float): Player's display width
        screen_height (float): Player's display height
        screen (Pygame surface): The window to display the game
        intro (pygame surface): Introduction screen
        instructions (pygame surface): Instructions screen
        background (pygame surface): Background when the game is active
        restart (pygame surface): Restart screen
        game_over (pygame surface): Game Over screen
        hearts (pygame surface): A heart obstacle
        spades (pygame surface): A spade obstacle
        clubs (pygame surface): A club obstacle
        diamonds (pygame surface): A diamond obstacle
    """

    def __init__(self, character):
        """
        Initialize necessary attributes in Mao Run world.

        Args:
            character (Character): A Character instance representing the player
        """
        # Inherits all attributes from character
        super().__init__(character)

        # Get player's screen information
        self.info_screen = pygame.display.Info()

        # Initialize a screen based on the player's screen
        self.screen_width = self.info_screen.current_w/2
        self.screen_height = self.info_screen.current_h/2
        self.screen = pygame.display.set_mode((self.screen_width,
                                                self.screen_height))

        # Reset the scale of different screens during the game
        self.intro = pygame.transform.scale(self.intro,
                                    (self.screen_height,self.screen_height))
        self.instructions = pygame.transform.scale(self.instructions,
                                    (self.screen_height,self.screen_height))
        self.background = pygame.transform.scale(self.background,
                                    (self.screen_width, self.screen_height))
        self.restart = pygame.transform.scale(self.restart,
                                    (self.screen_height, self.screen_height))
        self.game_over = pygame.transform.scale(self.game_over,
                                    (self.screen_height,self.screen_height))

        # Reset the scale of Mao Run obstacles
        self.hearts = pygame.transform.scale(self.hearts,
                                (self.screen_width/13, self.screen_height/7))
        self.spades = pygame.transform.scale(self.spades,
                                (self.screen_width/13, self.screen_height/7))
        self.clubs = pygame.transform.scale(self.clubs,
                                (self.screen_width/13, self.screen_height/7))
        self.diamonds = pygame.transform.scale(self.diamonds,
                                (self.screen_width/13, self.screen_height/7))

        # Set the game title
        pygame.display.set_caption('Mao Run')

        # Set the game icon
        pygame.display.set_icon(self.maorun_icon)

    def display_intro(self):
        """
        Display introduction surface to screen.
        """
        self.screen.fill("black")
        self.screen.blit(self.intro,
            self.intro.get_rect(midtop=(self.screen_width/2,0)))
        self.clock.tick(self.fps)
        pygame.display.update()

    def display_instructions(self):
        """
        Display instructions surface to screen.
        """
        self.screen.fill("black")
        self.screen.blit(self.instructions,
            self.instructions.get_rect(midtop=(self.screen_width/2,0)))
        self.clock.tick(self.fps)
        pygame.display.update()

    def display_restart(self):
        """
        Display restart surface to screen.
        """
        self.screen.fill("black")
        self.screen.blit(self.restart,
            self.restart.get_rect(midtop=(self.screen_width/2,0)))
        self.clock.tick(self.fps)
        pygame.display.update()

    def display_game_over(self):
        """
        Display game over surface to screen.
        """
        self.screen.fill("#5C5755")
        self.screen.blit(self.game_over,
            self.game_over.get_rect(midtop = (self.screen_width/2,0)))
        self.clock.tick(self.fps)

    def display_score(self, score):
        """
        Display score surface to screen.

        Args:
            score (string): The highest score of the current implementation
                of Mao Run.
        """
        text = self.score_font.render(score, False, 'Green')
        self.screen.blit(text,text.get_rect(midtop=(self.screen_width*.53,
                                                    self.screen_height*.73)))
        self.clock.tick(self.fps)

    def display_sprites(self, obstacle):
        """
        Display sprites surface to screen.

        Args:
            obstacle: An obstacle instance that is randomly generated.
        """
        # Display different obstacle sprites
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
        # Display character
        self.player.draw(self.screen)
        # Update character animation
        self.player.update()
        # Control frame rate
        self.clock.tick(self.fps)

    def display_esc_instructions(self):
        """
        Display "Esc" instructions surface to screen.
        """
        self.screen.blit(self.press,
            self.press.get_rect(bottomright=(self.screen_width-120,
                                            self.screen_height-5)))
        self.screen.blit(self.esc,
            self.esc.get_rect(bottomright=(self.screen_width-90,
                                            self.screen_height-5)))
        self.screen.blit(self.to_end_game,
            self.to_end_game.get_rect(bottomright=(self.screen_width-5,
                                                self.screen_height-5)))

    def display(self):
        """
        Display in game environment without sprites.
        """
        self.screen.blit(self.background, (0, 0))
        self.display_esc_instructions()
        self.clock.tick(self.fps)
