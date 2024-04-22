import os
from Projectile import Projectile
from Constants import *
import Globals

class StarRodProjectile(Projectile):
    def __init__(self,  startpos, speed):
        Projectile.__init__(self, startpos, 1, "Good Star", (30, 30), os.path.join("images", "Star.png"), 1, speed)

    def update(self, presses):
        Projectile.update(self, presses)
        self.goRight(self.speedX)
        self.goUp(self.speedY)
        
        for sprite in Globals.enemies:
            if (pygame.Rect.colliderect(self.rect, sprite.collisionRect)):
                sprite.changeHealth(-1 * self.damage)
                self.kill()
                del self
