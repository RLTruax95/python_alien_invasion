class Settings:
	"""A class to store all settings for alien invasion"""

	def __init__(self):
		"""Initialize the games static settings"""
		#Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		#Bullet settings
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3

		#Alien settings
		self.fleet_drop_speed = 10

		#Ship settings
		self.ship_limit = 3

		#How quickly the game will speed up
		self.speedup_scale = 1.1

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initialize the settings that can change during the game"""
		self.ship_speed = 1.0
		self.bullet_speed = 0.8
		self.alien_speed = 0.25

		# Fleet direction 1 = right, -1 = left
		self.fleet_direction = 1

	def increase_speed(self):
		"""Increase the speed settings"""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale