
class Obstacle:

    velocity = 5

    def __init__(self, sprite, actions):
        """
        
        Args:
            sprite: a string containing the name of the sprite.
            actions: a dictionary with the keys as the names of the sprites
                and the values as the expected actions for the given sprites.
        """
        self.sprite = sprite
        self.location = "" # location on screen
        self.action = actions[sprite]