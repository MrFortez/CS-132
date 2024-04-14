# class methods and static methods are things we dont tell yall about in the 130 series

class Gerald:
    
    max_height = 10
    
    #normal methods, methods applied to individual instances
    def jump(self):
        pass
    
    #class method operates on the class itself
    @classmethod
    def set_max_height(cls, value):
        cls.max_height = value
        
    #static methods are just functions in the class that don't have implicitly passed args
    @staticmethod
    def say_hello():
        print("hello")