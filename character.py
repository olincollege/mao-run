"""
Information and functionality of the player sprite.
"""
import pygame

class Character(pygame.sprite.Sprite):
    """
    Create the character sprite for the game.

    Attributes:
        joker_1:
        joker_2:
        joker_moves:
        joker_index:
        image:
        rect:
    """

    def __init__(self):
        """
        Create a new character
        """
        super().__init__()
        # Load player images
        self.joker_1 = pygame.image.load("Sprites/joker2.png")
        self.joker_1 = pygame.transform.scale(self.joker_1, (pygame.display.Info().current_w/5, pygame.display.Info().current_h/2.5))
        self.joker_2 = pygame.image.load("Sprites/joker1.png")
        self.joker_2 = pygame.transform.scale(self.joker_2, (pygame.display.Info().current_w/5, pygame.display.Info().current_h/2.5))

        # Set up animation for player
        self.joker_moves = [self.joker_1, self.joker_2]
        self.joker_index = 0

        self.image = self.joker_moves[int(self.joker_index)]
        self.rect = self.image.get_rect(midbottom = (pygame.display.Info().current_w/2,pygame.display.Info().current_h/11*8))

    def joker_animation(self):
        """
        Animate the joker sprite
        """
        self.joker_index += 0.15
        if self.joker_index >= len(self.joker_moves): self.joker_index = 0
        self.image = self.joker_moves[int(self.joker_index)]
        
    def update(self):
        """
        Update the joker sprite
        """
        self.joker_animation()

        
