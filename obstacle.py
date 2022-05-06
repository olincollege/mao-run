"""
Implement obstacles.
"""
from random import choice

class Obstacle:
    """
    Create an obstacle.

    Attributes:
        X_VELOCITY: A dictionary with the keys as strings representing
            the start side of the screen and the values as integers
            representing the respective velocities.
        STARTING_LOCATION: A dictionary with the keys as strings representing
            the start side of the screen and the values as the starting
            positions of the obstacles.
        COLLISION_LOCATION: A dictionary with the keys as strings representing
            the start side of the screen and the values as locations of
            collision with character.
        _sprite: A string representing the name of the obstacle.
        _start_position: A string representing the side of the screen
            at which the obstacle started.
        _x_position: An integer representing the appropriate beginning x
            position for the obstacle.
        _y_position: An integer representing the y position for the obstacle.
        _collision_position: An integere representing the x-coordinate at which
            the obstacle collides with the character.
        _action: A pygame event representing the desired key press for the obstacle.
    """
    X_VELOCITY = {"left": -4, "right": 4}
    STARTING_LOCATION = {"left": 0, "right": 800}
    COLLISION_LOCATION = {"left": 300, "right": 425}

    def __init__(self, sprite, actions, start_position=None):
        """
        
        Args:
            sprite: a string containing the name of the sprite.
            actions: a dictionary with the keys as the names of the sprites
                and the values as the expected actions for the given sprites.
            start_position: a string representing the desired side of the screen
                at which to start; the default value is a random choice.
        """
        self._sprite = sprite
        if start_position is None:
            start_position = choice(["left", "right"])
        self._start_position = start_position
        self._x_position = self.STARTING_LOCATION[self.start_position]
        self._y_position = 200
        self._collision_position = self.COLLISION_LOCATION[self.start_position]
        self._action = actions[sprite]

    @property
    def sprite(self):
        """
        Create a sprite property for Obstacle.
        """
        return self._sprite
    
    @property
    def start_position(self):
        """
        Create a start_position property for Obstacle.
        """
        return self._start_position

    @property
    def x_position(self):
        """
        Create an x-position property for Obstacle.
        """
        return self._x_position

    @property
    def y_position(self):
        """
        Create a y-position property for Obstacle.
        """
        return self._y_position
    
    @property
    def collision_position(self):
        """
        Create a collision_position property for Obstacle.
        """
        return self._collision_position

    @property
    def action(self):
        """
        Create an action property for Obstacle.
        """
        return self._action

    def update_position(self):
        """
        Update the x-position of the obstacle using appropriate velocity.
        """
        self._x_position -= self.X_VELOCITY[self.start_position]
    
    def has_collided(self):
        """
        Determine if the obstacle has collided with the character.
        """
        # if the obstacle begins of the left, it's position must not exceed
        # the collision_position
        if self.start_position == "left":
            return self.x_position >= self.collision_position
        # if the obstacle begins on the right, it's position must not be
        # less than the collision_position
        return self.x_position <= self.collision_position