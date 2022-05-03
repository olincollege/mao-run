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

    # Initialize player
    player = pygame.sprite.GroupSingle()
    player.add(Character())

    # Initialize world
    CUR_WORLD = MaoRun(player)

    #initialize game
    game = Game(obstacle_actions)

    # Initialize current obstacle
    current_obstacle = Obstacle(choice(game.possible_obstacles), game.obstacle_actions)

    # Initialize controller
    control = ObstacleController(obstacle_actions)

    # # allow the users three chances to play the game
    # while num_rounds < 3:
    #     num_rounds += 1
    #     print(game.game_over_called)

        # have the game continue until it should end
    game_start = False
    display_instructions = False
    while not game_start:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                display_instructions = True
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if display_instructions:
            CUR_WORLD.display_instructions()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_UP 
                    or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or
                    event.key == pygame.K_RIGHT):
                    game_start = True
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        else:
            CUR_WORLD.display_intro()
    while game_start:
        # update the current obstacle by checking if the game should continue
        current_obstacle = game.check_continue(control, current_obstacle)
        # move the current obstacle
        current_obstacle.update_position()

        # if the game should be over, restart the game and break the loop
        if game.game_over_called:
            if num_rounds < 2:
                CUR_WORLD.display_restart()
                for event in pygame.event.get():
                    # if the user tries to exit the window, end the game
                    if event.type == pygame.KEYDOWN:
                        game = Game(obstacle_actions)
                        current_obstacle = Obstacle(choice(game.possible_obstacles), game.obstacle_actions)
                        num_rounds += 1
                        continue
            else:
                CUR_WORLD.display_game_over()
        # else, update the display
        else:
            CUR_WORLD.display()
            CUR_WORLD.display_obstacles(current_obstacle)
            pygame.display.update()
