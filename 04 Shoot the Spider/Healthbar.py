import pygame
import sys
from constants import *

# Health bar class
class HealthBar:
    def __init__(self, x, y, width, height, maxHealth, name):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.maxHealth = maxHealth
        self.health = maxHealth
        self.name = name
        self.font = pygame.font.Font(None, 26)

    def draw(self, screen):
        # Calculate the width of the health bar based on current health
        healthRatio = self.health / self.maxHealth
        barWidth = int(self.width * healthRatio)

        # Draw the health bar background
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))
        
        # Draw the health bar filled with green representing current health
        pygame.draw.rect(screen, GREEN, (self.x, self.y, barWidth, self.height))

        # Render text for the name above the health bar
        text_surface = self.font.render(self.name, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.x + self.width // 2, self.y - 10)  # Adjust position of the text above the health bar
        screen.blit(text_surface, text_rect)

    def setHealth(self, health):
        self.health = health




