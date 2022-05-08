"""
Unit tests for game
"""

import pygame
from controller import ObstacleController
from obstacle import Obstacle
from game import Game

pygame.init()

# define variables needed to create test instances
possible_obstacles = ["spades", "diamonds", "hearts", "clubs"]
obstacle_actions = {
    "spades": pygame.K_UP,
    "diamonds": pygame.K_DOWN,
    "hearts": pygame.K_LEFT,
    "clubs": pygame.K_RIGHT,
}

# define controller and obstacle for testing
test_controller = ObstacleController(obstacle_actions)
test_obstacles = [Obstacle(obstacle, obstacle_actions)
                  for obstacle in possible_obstacles]

# define test game
game = Game(obstacle_actions)

# set up for testing with user input
up_arrow = pygame.event.Event(pygame.KEYDOWN, {
                              'unicode': '', 'key': 1073741906, 'mod': 4096,
                              'scancode': 82, 'window': None})
down_arrow = pygame.event.Event(pygame.KEYDOWN, {
                                'unicode': '', 'key': 1073741905, 'mod': 4096,
                                'scancode': 81, 'window': None})
left_arrow = pygame.event.Event(pygame.KEYDOWN, {
                                'unicode': '', 'key': 1073741904, 'mod': 4096,
                                'scancode': 80, 'window': None})
right_arrow = pygame.event.Event(pygame.KEYDOWN, {
                                 'unicode': '', 'key': 1073741903, 'mod': 4096,
                                 'scancode': 79, 'window': None})

key_input = [up_arrow, down_arrow, left_arrow, right_arrow]

# define test cases
correct_input_test_cases = [(test_controller, test_obstacles[i])
                            for i in range(len(test_obstacles))]
incorrect_input_test_cases = [
    (test_controller, test_obstacles[::-1][i])
    for i in range(len(test_obstacles))]


# check continue testing
def test_check_continue_incorrect_up():
    """
    If the correct key is not pressed, make sure that the same obstacle
    is returned check incorrect up arrow press.
    """
    pygame.event.post(up_arrow)
    assert game.check_continue(
        test_controller, test_obstacles[1]) == test_obstacles[1]

def test_check_continue_incorrect_down():
    """
    Check incorrect down arrow press.
    """
    pygame.event.post(down_arrow)
    assert game.check_continue(
        test_controller, test_obstacles[2]) == test_obstacles[2]

def test_check_continue_incorrect_left():
    """
    Check incorrect left arrow press.
    """
    pygame.event.post(left_arrow)
    assert game.check_continue(
        test_controller, test_obstacles[3]) == test_obstacles[3]

def test_check_continue_incorrect_right():
    """
    Check incorrect right arrow press.
    """
    pygame.event.post(right_arrow)
    assert game.check_continue(
        test_controller, test_obstacles[0]) == test_obstacles[0]

def test_check_game_over():
    """
    heck that game over attribute is updated.
    """
    game.game_over()
    assert game.game_over_called is True

def test_round_over():
    """
    Check that round over attribute is updated.
    """
    game.round_over()
    assert game.round_over_called is True
