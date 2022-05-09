"""
Main file for Mao Run game implementation.
"""
from random import choice, randint
import pygame
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
    current_obstacle = Obstacle(
        choice(game.POSSIBLE_OBSTACLES), game.obstacle_actions)

    # Initialize controller
    control = ObstacleController(OBSTACLE_ACTIONS)

    # Initialize game states indicator booleans
    game_start = False
    display_instructions = False

    # Initialize counter for player's restart option
    round_num = 1
    best_score = 0

    # Operate the starting state of the game (starting screen + instructions)
    while not game_start:
        # Press any key to display instructions
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                display_instructions = True
            game.exit_window(event)
        if display_instructions:
            CUR_WORLD.display_instructions()
            # Press any arrow key to start game
            for event in pygame.event.get():
                if control.press_any_arrow_key(event):
                    game_start = True
                game.exit_window(event)
        # Display intro screen if no input/irregularity is received
        else:
            CUR_WORLD.display_intro()

    # Operate in game logic and displays
    while game_start:
        if game.score > best_score:
            best_score = game.score
        # Update the current obstacle by checking if the game should continue
        current_obstacle = game.check_continue(control, current_obstacle)
        # Move the current obstacle
        current_obstacle.update_position()
        # Display game over screen when the player pressed the 'ESC' key
        if game.game_over_called:
            CUR_WORLD.display_game_over()
            CUR_WORLD.display_score("High Score: " + str(best_score))
            pygame.display.update()
        # If this iteration of game should be over, restart the game with
        # a new game instance
        elif game.round_over_called:
            # If the game is replayed less than 30 times, display restart screen
            CUR_WORLD.display_restart()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # Initialize new game state + obstacle
                    game = Game(OBSTACLE_ACTIONS)
                    current_obstacle = Obstacle(
                        choice(game.POSSIBLE_OBSTACLES), game.obstacle_actions)
                    # Keep a tally of the amount of restarts
                    round_num += 1
                    # Jump to next loop
                    continue
                game.exit_window(event)
        # Else, update the display and continue this iretation of the game
        else:
            print(current_obstacle.X_VELOCITY)
            if best_score == randint(12, 50):
                current_obstacle.X_VELOCITY["left"] = -randint(53, 60)/10
                current_obstacle.X_VELOCITY["right"] = randint(53, 60)/10
            elif best_score == randint(50, 100):
                current_obstacle.X_VELOCITY["left"] = -randint(55, 80)/10
                current_obstacle.X_VELOCITY["right"] = randint(53, 80)/10
            elif best_score >= 100:
                current_obstacle.X_VELOCITY["left"] = -randint(60, 100)/10
                current_obstacle.X_VELOCITY["right"] = randint(60, 100)/10
            CUR_WORLD.display()
            CUR_WORLD.display_sprites(current_obstacle)
            pygame.display.update()
