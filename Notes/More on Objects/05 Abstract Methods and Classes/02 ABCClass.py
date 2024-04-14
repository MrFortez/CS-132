from abc import ABC, abstractmethod
# ABC = abstract base class

class Animal(ABC):
    def __init__(self):
        """Animal Constructor"""
        
    @abstractmethod   
    def communicate(self):
        """Left to subclass for implementation"""
        
class Bird(Animal):
    
    def __init__(self):
        """Bird Constructor"""
        
    def communicate(self):
        print("chirp tweet caw")
        
#a = Animal()
b= Bird()
b.communicate()
