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
    # Initialize player

    # Initialize obstacles
    obstacles = [Obstacle("spades", game.obstacle_actions), Obstacle("diamonds", game.obstacle_actions), Obstacle("hearts", game.obstacle_actions), Obstacle("clubs", game.obstacle_actions)]

    # Initialize controller
    control = ObstacleController()

    while True:
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         sys.exit()
        control.interpret_input(obstacles[0].action, obstacles)
        control.check_collision(obstacles[0])
        obstacles[0].update_position()

        CUR_WORLD.display()