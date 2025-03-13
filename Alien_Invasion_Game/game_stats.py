class GameStats:
    def __init__(self, ai_game):
        """Initialize the statistics class"""

        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True

        #Start game in an inactive state
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit