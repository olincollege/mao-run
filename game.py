import pygame
import sys
from random import choice

class Game:

    actions = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_DOWN]

    def __init__(self):
        self.world = "" # create world instance
        self._obstacle_actions = {
            "spaids": choice(self.actions),
            "diamonds": choice(self.actions),
            "hearts": choice(self.actions),
            "clubs": choice(self.actions),
        }
        self.obstacles = [] # create obstacle instances
        self.character = "" # create character instance
        # self.player = ObstacleController()
    
    @property
    def obstacle_actions(self):
        return self._obstacle_actions
    
    def game_over(self):
        """"
        Demonstrate that the game is over.

        Update the screen to demonstrate the game is over.
        """
        print("game over")
        # return False
        # create a method in world that will display game over when called
    
    def update_obstacles():
        pass

    # def check_continue(self, obstacle):
    #     """
    #     Check whether the game should continue.

    #     If the user presses the correct key, the game continues.
    #     If not, game_over is called and the game restarts.

    #     Args:
    #         obstacle: An obstacle instance that is the current obstacle
    #             on the screen.
    #     """
    #     if self.player.interpret_input(obstacle.action):
    #         print("Can continue")
    #     else:
    #         print("end game")
    #         self.game_over()

