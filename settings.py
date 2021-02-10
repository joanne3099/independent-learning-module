import pygame


class Settings():
    """ Class to store all the settings for Alien Invasion"""

    def __init__(self):
        """ Initialise the game's static settings."""

        # Scoring
        self.alien_points = 50

        # Alien settings
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 6
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_image = pygame.image.load('images/moon.bmp')
        self.bg_colour = (0, 0, 0)

        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 2  # travel slightly slower than ship
        self.bullet_width = 8
        self.bullet_height = 15
        self.bullet_colour = 255, 255, 255  # white
        self.bullets_allowed = 3

        # How quickly the game speeds up
        self.speedup_scale = 1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        """Intialise settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet directions of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        # Multiply each speed setting by the speedup scale.
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
