import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class that represents an alien in the fleet"""
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen

        #Load the alien image and set its rect attribute
        self.image = pygame.image.load('Images/alien.bmp')
        self.rect = self.image.get_rect()

        #Start each alien near th etop left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the aliens exact horizontal position
        self.x = float(self.rect.x)