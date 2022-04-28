import sys
import pygame

from world import MaoRun
from game import Game
from obstacle import Obstacle
from controller import ObstacleController

if __name__ == '__main__':
    pygame.init()

    # Initialize world
    CUR_WORLD = MaoRun()
    game = Game()
    control = ObstacleController()
    # Initialize player

    # Initialize obstacles

    # Initialize controller

    while True:
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         sys.exit()
        obstacle_test = Obstacle("square", game.obstacle_actions)
        control.interpret_input(obstacle_test.action)

        CUR_WORLD.display()