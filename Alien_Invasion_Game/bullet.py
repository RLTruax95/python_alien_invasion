import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage the bullets fired from the ship"""

    def __init__(self, ai_game):
        """Initialize the bullet and set its starting position"""
        super().__init__()
        self.screen_width = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Create a bullet rectangle at (0,0) and then set the correct position
        self.rect = pygame.Rect(0, 0, self.settings.screen_width,
                                self.settings.screen_height)
        self.rect.midtop = ai_game.ship_rect.midtop

        #Store the bullets position as a decimal value
        self.y = float(self.rect.y)