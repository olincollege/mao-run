"""
Unit tests for controller
"""

import pytest
import pygame
from random import choice
from controller import ObstacleController
from obstacle import Obstacle
from game import Game

pygame.init()

# define variables needed to create test instances
actions = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
possible_obstacles = ["spades", "diamonds", "hearts", "clubs"]
obstacle_actions = {
    "spades": pygame.K_UP,
    "diamonds": pygame.K_DOWN,
    "hearts": pygame.K_LEFT,
    "clubs": pygame.K_RIGHT,
}

# define controller and obstacle for testing
test_controller = ObstacleController(obstacle_actions)
test_obstacles = [Obstacle(obstacle, obstacle_actions) for obstacle in possible_obstacles]
test_spades_right = Obstacle("spades", obstacle_actions)
test_spades_right._start_position = "right"
test_spades_left = Obstacle("spades", obstacle_actions)
test_spades_left._start_position = "left"

# set up for testing with user input
up_arrow = pygame.event.Event(pygame.KEYDOWN, {'unicode': '', 'key': 1073741906, 'mod': 4096, 'scancode': 82, 'window': None})
down_arrow = pygame.event.Event(pygame.KEYDOWN, {'unicode': '', 'key': 1073741905, 'mod': 4096, 'scancode': 81, 'window': None})
left_arrow = pygame.event.Event(pygame.KEYDOWN, {'unicode': '', 'key': 1073741904, 'mod': 4096, 'scancode': 80, 'window': None})
right_arrow = pygame.event.Event(pygame.KEYDOWN, {'unicode': '', 'key': 1073741903, 'mod': 4096, 'scancode': 79, 'window': None})

key_input = [up_arrow, down_arrow, left_arrow, right_arrow]

# define test cases
correct_input_test_cases = [(key_input[i], test_obstacles[i]) for i in range(len(key_input))]
incorrect_input_test_cases = [(key_input[::-1][i], test_obstacles[i]) for i in range(len(key_input))]


# input testing
# test that the correct input is detected
@pytest.mark.parametrize("key,obstacle", correct_input_test_cases)
def test_interpret_input_correct(key, obstacle):
    assert test_controller.interpret_input(key, obstacle.action) == True

# test that the incorrect input is detected as incorrect
@pytest.mark.parametrize("key,obstacle", incorrect_input_test_cases)
def test_interpret_input_incorrect(key, obstacle):
    assert test_controller.interpret_input(key, obstacle.action) == False


# collision testing
# test that the collision is detected when it should be from right
def test_check_collision_happens_right():
    test_spades_right._x_position = 400
    assert test_controller.check_collision(test_spades_right) == True

# test that the collision is not detected when it should not be
# from right hand side
def test_check_collision_does_not_happen_right():
    test_spades_right._x_position = 500
    assert test_controller.check_collision(test_spades_right) == False

# test that the collision is detected when it should be from left
def test_check_collision_happens_left():
    test_spades_left._x_position = 350
    assert test_controller.check_collision(test_spades_left) == True

# test that the collision is not detected when it should not be
# from right hand side
def test_check_collision_does_not_happen_left():
    test_spades_left._x_position = 200
    assert test_controller.check_collision(test_spades_left) == False