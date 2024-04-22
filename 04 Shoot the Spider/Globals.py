import pygame

# Set up Sprite Groups
players = pygame.sprite.Group()

enemies = pygame.sprite.Group()

playerProjectiles = pygame.sprite.Group()

enemyProjectiles = pygame.sprite.Group()

# Set up the game clock
clock = pygame.time.Clock()
globalTime = pygame.time.get_ticks()