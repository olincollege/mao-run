"""
Unit tests for controller
"""

import pytest
import pygame
from controller import ObstacleController
from obstacle import Obstacle

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
test_obstacles = [Obstacle(obstacle, obstacle_actions)
                  for obstacle in possible_obstacles]
test_spades_right = Obstacle("spades", obstacle_actions, "right")
test_spades_left = Obstacle("spades", obstacle_actions, "left")


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
space_bar = pygame.event.Event(pygame.KEYDOWN, {
                               'unicode': ' ', 'key': 32, 'mod': 4096,
                               'scancode': 44, 'window': None})

key_input = [up_arrow, down_arrow, left_arrow, right_arrow]

# define test cases
correct_input_test_cases = [(key_input[i], test_obstacles[i])
                            for i in range(len(key_input))]
incorrect_input_test_cases = [
    (key_input[::-1][i], test_obstacles[i]) for i in range(len(key_input))]


# input testing
@pytest.mark.parametrize("key,obstacle", correct_input_test_cases)
def test_interpret_input_correct(key, obstacle):
    """
    Test that the correct input is detected.

    Args:
        key: Pygame event representing key press.
        obstacle: an instance of Obstacle.
    """
    assert test_controller.interpret_input(key, obstacle.action) is True

@pytest.mark.parametrize("key,obstacle", incorrect_input_test_cases)
def test_interpret_input_incorrect(key, obstacle):
    """
    Test that the incorrect input is detected as incorrect.

    Args:
        key: Pygame event representing key press.
        obstacle: an instance of Obstacle.
    """
    assert test_controller.interpret_input(key, obstacle.action) is False


# collision testing
def test_check_collision_happens_right():
    """
    Test that the collision is detected when it should be from right.
    """
    test_spades_right._x_position = 400 # pylint: disable=protected-access
    assert test_controller.check_collision(test_spades_right) is True

def test_check_collision_does_not_happen_right():
    """
    Test that the collision is not detected when it should not be
    from right hand side.
    """
    test_spades_right._x_position = 500 # pylint: disable=protected-access
    assert test_controller.check_collision(test_spades_right) is False

def test_check_collision_happens_left():
    """
    Test that the collision is detected when it should be from left.
    """
    test_spades_left._x_position = 300 # pylint: disable=protected-access
    assert test_controller.check_collision(test_spades_left) is True

def test_check_collision_does_not_happen_left():
    """
    Test that the collision is not detected when it should not be
    from left hand side.
    """
    test_spades_left._x_position = 200 # pylint: disable=protected-access
    assert test_controller.check_collision(test_spades_left) is False


# test press any arrow key function
def test_press_any_arrow_key_with_input():
    """
    Check that a key press is detected.
    """
    assert test_controller.press_any_arrow_key(right_arrow) is True

def test_press_any_arrow_key_no_input():
    """
    Check that when a key other than arrow key is pressed, false is returned.
    """
    assert test_controller.press_any_arrow_key(space_bar) is False
