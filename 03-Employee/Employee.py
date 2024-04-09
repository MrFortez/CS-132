#####################################################################
# author: Brandon Fortes  
# date: April 8, 2024
# description: 
#####################################################################

# import the abc library to make abstract classes
from abc import ABC, abstractmethod

######################################################################
# An employee class. Its constructor takes the first name, last name and
# pay. It also has email and position as instance variables. It contains
# a single abstract method i.e. applyRaise, and a createEmail function
# that creates an appropriate email address from the employee's first
# and last names.
######################################################################

class Employee(ABC):
    def __init__(self, first, last, pay) -> None:
        super().__init__()
        self.firstname = first
        self.lastname = last
        self.pay = pay
        self.position = None
        self.email = self.createEmail()

    @property
    def firstname(self):
        return self._firstname
    
    @firstname.setter
    def firstname(self, val):
        newFirst = val.strip()
        newFirst = newFirst.lower()
        newFirst = newFirst.title()
        self._firstname = newFirst

    @property
    def lastname(self):
        return self._lastname
    
    @lastname.setter
    def lastname(self, val):
        newLast = val.strip()
        newLast = newLast.lower()
        newLast = newLast.title()
        self._lastname = newLast
    
    @property
    def pay(self):
        return self._pay
    
    @pay.setter
    def pay(self, val):
        self._pay = val if val >= 20000 else 20000

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, val):
        if (val.find("@latech.edu") >= 0):
            self._email = val

    def createEmail(self):
        return f"{self.firstname.lower()}.{self.lastname.lower()}@latech.edu"
    
    @abstractmethod
    def applyRaise(self, rate):
        raise NotImplementedError("applyRaise(rate) needs to be overriden!")

    def __str__(self) -> str:
        return f"{self.lastname}, {self.firstname} ({self.email})"
    
######################################################################
# A faculty class is a subclass of the Employee class above. Its
# constructor receives both names as well as the position. The Faculty
# class also overrides the applyRaise function by multiplying the pay by
# the rate provided as an argument. It also slightly tweaks the __str__
# function in the super class.
######################################################################

class Faculty(Employee):
    def __init__(self, first, last, position):
        super().__init__(first, last, 50000)
        self.position = position

    def applyRaise(self, rate):
        self.pay = rate * self.pay if rate > 0 else self.pay

    def __str__(self) -> str:
        return super().__str__() + f" -- {self.position}"

######################################################################
# A Staff class is a subclass of the Employee class above. Its
# constructor only receives both names. It also overrides the applyraise
# function but adding the increase (provided as the argument) to the
# pay. It doesn't change anything else from the Employee class.
######################################################################

class Staff(Employee):
    def __init__(self, first, last):
        super().__init__(first, last, 40000)

    def applyRaise(self, rate):
        self.pay = rate + self.pay if rate > 0 else self.pay

# f = Faculty("bill ", "boD", "God")
# print(f)