import pygame

class Character(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((800,300))
        self.image.fill('Black')
        self.rect = self.image.get_rect(midbottom = (200,300))
    
    location = "" # location of character all of the time

    def __init__(self):
        self.sprite = "" # assign sprite value / filepath
