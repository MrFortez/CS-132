import pygame
from Character import Character
from Constants import *
from NightmareProjectile import NightmareProjectile
from Healthbar import HealthBar
import Globals
import math

class Enemy(Character):
    def __init__(self, health, name, size, image):
        Character.__init__(self, 650, 250, 650, 250, health, name, size, image, (255, 0, 0))
        self.healthbar = HealthBar(700, 40, 100, 20, health, name)
        self.state = 1
        self.canShoot = True
        self.shootCooldown = 0
        self.previousState = 0
        self.animationTimer = 0
        self.movementHelperOne = 0
        self.movementHelperTwo = 0
        self.movementHelperThree = 0
        self.isEnraged = False

    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, val):
        self._state = val

    def initializeNewState(self):
        self.movementHelperOne = 0
        self.movementHelperTwo = 0        
        self.movementHelperThree = 0
        if (self.state == 3):
            self.setPosition((600, 20))

        if (self.state == 4):
            self.setPosition((337, 250))

        if (self.state == 0):
            self.setPosition((650, 250))

    def shootingCooldown(self, time:int):
        if (not self.canShoot and (self.shootCooldown + time) < Globals.globalTime):
            self.canShoot = True

    def shootProjectile(self, speed):
        Globals.enemyProjectiles.add(NightmareProjectile(speed, (self.rect.x + (self.size[1] / 2), self.rect.y + (self.size[1] / 2))))

    def shootProjectilePos(self, speed, startPos):
        Globals.enemyProjectiles.add(NightmareProjectile(speed, startPos))

    def teleportShot(self, pos, speeds, cooldown):
        self.setPosition(pos) 
        if (self.canShoot):
            for speed in speeds:
                self.shootProjectile(speed)
            self.canShoot = False
            self.shootCooldown = Globals.globalTime
        self.shootingCooldown(cooldown)

    def stateOneAi(self):
        self.goUp(int(math.cos(math.radians(self.movementHelperOne)) * 4))
        self.goLeft(int(math.sin(math.radians(self.movementHelperTwo)) * 3))
        self.movementHelperOne += 1
        self.movementHelperTwo += math.pi

        self.shootingCooldown(500)

        if (self.canShoot):
            self.shootProjectile((5, 0))

            if (self.isEnraged):
                self.shootProjectile((4, 2))
                self.shootProjectile((4, -2))
            self.canShoot = False
            self.shootCooldown = Globals.globalTime


    def stateTwoAi(self):
        if (self.isEnraged):
            teleportCooldown = 200
        else:
            teleportCooldown = 400

        if ((self.animationTimer // teleportCooldown) % 5 == 0):
            self.teleportShot((500, 20), ((4, -2), (3, -4)), 400)

        elif ((self.animationTimer // teleportCooldown) % 5 == 1):
            self.teleportShot((600, 100), ((4, -1), (3, -3)), 400)

        elif ((self.animationTimer // teleportCooldown) % 5 == 2):
            self.teleportShot((700, 250), ((4, 2), (4, -2)), 400)
    
        elif ((self.animationTimer // teleportCooldown) % 5 == 3):
            self.teleportShot((600, 400), ((4, 1), (3, 3)), 400)

        elif ((self.animationTimer // teleportCooldown) % 5 == 4):
            self.teleportShot((500, 480), ((4, 2), (3, 4)), 400)


    def stateThreeAi(self):
        if (self.isEnraged):
            chargeCooldown = 1500
            speedMultiplier = 1.3
        else:
            chargeCooldown = 2000
            speedMultiplier = 1
                
        if ((self.animationTimer // chargeCooldown) % 2 == 0):
            self.movementHelperTwo = 0

        if ((self.animationTimer // chargeCooldown) % 2 == 1 and self.movementHelperTwo < 361):
            self.goLeft(int(math.sin(math.radians(self.movementHelperTwo)) * 11 * speedMultiplier))
            self.movementHelperTwo += 2 * speedMultiplier
        else:
            self.setPosition((600, Globals.players.sprites()[0].rect.y))
            if (self.canShoot):
                if (self.isEnraged):
                    self.shootProjectile((5, 2))
                    self.shootProjectile((5, -2))
                
                self.shootProjectile((5, 0))
                self.canShoot = False
                self.shootCooldown = Globals.globalTime
            self.shootingCooldown(500)


    def stateFourAi(self):
        if (self.isEnraged):
            sweepTimer = 800
        else:
            sweepTimer = 600
            
        if ((self.animationTimer // sweepTimer) % 2 == 0):
            if ((self.previousTime // sweepTimer) % 2 == 1):
                self.setPosition((600, 20))

            self.goDown(3)
            if (self.canShoot):
                self.shootProjectile((5, 0))
                self.canShoot = False
                self.shootCooldown = Globals.globalTime
            self.shootingCooldown(100)


        if ((self.animationTimer // sweepTimer) % 2 == 1):
            if ((self.previousTime // sweepTimer) % 2 == 0):
                self.setPosition((600, 480))
                
            self.goUp(3)
            if (self.canShoot):
                self.shootProjectile((5, 0))
                self.canShoot = False
                self.shootCooldown = Globals.globalTime
            self.shootingCooldown(100)


    def stateFiveAi(self):
        if (self.canShoot):
            self.shootProjectilePos((
                int(math.cos(math.radians(self.movementHelperThree + 45)) * 5), 
                int(math.sin(math.radians(self.movementHelperThree + 45)) * 5)),
                (373, 285))
            self.shootProjectilePos((
                int(math.cos(math.radians(self.movementHelperThree + 225)) * 5), 
                int(math.sin(math.radians(self.movementHelperThree + 225)) * 5)),
                (373, 285))
            if (self.isEnraged):
                self.shootProjectilePos((
                    int(math.cos(math.radians(self.movementHelperThree + 135)) * 5), 
                    int(math.sin(math.radians(self.movementHelperThree + 135)) * 5)),
                    (373, 285))
                self.shootProjectilePos((
                    int(math.cos(math.radians(self.movementHelperThree + 315)) * 5), 
                    int(math.sin(math.radians(self.movementHelperThree + 315)) * 5)),
                    (373, 285))

            self.canShoot = False
            self.shootCooldown = Globals.globalTime
        self.shootingCooldown(200)
        self.movementHelperThree += 0.5


    def stateSixAi(self):
        self.goUp(int(math.cos(math.radians(self.movementHelperOne)) * 5))
        self.goLeft(int(math.sin(math.radians(self.movementHelperTwo)) * 6.2))
        self.movementHelperOne += 1
        self.movementHelperTwo += 1
        
        if (self.isEnraged):
            if (self.movementHelperOne % 360 == 60):
                self.shootProjectile((0, -3))

            elif (self.movementHelperOne % 360 == 100):
                self.shootProjectile((0, -3))

            elif (self.movementHelperOne % 360 == 150):
                self.shootProjectile((-3, 0))

            elif (self.movementHelperOne % 360 == 190):
                self.shootProjectile((-3, 0))
            
            elif (self.movementHelperOne % 360 == 240):
                self.shootProjectile((0, 3))

            elif (self.movementHelperOne % 360 == 280):
                self.shootProjectile((0, 3))

            elif (self.movementHelperOne % 360 == 340):
                self.shootProjectile((3, 0))

            elif (self.movementHelperOne % 360 == 20):
                self.shootProjectile((3, 0))
        else:
            if (self.movementHelperOne % 360 == 80):
                self.shootProjectile((0, -3))

            elif (self.movementHelperOne % 360 == 170):
                self.shootProjectile((-3, 0))

            elif (self.movementHelperOne % 360 == 260):
                self.shootProjectile((0, 3))

            elif (self.movementHelperOne % 360 == 0):
                self.shootProjectile((3, 0))

        




    def update(self, presses):
        self.animationTimer = Globals.globalTime % 60000
        self.state = (self.animationTimer // 10000) % 6

        if (self.previousState != self.state):
            self.initializeNewState()

        if (not self.isEnraged and self.health < 50):
            self.isEnraged = True

        match self.state:
            case 0:
                self.stateOneAi()
            case 1:
                self.stateTwoAi()
            case 2:
                self.stateThreeAi()
            case 3:
                self.stateFourAi()
            case 4:
                self.stateFiveAi()
            case 5:
                self.stateSixAi()

        self.previousState = self.state
        self.previousTime = self.animationTimer

        self.healthbar.setHealth(self.health)