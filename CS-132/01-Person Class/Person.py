#####################################################################
# author: Brandon Fortes
# date: March 18, 2024
# description: A class that constructs Person objects with names and 2d positions
#####################################################################

# math import
import math

# global Constants to restrict the maximum x and y values that a person object
# can have.
MAX_X = 800
MAX_Y = 600

# A class representing a person. A person can be initialized with a
# name, as well as x and y coordinates. However, there are default
# values for all those (i.e. player 1, 0 and 0 respectively). A person
# also has a size which is set to 1 by default. A person can go left, 
# go right, go up and go down. A person also has a string function 
# that prints out their name location, and size. A person also has a 
# function that calculates the euclidean distance from another person 
# object.
class Person:
    def __init__(self, name = "player 1", x = 0, y = 0):
        self.name = name
        self.x = x
        self.y = y
        self.size = 1

    # get the value of name
    @property
    def name(self):
        return self._name
    
    # get the value of x    
    @property
    def x(self):
        return self._x
    
    # get the value of y
    @property
    def y(self):
        return self._y
    
    # get the value of size
    @property
    def size(self):
        return self._size
    
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

    # set the value of x, clamping the value between 0 and the max x value
    @x.setter
    def x(self, val):
        val = 0 if val < 0 else val
        val = MAX_X if val > MAX_X else val
        self._x = val

    # set the value of y, clamping the value between 0 and the max y value
    @y.setter
    def y(self, val):
        val = 0 if val < 0 else val
        val = MAX_Y if val > MAX_Y else val
        self._y = val

    # set the value of size, only if the given value is at least 1
    @size.setter
    def size(self, val):
        if (val >= 1):
            self._size = val

    # decrease x by the given value, defaulting to 1 if no value is given
    def goLeft(self, xVal = 1):
        self.x -= xVal

    # increase x by the given value, defaulting to 1 if no value is given
    def goRight(self, xVal = 1):
        self.x += xVal

    # decrease y by the given value, defaulting to 1 if no value is given
    def goUp(self, yVal = 1):
        self.y -= yVal

    # increase u by the given value, defaulting to 1 if no value is given
    def goDown(self, yVal = 1):
        self.y += yVal

    # calculate and return the distance between this Person object and another given Person object
    def getDistance(self, other):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
    
    # print associated instance variables
    def __str__(self):
        return f"Person({self.name}):     size = {self.size},     x = {self.x}   y = {self.y}"

