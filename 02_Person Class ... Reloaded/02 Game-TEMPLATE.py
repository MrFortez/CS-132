#####################################################################
# author: Brandon Fortes
# date: April 2, 2024
# description: 
#####################################################################

import pygame
from random import randint, choice

from pygame.sprite import Group
from Item import *
from Constants import *


class Person(pygame.sprite.Sprite, Item):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        Item.__init__(self)
        self.surf = pygame.Surface((self.size, self.size))
        self.color = BLACK

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, val):
        self._color = val

    @property
    def surf(self):
        return self._surf
    
    @surf.setter
    def surf(self, val):
        self._surf = val

    def setColor(self):
        self.color = COLORS[randint(0, 4)]
        self.surf.fill(self.color)

    def setSize(self):
        self.size = randint(10, 100)
        self.surf = pygame.Surface((self.size, self.size))  

    def update(self, presses):
        if (presses[K_UP]):
            self.goUp()

        elif (presses[K_DOWN]):
            self.goDown()

        elif (presses[K_LEFT]):
            self.goLeft()

        elif (presses[K_RIGHT]):
            self.goRight()

        elif (presses[K_SPACE]):
            self.setSize()
            self.setColor()

        if  (self.y < 0):
            self.y = 0

        if (self.x > WIDTH ):
            self.x = WIDTH
            
        if (self.x  < 0):
            self.x = 0 
            
        if  (self.y > HEIGHT):
            self.y = HEIGHT
        
    def setRandomPosition(self):
        self.x = randint(0, WIDTH)
        self.y = randint(0, HEIGHT)

    def getPosition(self):
        return (self.x - (self.size / 2), self.y - (self.size / 2))
    
    def __str__(self):
        return super().__str__() + f" Color: {self.color}"

        


########################### main game ################################
# DO NOT CHANGE ANYTHING BELOW THIS LINE
#####################################################################

# Initialize pygame library and display
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a person object
p = Person()
RUNNING = True  # A variable to determine whether to get out of the
                # infinite game loop

while (RUNNING):
    # Look through all the events that happened in the last frame to see
    # if the user tried to exit.
    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_ESCAPE):
            RUNNING = False
        elif (event.type == QUIT):
            RUNNING = False
        elif (event.type == KEYDOWN and event.key == K_SPACE):
            print(p)

    # Otherwise, collect the list/dictionary of all the keys that were
    # pressed
    pressedKeys = pygame.key.get_pressed()
    
    # and then send that dictionary to the Person object for them to
    # update themselves accordingly.
    p.update(pressedKeys) 

    # fill the screen with a color
    screen.fill(WHITE)
    # then transfer the person to the screen
    screen.blit(p.surf, p.getPosition())
    pygame.display.flip()

