"""
Insert Docstring Here
"""

import sys
import pygame
from random import choice
from world import MaoRun
from game import Game
from character import Character
from obstacle import Obstacle
from controller import ObstacleController

if __name__ == '__main__':
    # Starts pygame
    pygame.init()

    # Initialize constants
    ACTIONS = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
    OBSTACLE_ACTIONS = {
            "spades": choice(ACTIONS),
            "diamonds": choice(ACTIONS),
            "hearts": choice(ACTIONS),
            "clubs": choice(ACTIONS),
    }

    # Initialize player
    player = pygame.sprite.GroupSingle()
    player.add(Character())

    # Initialize world
    CUR_WORLD = MaoRun(player)

    # Initialize game
    game = Game(OBSTACLE_ACTIONS)

    # Initialize current obstacle
    current_obstacle = Obstacle(choice(game.possible_obstacles), game.obstacle_actions)

    # Initialize controller
    control = ObstacleController(OBSTACLE_ACTIONS)

    # Initialize game states indicator booleans
    game_start = False
    display_instructions = False

    # Initialize counter for player's restart option
    num_rounds = 0

    # Operate the starting state of the game (starting screen + instructions)
    while not game_start:
        # Press any key to display instructions
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                display_instructions = True
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if display_instructions:
            CUR_WORLD.display_instructions()
            # Press any arrow key to start game
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_UP 
                    or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or
                    event.key == pygame.K_RIGHT):
                    game_start = True
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        # Display intro screen if no input/irregularity is received
        else:
            CUR_WORLD.display_intro()
    
    # Operate in game logic and displays
    while game_start:
        # Update the current obstacle by checking if the game should continue
        current_obstacle = game.check_continue(control, current_obstacle)
        # Move the current obstacle
        current_obstacle.update_position()

        # If this iteration of game should be over, restart the game with a new game instance
        if game.game_over_called:
            # If the game is replayed less than 30 times, display restart screen
            if num_rounds < 30:
                CUR_WORLD.display_restart()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        # Initialize new game state + obstacle
                        game = Game(OBSTACLE_ACTIONS)
                        current_obstacle = Obstacle(choice(game.possible_obstacles), game.obstacle_actions)
                        # Keep a tally of the amount of restarts
                        num_rounds += 1
                        # Jump to next loop
                        continue
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
            # If the game is replayed more than 30 times, display game over screen
            else:
                CUR_WORLD.display_game_over()

        # Else, update the display and continue this iretation of the game
        else:
            CUR_WORLD.display()
            CUR_WORLD.display_obstacles(current_obstacle)
            pygame.display.update()
