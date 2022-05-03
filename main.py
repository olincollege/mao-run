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

    # initialize constants
    actions = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
    obstacle_actions = {
            "spades": choice(actions),
            "diamonds": choice(actions),
            "hearts": choice(actions),
            "clubs": choice(actions),
    }
    num_rounds = 0

    # initiliaze player
    player = pygame.sprite.GroupSingle()
    player.add(Character())

    # Initialize world
    CUR_WORLD = MaoRun(player)

    #initialize game
    game = Game(obstacle_actions)

    # Initialize player
    
    # Initialize current obstacle
    current_obstacle = Obstacle(choice(game.possible_obstacles), game.obstacle_actions)

    # Initialize controller
    control = ObstacleController(obstacle_actions)

    # allow the users three chances to play the game
    while num_rounds < 3:
        num_rounds += 1

        # have the game continue until it should end
        while True:
            # update the current obstacle by checking if the game should continue
            current_obstacle = game.check_continue(control, current_obstacle)
            # move the current obstacle
            current_obstacle.update_position()

            # if the game should be over, restart the game and break the loop
            if game.game_over_called:
                print("restart")
                # CUR_WORLD.display_restart()
                game = Game(obstacle_actions)
                break
            # else, update the display
            else:
                CUR_WORLD.display()
                CUR_WORLD.display_obstacles(current_obstacle)
                pygame.display.update()
    
    # after three tries, display game over screen
    CUR_WORLD.display_game_over()
