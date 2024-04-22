import pygame
from Constants import *
from abc import ABC, abstractmethod

class Character(ABC, pygame.sprite.Sprite):
    def __init__(self, spriteX, spriteY, collisionX, collisionY, health, name, size, image, colorkey,):
        pygame.sprite.Sprite.__init__(self)
        self.health = health
        self.name = name
        self.size = size
        self.surf = pygame.transform.scale(pygame.image.load(image), size)
        self.surf.set_colorkey(colorkey)
        self.rect = self.surf.get_rect()
        self.rect.x = spriteX
        self.rect.y = spriteY
        self.collisionRect = pygame.Rect(collisionX, collisionY, size[0], size[1])
        self.collisionRect = pygame.Rect.clip(self.collisionRect, self.rect)
        self.surf.fill((255, 255, 255), self.collisionRect)
        
    @property
    def health(self):
        return self._health
    
    # get the value of name
    @property
    def name(self):
        return self._name

    # set the value of health
    @health.setter
    def health(self, val):
        val = 0 if val < 0 else val
        self._health = val

    # set the value of name, defaulting to "player 1" if the name variable has not yet been created and the given name value is invalid
    @name.setter
    def name(self, val):
        if (isinstance(val, str) and len(val) >= 2):
            self._name = val
        else:
            try: 
                self._name = self.name
            except:
                self._name = "player 1"
    
    def changeHealth(self, val):
        self.health += val

    # decrease x by the given value, defaulting to 1 if no value is given
    def goLeft(self, xVal = 1):
        if (not self.rect.x - xVal < 0):
            self.rect.move_ip(-xVal, 0)
            self.collisionRect.move_ip(-xVal, 0)

    # increase x by the given value, defaulting to 1 if no value is given
    def goRight(self, xVal = 1):
        if (not self.rect.x + xVal + self.size[0] > WIDTH):
            self.rect.move_ip(xVal, 0)
            self.collisionRect.move_ip(xVal, 0)


    # decrease y by the given value, defaulting to 1 if no value is given
    def goUp(self, yVal = 1):
        if (not self.rect.y - yVal < 0):
            self.rect.move_ip(0, -yVal)
            self.collisionRect.move_ip(0, -yVal)


    # increase u by the given value, defaulting to 1 if no value is given
    def goDown(self, yVal = 1):
        if (not self.rect.y + yVal + self.size[1] > HEIGHT):
            self.rect.move_ip(0, yVal)
            self.collisionRect.move_ip(0, yVal)

    def setPosition(self, pos):
        if (not (pos[0] < 0 or pos[0] + self.size[0] > WIDTH)):
            self.rect.x = pos[0]
            self.collisionRect.x = pos[0]
        if (not (pos[1] < 0 or pos[1] + self.size[1] > HEIGHT)):
            self.rect.y = pos[1]   
            self.collisionRect.y = pos[1]


    @abstractmethod
    def update(self, presses):
        print("update needs to be overriden!")

    