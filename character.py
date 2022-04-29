"""
Information and functionality of the player sprite.
"""
import pygame

class Character(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Sprites/joker2.png")
        self.rect = self.image.get_rect(midbottom = (80,300))
