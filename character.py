"""
Information and functionality of the player sprite.
"""
import pygame


class Character(pygame.sprite.Sprite):
    """
    Create the character sprite for the game.

    Attributes:
        infoObject:
        screen_width:
        screen_height:
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
        # Fetch screen info
        self.infoObject = pygame.display.Info()
        self.screen_width = self.infoObject.current_w/2
        self.screen_height = self.infoObject.current_h/2
        
        # Load player images
        self.joker_1 = pygame.image.load("Sprites/joker2.png")
        self.joker_1 = pygame.transform.scale(self.joker_1, (self.screen_width/5, self.screen_height/2.5))
        self.joker_2 = pygame.image.load("Sprites/joker1.png")
        self.joker_2 = pygame.transform.scale(self.joker_2, (self.screen_width/5, self.screen_height/2.5))

        # Set up animation for player
        self.joker_moves = [self.joker_1, self.joker_2]
        self.joker_index = 0

        self.image = self.joker_moves[int(self.joker_index)]
        self.rect = self.image.get_rect(midbottom = (self.screen_width/2, self.screen_height*.73))

    def joker_animation(self):
        """
        Animate the joker sprite
        """
        self.joker_index += 0.15
        if self.joker_index >= len(self.joker_moves):
            self.joker_index = 0
        self.image = self.joker_moves[int(self.joker_index)]

    def update(self):
        """
        Update the joker sprite
        """
        self.joker_animation()
