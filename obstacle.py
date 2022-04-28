class Obstacle:

    velocity = 4

    def __init__(self, sprite, actions):
        """
        
        Args:
            sprite: a string containing the name of the sprite.
            actions: a dictionary with the keys as the names of the sprites
                and the values as the expected actions for the given sprites.
        """
        self._sprite = sprite
        self._x_position = 800
        self._y_position = 600
        self._action = actions[sprite]

    @property
    def sprite(self):
        return self._sprite

    @property
    def x_position(self):
        return self._x_position

    @property
    def y_position(self):
        return self._y_position

    @property
    def action(self):
        return self._action

    def update_position(self):
        self._x_position -= self.velocity