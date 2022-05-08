"""
Unit tests for obstacle
"""

import pygame
from obstacle import Obstacle

pygame.init()

# define variables needed to create test instances
obstacle_actions = {
    "spades": pygame.K_UP,
    "diamonds": pygame.K_DOWN,
    "hearts": pygame.K_LEFT,
    "clubs": pygame.K_RIGHT,
}

# define test obstacle instances
test_spades_right = Obstacle("spades", obstacle_actions, "right")
test_spades_left = Obstacle("spades", obstacle_actions, "left")


# update position testing
def test_update_position_left():
    """
    Test that x_position updated correctly when obstacle
    begins on the left hand side.
    """
    test_spades_left.update_position()
    assert test_spades_left.x_position == 4


def test_update_position_right():
    """
    Test that x_position updated correctly when obstacle
    begins on right hand side.
    """
    test_spades_right.update_position()
    assert test_spades_right.x_position == 796


# has collided testing
def test_has_collided_left():
    """
    Test that collision detected when coming from left
    hand side
    """
    test_spades_left._x_position = \
        test_spades_left.collision_position  # pylint: disable=protected-access
    assert test_spades_left.has_collided() is True


def test_has_not_collided_left():
    """
    Test that collision is not detected when coming from left
    hand side
    """
    test_spades_left._x_position = test_spades_left.collision_position - \
        1  # pylint: disable=protected-access
    assert test_spades_left.has_collided() is False


def test_has_collided_right():
    """
    Test that collision detected when coming from right
    hand side
    """
    test_spades_right._x_position = \
        test_spades_right.collision_position  # pylint: disable=protected-access
    assert test_spades_right.has_collided() is True


def test_has_not_collided_right():
    """
    Test that collision is not detected when coming from right
    hand side
    """
    test_spades_right._x_position = test_spades_right.collision_position + \
        1  # pylint: disable=protected-access
    assert test_spades_right.has_collided() is False
