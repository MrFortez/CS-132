# Abstract Methods:
#   Methods that are intended to be implemented in 
#   subclasses of the abstract class.
#   A way of promising the subclasses
#   will implement functionality
#
# Abstract Classes:
#   Classes that are designed to never be instantiated
#   Serves as a template for subclasses
#
# Concrete Classes:
#   Class that can be and are designed to be instantiated
#
#
# 3 Ways to Implement:
#   1: Raise NotImplementedError
#   2: (recommened) Use the ABC class (Abstract Base Class)
#   3: Use ABCMeta (deprecated... don't do this)



## ABC Class ##

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def communicate(self):
        pass

class Bird(Animal):
    def __init__(self) -> None:
        pass

    # def communicate(self):
    #     print("chirp tweet caw")

# a = Animal()  # This will cause an error
b = Bird()
b.communicate()