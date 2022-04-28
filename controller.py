from abc import ABC, abstractmethod
import pygame
import sys
from game import Game


class Controller(ABC):

    def __init__(self):
        self._game = Game()

        # a dictionary with the keys as the pygame constant for
        # each key and the value as 1 or 0, demonstrating if the
        # key was pressed or not, respectively.
        self._keys = {}

    @property
    def game(self):
        return self._game

    @property
    def keys(self):
        return self._keys

    @abstractmethod
    def interpret_input():
        pass


# not needed for MVP 1
class CharacterController(Controller):

    def __init__():
        pass

    def interpret_input():
        pass


class ObstacleController(Controller):

    def interpret_input(self, correct_key):
        """
        Get user input from keyboard and check if it is expected input.

        If the correct key is inputted, the game continues. If not,
        the game.game_over() is called. If the user exits the game window,
        game.game_over() is called.

        Args:
            correct_key: Pygame constant referring to the key that
                needed to be pressed for the given obstacle.
        """
        # if the user exits the game window, end the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # update the values of keys pressed
        self._keys = pygame.key.get_pressed()

        # if the user presses the wrong key, end the game
        if not self.keys[correct_key]:
            self.game.game_over()
        else:
            print('key')