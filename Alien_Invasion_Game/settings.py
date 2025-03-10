class Settings:
	"""A class to store all settings for alien invasion"""

	def __init__(self):
		"""Initialize the settings class"""
		#Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		#Bullet settings
		self.bullet_speed = 0.8
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3

		#Alien settings
		self.alien_speed = 0.25
		self.fleet_drop_speed = 10
		#Fleet direction 1 = right, -1 = left
		self.fleet_direction = 1

		#Ship settings
		self.ship_limit = 3
		self.ship_speed = 1.0