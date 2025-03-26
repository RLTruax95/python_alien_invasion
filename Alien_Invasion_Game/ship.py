import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""Class for managing the ship properties"""

	def __init__(self, ai_game):
		"""Initialize the ship and set its starting position"""
		super().__init__()
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.settings = ai_game.settings

		#Load the ship image and get its rect.
		self.image = pygame.image.load('Images/spaceship.bmp')
		self.rect = self.image.get_rect()

		#Start each new ship at the bottom center of the screen
		self.rect.midbottom = self.screen_rect.midbottom

		#Store the horizontal position as a decimal value
		self.x = float(self.rect.x)

		#Movement flags
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Update the ships position based on the movement flag"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.rect.x -= self.settings.ship_speed

	def center_ship(self):
		"""Center the ship on the screen"""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)

		#Update rect object from self.x
		# self.rect.x = self.x  #This command is supposed to be in the program, but prevents the ship from moving

	def blitme(self):
		"""Draw the ship at its current location"""
		self.screen.blit(self.image, self.rect)
