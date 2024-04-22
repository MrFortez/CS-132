import os
from Projectile import Projectile
from Constants import *
import Globals

class NightmareProjectile(Projectile):
    def __init__(self, speed, startpos):
        Projectile.__init__(self, startpos, 1, "Evil Star", (30, 30), os.path.join("images", "Evil-Star.png"), 1, speed)

    def update(self, presses):
        Projectile.update(self, presses)
        self.goLeft(self.speedX)
        self.goUp(self.speedY)

        for sprite in Globals.players:
            if (pygame.Rect.colliderect(self.rect, sprite.collisionRect)):
                if (not sprite.isInvincible):
                    sprite.changeHealth(-1 * self.damage)
                    sprite.becomeInvincible()
                self.kill()
                del self



