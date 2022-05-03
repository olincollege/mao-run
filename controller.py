"""
Contro
"""

from abc import ABC, abstractmethod
import pygame
import sys
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

    def interpret_input(self, event, correct_key):
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
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         sys.exit()

            # if a key is down, check if the correct key was pressed
            # if it is not the correct key, end the game
        if event.type == pygame.KEYDOWN:
            if event.key != correct_key:
                return False
            return True
        return

    def check_collision(self, current_obstacle):
        """
        Check whether the obstacle has collided with the character.

        Args:
            current_obstacle: An instance of obstacle that represents
                the obstacle on the screen.
        """
        if current_obstacle.x_position <= 200:
            return True
        return False