class Animal:
    def __init__(self):
        """What it mens to be an animal"""
        
    def communicate(self):
        raise NotImplementedError("Communicate not implemented in subclass!")

class Bird(Animal):
    def __init__(self):
        """What it means to be a bird"""
        
    #def communicate(self):
        #print("tweet tweet caw caw chirp chirp")
        

a = Animal()
b = Bird()
b.communicate()
