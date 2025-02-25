import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
	"""Class for managing the game assets"""
	def __init__(self):
		"""Initialize the game and create the resources"""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)

	def run_game(self):
		"""Start the main loop for the game"""
		while True:
			#used to watch the keyboard and mouse
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			#Redraw the screen during each pass through the loop
			self.screen.fill(self.settings.bg_color)
			self.ship.blitme()

			#Makes the most recent screen visible
			pygame.display.flip()

if __name__ == '__main__':
	#Make a game instance and run the game
	ai = AlienInvasion()
	ai.run_game()