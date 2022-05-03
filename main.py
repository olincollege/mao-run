import sys
import pygame
from random import choice
from world import MaoRun
from game import Game
from character import Character
from obstacle import Obstacle
from controller import ObstacleController

if __name__ == '__main__':
    pygame.init()

    player = pygame.sprite.GroupSingle()
    player.add(Character())

    # Initialize world
    CUR_WORLD = MaoRun(player)
    game = Game()

    # Initialize player
    
    # Initialize current obstacle
    current_obstacle = Obstacle(choice(game.possible_obstacles), game.obstacle_actions)

    # Initialize controller
    control = ObstacleController()

    while True:
        current_obstacle = game.check_continue(control, current_obstacle)
        current_obstacle.update_position()
        if game.called:
            CUR_WORLD.display_game_over()
        else:
            CUR_WORLD.display(current_obstacle)
