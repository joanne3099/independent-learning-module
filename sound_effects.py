import pygame

# Initializes the sound mixer to be used 

pygame.mixer.init()

# Loads the sounds into the game 
bullet_sound = pygame.mixer.Sound('sounds/laser10.wav')
alien_sound = pygame.mixer.Sound('sounds/explosion.wav')
