import os
from Character import Character
from Constants import *
from StarRodProjectile import StarRodProjectile
from Healthbar import HealthBar
import Globals


class Player(Character):
    def __init__(self, health, name, size, image):
        Character.__init__(self, 100, 100, 100, 135, health, name, size, image, ((255, 0, 0)))
        self.healthbar = HealthBar(0, 40, 100, 20, health, name)
        self.canShoot = True
        self.shootCooldown = 0
        self.isInvincible = False
        self.invincibilityCooldown = 0

    def becomeInvincible(self):
        self.isInvincible = True
        self.invincibilityCooldown = Globals.globalTime

    def update(self, presses):
        if (not self.canShoot and self.shootCooldown + 500 < Globals.globalTime):
            self.canShoot = True

        if (presses[K_SPACE] and self.canShoot and self.rect.x < 720):
            Globals.playerProjectiles.add(StarRodProjectile((self.rect.x + 50, self.rect.y + 25), (5, 0)))
            self.canShoot = False
            self.shootCooldown = Globals.globalTime

        if (presses[K_UP]):
            self.goUp(3)

        elif (presses[K_DOWN]):
            self.goDown(3)

        if (presses[K_LEFT]):
            self.goLeft(3)

        elif (presses[K_RIGHT]):
            self.goRight(3)
            
        if  (self.rect.y < 0):
            self.rect.y = 0

        if (self.rect.x > WIDTH ):
            self.rect.x = WIDTH
            
        if (self.rect.x  < 0):
            self.rect.x = 0 
            
        if  (self.rect.y > HEIGHT):
            self.rect.y = HEIGHT

        if (not self.isInvincible):
            for sprite in Globals.enemies:
                if (pygame.Rect.colliderect(self.collisionRect, sprite.collisionRect)):
                    self.changeHealth(-1)
                    self.becomeInvincible()

        if (self.isInvincible and self.invincibilityCooldown + 2000 < Globals.globalTime):
            self.isInvincible = False

        self.healthbar.setHealth(self.health)