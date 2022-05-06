"""
Create a controller for the game.
"""

from abc import ABC, abstractmethod
import pygame
import sys
from game import Game


class Controller(ABC):
    """
    Create an abstract base class for the controller.
    
    Attributes:
        _game: an instance of Game.
    """
    def __init__(self, obstacle_actions):
        """
        Create an instance of controller.

        Args:
            obstacle_actions: a dictionary with the keys as string
                representations of the sprites and the values as
                the randomly assigned expected key press.
        """
        self._game = Game(obstacle_actions)

    @property
    def game(self):
        """
        Create a game property so game can be accessed.
        """
        return self._game

    @abstractmethod
    def interpret_input():
        """
        Create an abstract method to interpret input.
        """
        pass


class ObstacleController(Controller):
    """
    Create a subclass for controller that interprets user input.
    """

    def interpret_input(self, event, correct_key):
        """
        Get user input from keyboard and check if it is expected input.

        Args:
            event: pygame event referring to user input.
            correct_key: Pygame constant referring to the key that
                needed to be pressed for the given obstacle.
        
        Returns:
            A boolean value referring to whether the correct key was pressed.
        """
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
        
        Returns:
            Boolean value determined from current_obstacle.has_collided()
        """
        return current_obstacle.has_collided()
    
    def press_any_arrow_key(self, event):
        """
        Check if the player is pressing one of the arrow keys.
        Args:
            event: pygame event referring to user input.

        Returns
            A boolean statement representing whether the correct key is pressed.
        """
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_UP 
                or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or
                event.key == pygame.K_RIGHT):
            return True
        return False