from abc import ABC, abstractmethod
import pygame
from game import Game


class Controller(ABC):

    def __init__(self):
        self._game = Game()

    @property
    def game(self):
        return self._game

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
        the game.game_over() is called.

        Args:
            correct_key: Pygame constant referring to the key that
                needed to be pressed for the given obstacle.
        """
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key != correct_key:
                    self.game.game_over()