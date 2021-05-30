# this is the main file to run the game
import pygame
# contains the functionality to run a game
from pygame.sprite import Group
# Helps to work with a group of sprites

# this allows to access settings and modify alien invasion
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button

from ship import Ship
import game_functions as gf


def run_game():
    # Intialise pygame, settings and create a screen object.
    pygame.init()

    # Display size of screen and modify it
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion!")

    # Make the play button
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics.
    # And Create scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship, a group of bullets and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Main loop for the game
    while True:
        # Refracted code, now in different programs.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)
        # if the game is active, then update these settings to the screen and update the screen
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb,
                              ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                             bullets)
        # very important to indent this so that it would work 
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                         play_button)


# Calling this function runs the game
run_game()
