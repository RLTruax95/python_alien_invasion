import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
	"""Class for managing the game assets"""
	def __init__(self):
		"""Initialize the game and create the resources"""
		pygame.init()
		self.settings = Settings()

		# allows the game ot be displayed in fullscreen
		# self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		# self.settings.screen_width = self.screen.get_rect().width
		# self.settings.screen_height = self.screen.get_rect().height

		#Allows the game to be played in a defined window size
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
# --------------------------------------------------------------------------
	def run_game(self):
		"""Start the main loop for the game"""
		while True:
			self._check_events()
			self.ship.update()
			self._update_bullets()
			self._update_screen()
# --------------------------------------------------------------------------
	def _check_events(self):
		"""Responds to key presses and mouse events"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
#--------------------------------------------------------------------------
	def _check_keydown_events(self, event):
		"""Responds to keyboard events"""
		if event.key == pygame.K_RIGHT:
			# Move the ship to the right
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			# Move the ship to the right
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			#quit the game if 'Q' is pressed
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
# --------------------------------------------------------------------------
	def _check_keyup_events(self, event):
		"""Responds to keyboard events"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False
# --------------------------------------------------------------------------
	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullets group"""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)
# --------------------------------------------------------------------------
	def _update_bullets(self):
		"""Update the position of the bullets and remove old bullets"""
		#Update the bullet position
		self.bullets.update()

		# Get rid of bullets that have disappeared
		for bullets in self.bullets.copy():
			if bullets.rect.bottom <= 0:
				self.bullets.remove(bullets)
# --------------------------------------------------------------------------
	def _update_screen(self):
		"""Updates the images on screen and flips the new image"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		# Makes the most recent screen visible
		pygame.display.flip()
# --------------------------------------------------------------------------
if __name__ == '__main__':
	# Make a game instance and run the game
	ai = AlienInvasion()
	ai.run_game()