import pygame
from random import choice

class Game:

    actions = ["up", "down", "left", "right"]

    def __init__(self):
        self.world = "" # create world instance
        self.obstacle_actions = {
            "square": choice(self.actions),
            "rectangle": choice(self.actions),
            "triangle": choice(self.actions),
            "circle": choice(self.actions),
        }
        self.obstacles = [] # create obstacle instances
        self.character = "" # create character instance
    
    def game_over():
        pass

    def restart():
        pass
    
    def update_obstacles():
        pass
