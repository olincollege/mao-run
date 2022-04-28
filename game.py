import pygame
from random import choice
from obstacle import Obstacle
from controller import ObstacleController

class Game:

    actions = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_DOWN]

    def __init__(self):
        self.world = "" # create world instance
        self._obstacle_actions = {
            "square": choice(self.actions),
            "rectangle": choice(self.actions),
            "triangle": choice(self.actions),
            "circle": choice(self.actions),
        }
        self.obstacles = [] # create obstacle instances
        self.character = "" # create character instance
        self.player = ObstacleController()
    
    def game_over(self):
        print("game over")
        self.restart()

    def restart():
        pass
    
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

