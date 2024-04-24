import os
from projectile import Projectile
from constants import *
import globals

# a child of the Projectile class, used by the Player class.
class StarRodProjectile(Projectile):
    def __init__(self,  startpos, speed):
        Projectile.__init__(self, startpos, 1, "Good Star", (30, 30), os.path.join("images", "Star.png"), 1, speed)

    # the update function for StarRodProjectiles. Called every frame (120 fps)
    def update(self, presses):
        Projectile.update(self, presses)
        self.goRight(self.speedX)
        self.goUp(self.speedY)
        
        #if this sprite collides wtih an enemy, deal damage to the enemy and kill the sprite
        for sprite in globals.enemies:
            if (pygame.Rect.colliderect(self.rect, sprite.collisionRect)):
                sprite.changeHealth(-1 * self.damage)
                self.kill()
                del self
