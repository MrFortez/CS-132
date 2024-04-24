from character import Character
from constants import *
import globals

# a child of the character class, creates a generic projectile.
class Projectile(Character):
    def __init__(self, startPos, health, name, size, image, damage, speed):
        Character.__init__(self, startPos[0], startPos[1], startPos[0], startPos[1], health, name, size, image, (255, 0, 0))
        
        self.damage = damage
        self.speedX = speed[0]
        self.speedY = speed[1]

    # the Projectile's update function, called once every frame by its children's update functions.
    # Any factor shared by all projectiles should be added here
    def update(self, presses):

        # checks if the projectile is offscreen. If it is, it is killed.
        if (self.rect.x < 10 or abs(self.rect.x + self.size[0] - WIDTH) < 10 or self.rect.y < 10 or abs(self.rect.y + self.size[1] - HEIGHT) < 10):
            self.kill()
            del self


