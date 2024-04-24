import pygame
from character import Character
from constants import *
from nightmareProjectile import NightmareProjectile
from healthbar import HealthBar
import globals
import math

# a child class of character that handles enemies. (In this game there is only one enemy)
class Enemy(Character):
    def __init__(self, health, name, size, image):
        Character.__init__(self, 650, 250, 650, 250, health, name, size, image, (255, 0, 0))

        # creates a health bar for the enemy that will appear on the top right of the screen
        self.healthbar = HealthBar(700, 40, 100, 20, health, name)

        # the state that determines what ai the enemy uses
        self.state = 1

        # this variable is called to determine whether or not the enemy can shoot
        self.canShoot = True

        # this variable is called to determine when the enemy will be allowed to shoot again.
        self.shootCooldown = 0

        self.previousState = 0
        self.animationTimer = 0

        # these are temporary variables used by the ai methods to assist in movement, such as storing angles.
        self.movementHelperOne = 0
        self.movementHelperTwo = 0
        self.movementHelperThree = 0

        # A variable keeping track of whether the enemy is below half health, used in the ai methods to make them harder
        self.isEnraged = False

    # Get the value of the enemy's current state
    @property
    def state(self):
        return self._state
    
    # Set the value of the enemy's current state
    @state.setter
    def state(self, val):
        self._state = val

    # A method every time the enemy changes state. It resets movement helpers and teleports the enemy
    # to a specific position depending on the state
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

    # A method used to determine when the enemy can shoot again. It looks at the shootCooldown variable
    # and checks if the current time is greater than the shootCooldown plus a specified amount of time.
    # For example, if it is given 1000, the enemy will be able to shoot again after 1 second
    def checkShootingCooldown(self, time:int):
        if (not self.canShoot and (self.shootCooldown + time) < globals.globalTime):
            self.canShoot = True

    # Creates a new NightmareProjectile based on the enemy's current position and a given (x, y) speed
    def shootProjectile(self, speed:tuple):
        globals.enemyProjectiles.add(NightmareProjectile(speed, (self.rect.x + (self.size[1] / 2), self.rect.y + (self.size[1] / 2))))

    # Creates a new NightmareProjectile based on the given (x, y) coordinates and a given (x, y) speed
    def shootProjectilePos(self, speed:tuple, startPos:tuple):
        globals.enemyProjectiles.add(NightmareProjectile(speed, startPos))

    # A method that teleports the enemy to the given (x, y) coordinates, then if the enemy canShoot, fires
    # a projectile for each (x, y) speed given to it
    def teleportShot(self, pos:tuple, speeds:tuple, cooldown:int):
        self.setPosition(pos) 
        if (self.canShoot):
            for speed in speeds:
                self.shootProjectile(speed)
            self.canShoot = False
            self.shootCooldown = globals.globalTime
        self.checkShootingCooldown(cooldown)

    # The ai used for state 1. Nightmare will move up and down the screen and fire a single star projectile horizontally
    # towards kirby every half second. If enraged, he'll fire two more star projectiles, one above and one below
    # the original shot. His movement is based on trigonomic functions to make it wavy. 
    def stateOneAi(self):
        self.goUp(int(math.cos(math.radians(self.movementHelperOne)) * 4))
        self.goLeft(int(math.sin(math.radians(self.movementHelperTwo)) * 3))
        self.movementHelperOne += 1
        self.movementHelperTwo += math.pi # (math.pi is used here to give its movements a degree of sudo randomness.)

        self.checkShootingCooldown(500)

        if (self.canShoot):
            self.shootProjectile((5, 0))

            if (self.isEnraged):
                self.shootProjectile((4, 2))
                self.shootProjectile((4, -2))
            self.canShoot = False
            self.shootCooldown = globals.globalTime

    # The ai used for state 2. Nighmare will teleport to 5 different posisitions on the right side of the screen and
    # fire two star projectiles. If enraged, he'll teleport twice as fast. The Times at which he teleports depends on the current
    # animation timer. It divides the current time by the given cooldown, then does modulus to determine the timeframe
    # at which that specific action should occur. This is a technique used in severl of his phases.
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


    # The ai used for state 3. Nightmare will alternate between two attacks. First he will follow Kirby vertically,
    # firing a single star projectile horizontally in a very similar manner to Phase 1. Every few seconds,
    # he will stop firing shots and dash towards kirby, dealing contact damage if he hits kirby, before returning
    # to firing shots. If enraged, he will again fire two more projectiles, and he also dashes
    # more often and faster. It uses a sin function to achieve the slingshot-like effect in the dash.
    # Once the animation helper reaches past 360, the sin function is cut off to ensure that Nightmare
    # returns to the same position that it started the dash.
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
            self.setPosition((600, globals.players.sprites()[0].rect.y))
            if (self.canShoot):
                if (self.isEnraged):
                    self.shootProjectile((5, 2))
                    self.shootProjectile((5, -2))
                
                self.shootProjectile((5, 0))
                self.canShoot = False
                self.shootCooldown = globals.globalTime
            self.checkShootingCooldown(500)


    # This is the ai used for State 4. Nightmare will teleport near the top right of the screen and slowly move down, rapidly
    # firing projectiles horizontally. Once he reaches a bit below the middle of the screen, he teleports to
    # the bottom of the screen, slowly moving up and firing more projectiles. It will then repeat this process. 
    # If enraged, Nightmare will move further before teleporting and changing direction, making the opening to avoid
    # the projectiles smaller.
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
                self.shootCooldown = globals.globalTime
            self.checkShootingCooldown(100)


        if ((self.animationTimer // sweepTimer) % 2 == 1):
            if ((self.previousTime // sweepTimer) % 2 == 0):
                self.setPosition((600, 480))
                
            self.goUp(3)
            if (self.canShoot):
                self.shootProjectile((5, 0))
                self.canShoot = False
                self.shootCooldown = globals.globalTime
            self.checkShootingCooldown(100)

    # This is the ai used for State 5. Nightmare will teleport to the center of the screen and rapidly fire two sets of projectiles 
    # at opposite angles in a circular motion. If enraged, he will fire two more bands of projectiles, those at 
    # 90 degree offsets from the original 2 bands. Trigonomic functions are used to create the circular patterns
    # of the projectiles. They also use the shootProjectilePos() function to ensure that they come from the
    # center of the screen.
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
            self.shootCooldown = globals.globalTime
        self.checkShootingCooldown(200)
        self.movementHelperThree += 0.5

    # This is the ai used for State 6. Nightmare will circle the outer edges of the screen, occasionally firing projectiles 
    # towards the center of the screen. If enraged, he will fire twice as many projectiles. Trig functions are used
    # to have Nightmare circle around the screen. The intervals at which he fires a shot is the sane as the angle
    # given to the trig function.
    def stateSixAi(self):
        self.goUp(int(math.cos(math.radians(self.movementHelperOne)) * 5))
        self.goLeft(int(math.sin(math.radians(self.movementHelperTwo)) * 6.2))
        self.movementHelperOne += 1
        self.movementHelperTwo += 1
        
        if (self.isEnraged):
            match self.movementHelperOne % 360:
                case 60:
                    self.shootProjectile((0, -3))
                case 100:
                    self.shootProjectile((0, -3))
                case 150:
                    self.shootProjectile((-3, 0))
                case 190:
                    self.shootProjectile((-3, 0))
                case 240:
                    self.shootProjectile((0, 3))
                case 280:
                    self.shootProjectile((0, 3))
                case 340:
                    self.shootProjectile((3, 0))
                case 20:
                    self.shootProjectile((3, 0))
        else:
            match self.movementHelperOne % 360:
                case 80:
                    self.shootProjectile((0, -3))
                case 170:
                    self.shootProjectile((-3, 0))
                case 260:
                    self.shootProjectile((0, 3))
                case 0:
                    self.shootProjectile((3, 0))

    # The Enemy's update function, which is called every frame (120 fps)
    def update(self, presses):
        # Update the enemy's animation timer. Its the same as the global time, just moded by 60000 (1 minute) for smooth math
        # in the ai function
        self.animationTimer = globals.globalTime % 60000

        # Update the state based on the current time (i.e. every ten seconds)
        self.state = (self.animationTimer // 10000) % 6

        # If from the previous frame to the current frame the state has changed, call the initializeNewState() function
        if (self.previousState != self.state):
            self.initializeNewState()

        # Determine whether the enemy is enraged
        if (not self.isEnraged and self.health < self.healthbar.maxHealth / 2):
            self.isEnraged = True

        # Run the ai 
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

        # keep track of the previous states and times
        self.previousState = self.state
        self.previousTime = self.animationTimer

        # update healthbar
        self.healthbar.setHealth(self.health)
        