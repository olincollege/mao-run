"""
Unit tests for controller
"""

import pytest
import pygame
from random import choice
from controller import ObstacleController
from obstacle import Obstacle
from game import Game

# define variables needed to create test instances
actions = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_DOWN]
possible_obstacles = ["spades", "diamonds", "hearts", "clubs"]
obstacle_actions = {
    "spades": choice(actions),
    "diamonds": choice(actions),
    "hearts": choice(actions),
    "clubs": choice(actions),
}

# define controller and obstacle for testing
test_controller = ObstacleController()
test_obstacle = Obstacle(choice(possible_obstacles), obstacle_actions)

# how do you test when you need to have the key go down??
# def test_interpret_input():
#     assert test_controller.interpret_input(test_obstacle.action, test_obstacle.action) == True

# test that the collision is detected when it should be
def test_check_collision_happens():
    test_obstacle._x_position = 200
    assert test_controller.check_collision(test_obstacle) == True

# test that the collision is not detected when it should not be
def test_check_collision_does_not_happen():
    test_obstacle._x_position = 500
    assert test_controller.check_collision(test_obstacle) == False

# test that the collision is detected when obstacle is past the player
def test_check_collision_happens_at_zero():
    test_obstacle._x_position = 0
    assert test_controller.check_collision(test_obstacle) == True