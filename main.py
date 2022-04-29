import sys
import pygame
from random import choice
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
    possible_obstacles = ["spaids", "diamonds", "hearts", "clubs"]
    obstacle_list = [Obstacle(choice(possible_obstacles), game.obstacle_actions) for _ in range(10)]
    # obstacles = [Obstacle("spaids", game.obstacle_actions), Obstacle("diamonds", game.obstacle_actions), Obstacle("hearts", game.obstacle_actions), Obstacle("clubs", game.obstacle_actions)]

    # Initialize controller
    control = ObstacleController()

    while True:
        CUR_WORLD.display(obstacle_list[0])
        should_continue = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pressed_correct_key = control.interpret_input(event, obstacle_list[0].action, obstacle_list)
            has_collided = control.check_collision(obstacle_list[0])
            if event.type == pygame.KEYDOWN:
                if pressed_correct_key:
                    should_continue = False
                    print(obstacle_list[0].sprite)
                    obstacle_list = obstacle_list[1:]
                    break
            if has_collided:
                game.game_over()
        if control.check_collision(obstacle_list[0]):
            game.game_over()

        # print([obstacle.sprite for obstacle in obstacle_list])
        obstacle_list[0].update_position()
        # CUR_WORLD.obstacle_display(obstacle_list[0])