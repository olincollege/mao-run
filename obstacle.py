from random import choice

class Obstacle:

    x_velocity = {"left": -4, "right": 4}
    starting_location = {"left": 0, "right": 800}
    collision_location = {"left": 300, "right": 425}

    def __init__(self, sprite, actions):
        """
        
        Args:
            sprite: a string containing the name of the sprite.
            actions: a dictionary with the keys as the names of the sprites
                and the values as the expected actions for the given sprites.
        """
        self._sprite = sprite
        self._start_position = choice(["left", "right"])
        self._x_position = self.starting_location[self.start_position]
        self._y_position = 200
        self._collision_position = self.collision_location[self.start_position]
        self._action = actions[sprite]

    @property
    def sprite(self):
        return self._sprite
    
    @property
    def start_position(self):
        return self._start_position

    @property
    def x_position(self):
        return self._x_position

    @property
    def y_position(self):
        return self._y_position
    
    @property
    def collision_position(self):
        return self._collision_position

    @property
    def action(self):
        return self._action

    def update_position(self):
        self._x_position -= self.x_velocity[self.start_position]
    
    def has_collided(self):
        if self.start_position == "left":
            return self.x_position >= self.collision_position
        return self.x_position <= self.collision_position