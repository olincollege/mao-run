import pygame
import sys
from random import choice
from obstacle import Obstacle
from world import MaoRun

class Game:

    possible_obstacles = ["spades", "diamonds", "hearts", "clubs"]

    def __init__(self, obstacle_actions):
        self._game_over_called = False
        self._obstacle_actions = obstacle_actions
    
    @property
    def game_over_called(self):
        return self._game_over_called

    @property
    def obstacle_actions(self):
        return self._obstacle_actions
    
    def game_over(self):
        """"
        Demonstrate that the game is over.
        """
        self._game_over_called = True

    def check_continue(self, control, obstacle):
        """
        Check whether the game should continue.

        If the user presses the correct key, the game continues.
        If not, game_over is called and the game restarts.

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
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # determine whether the user pressed the correct key
            pressed_correct_key = control.interpret_input(event, obstacle.action)

            # if a key is pressed and the key is the correct key, return a new
            # obstacle instance
            if event.type == pygame.KEYDOWN:
                if pressed_correct_key:
                    print(obstacle.sprite)
                    return Obstacle(choice(self.possible_obstacles), self.obstacle_actions)
                else:
                    self.game_over()
        
        # If the obstacle collides with the player, end the game
        if control.check_collision(obstacle):
            self.game_over()
        
        # Return the obstacle instance entered as an argument if no keys were pressed
        return obstacle
