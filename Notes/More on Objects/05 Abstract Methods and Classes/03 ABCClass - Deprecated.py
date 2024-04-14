import abc 

class Animal(metaclass = abc.ABCMeta):
    def __init__(self):
        """Animal Stuff"""
        
    @abc.abstractclassmethod
    def communicate(self):
        """Communicating"""
        
# bird and such...