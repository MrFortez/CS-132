import os
from character import Character
from constants import *
from starRodProjectile import StarRodProjectile
from healthbar import HealthBar
import globals

# a child of the character class that handles the player. 
class Player(Character):
    def __init__(self, health, name, size, image):
        Character.__init__(self, 100, 100, 100, 135, health, name, size, image, ((255, 0, 0)))

        # creates a health bar for the player that will appear on the top left of the screen
        self.healthbar = HealthBar(0, 40, 100, 20, health, name)

        # this variable is called to determine whether or not the player can shoot
        self.canShoot = True
        
        # this variable is called to determine when the enemy will be allowed to shoot again.
        self.shootCooldown = 0

        # Determines whether or not the player can take damange
        self.isInvincible = False

        # Determines when the player's invincibility will wear off
        self.invincibilityCooldown = 0

    # A method used to determine when the Player can shoot again. It looks at the shootCooldown variable
    # and checks if the current time is greater than the shootCooldown plus a specified amount of time.
    # For example, if it is given 1000, the Player will be able to shoot again after 1 second
    def checkShootingCooldown(self, time:int):
        if (not self.canShoot and (self.shootCooldown + time) < globals.globalTime):
            self.canShoot = True

    # called immediately after the player takes damage, and makes them invincible
    def becomeInvincible(self):
        self.isInvincible = True
        self.invincibilityCooldown = globals.globalTime

    # A method used to determine when the Player can get hit again. Uses the same logic as the shootCooldown.
    def checkInvincibilityCooldown(self, time:int):
        if (self.isInvincible and self.invincibilityCooldown + time < globals.globalTime):
            self.isInvincible = False

        # the update function for the player, called every frame (120 fps)
    def update(self, presses):

        # Player can shoot every half second.
        self.checkShootingCooldown(500)

        # Fires a projectile from in front of the player horizontally to the right.
        # The {self.rect.x < 720} is used to account for a bug where if a projectile
        # is shot on the far right edge of the screen, it will not despawn.
        # This failsafe keeps you from firing too close to the right edge of the screen
        if (presses[K_SPACE] and self.canShoot and self.rect.x < 720):
            globals.playerProjectiles.add(StarRodProjectile((self.rect.x + 50, self.rect.y + 25), (5, 0)))
            self.canShoot = False
            self.shootCooldown = globals.globalTime

        # player's movement controls
        if (presses[K_UP]):
            self.goUp(3)

        elif (presses[K_DOWN]):
            self.goDown(3)

        if (presses[K_LEFT]):
            self.goLeft(3)

        elif (presses[K_RIGHT]):
            self.goRight(3)
            
        # These ensure the player doesnt go offscreen
        if  (self.rect.y < 0):
            self.rect.y = 0

        if (self.rect.x > WIDTH ):
            self.rect.x = WIDTH
            
        if (self.rect.x  < 0):
            self.rect.x = 0 
            
        if  (self.rect.y > HEIGHT):
            self.rect.y = HEIGHT

        # if the player is not invincible and collides with an enemy, take damage and become invincible
        if (not self.isInvincible):
            for sprite in globals.enemies:
                if (pygame.Rect.colliderect(self.collisionRect, sprite.collisionRect)):
                    self.changeHealth(-1)
                    self.becomeInvincible()

        # Player has 2 seconds worth of an invincibility grace period before they can get hit again
        self.checkInvincibilityCooldown(2000)

        # update the player's health bar
        self.healthbar.setHealth(self.health)