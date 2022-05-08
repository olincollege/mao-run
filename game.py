"""
Create game functionality
"""
import sys
from random import choice
import pygame
from obstacle import Obstacle


class Game:
    """
    Functionality for the mao-run game.

    Attributes:
        POSSIBLE_OBSTACLES: a list of the possible obstacles for the game.
        score: an integer representing the player's score.
        _round_over_called: a boolean representing whether the round has ended.
        _game_over_called: a boolean representing whether the game has ended.
        _obstacle_actions: a dictionary with the keys as the string
            representations of the obstacles and the values as the
            expected key presses.
    """
    POSSIBLE_OBSTACLES = ["spades", "diamonds", "hearts", "clubs"]
    score = 0

    def __init__(self, obstacle_actions):
        """
        Create an instance of Game.

        Args:
            obstacle_actions: a dictionary with the keys as the string
                representations of the obstacles and the values as the
                expected key presses.
        """
        self._round_over_called = False
        self._game_over_called = False
        self._obstacle_actions = obstacle_actions

    @property
    def round_over_called(self):
        """
        Create a round_over_called property for Game.
        """
        return self._round_over_called

    @property
    def game_over_called(self):
        """
        Create a game_over_called property for Game.
        """
        return self._game_over_called

    @property
    def obstacle_actions(self):
        """
        Create an obstacle_actions property for Game.
        """
        return self._obstacle_actions

    def round_over(self):
        """"
        Demonstrate that the round is over.
        """
        self._round_over_called = True

    def game_over(self):
        """"
        Demonstrate that the game is over.
        """
        self._game_over_called = True

    @staticmethod
    def exit_window(event):
        """
        Allow the user to turn off the game windown when clicking the
        'X' button.

        Args:
            event: a pygame event regarding user input.
        """
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    def check_continue(self, control, obstacle):
        """
        Check whether the game should continue.

        If the user presses the correct key, the game continues.
        If not, round_over is called and the game restarts.

        Args:
            control: An ObstacleController instance for the current game.
            obstacle: An obstacle instance that is the current obstacle
                on the screen.

        Returns:
            An obstacle instance that is the same as the argument if the game
            is not over and the key is pressed, or is a new random obstacle if
            the correct key was pressed.
        """
        for event in pygame.event.get():
            # if the user tries to exit the window, end the game
            self.exit_window(event)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game_over()
            self.exit_window(event)
            # determine whether the user pressed the correct key
            pressed_correct_key = control.interpret_input(
                event, obstacle.action)

            # if a key is pressed and the key is the correct key, return a new
            # obstacle instance
            if event.type == pygame.KEYDOWN:
                if pressed_correct_key:
                    self.score += 1
                    return Obstacle(choice(self.POSSIBLE_OBSTACLES),
                                    self.obstacle_actions)
                self.round_over()

        # If the obstacle collides with the player, end the game
        if control.check_collision(obstacle):
            self.round_over()

        # Return the obstacle instance entered as an argument
        # if no keys were pressed
        return obstacle
