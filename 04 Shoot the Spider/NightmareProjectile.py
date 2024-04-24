import os
from projectile import Projectile
from constants import *
import globals

# a child of the Projectile class, used by the Enemy class.
class NightmareProjectile(Projectile):
    def __init__(self, speed, startpos):
        Projectile.__init__(self, startpos, 1, "Evil Star", (30, 30), os.path.join("images", "Evil-Star.png"), 1, speed)

    # the update function for NightmareProjectiles. Called every frame (120 fps)
    def update(self, presses):
        Projectile.update(self, presses)
        self.goLeft(self.speedX)
        self.goUp(self.speedY)

        # if this sprite collides wtih the player, kill the sprite. If the player is not invincible, deal
        # damage to the player and make them invincible
        for sprite in globals.players:
            if (pygame.Rect.colliderect(self.rect, sprite.collisionRect)):
                if (not sprite.isInvincible):
                    sprite.changeHealth(-1 * self.damage)
                    sprite.becomeInvincible()
                self.kill()
                del self



