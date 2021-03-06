import pygame
from pygame.sprite import Sprite
# this is so that you can manipulate the images on the screen
# the rect. refers to rectangular coordinates, referring to pixels essentially

class Ship(Sprite):

    def __init__(self, ai_settings, screen):

        """Initialise the ship and set its starting position"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load ship image and get its rect
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom of centre of scren
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for ship's centre.
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draws the ship at its current location on screen."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Centre the ship on the screen."""
        self.center = self.screen_rect.centerx
