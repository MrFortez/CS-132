## Method Lookup ##
# Type of Polymorphism
#   The idea of having different ways to interface with something
#
# Method lookup:
#   A form of polymorphism
#   Used to find the right method to call in a class hierarchy
#   Ex: if a subclass doesnt have the __str__ method but it's 
#       super class does, then the method in the super class 
#       will be called

class Shape:
    def __init__(self, length:int, width:int):
        self.length = length
        self.width = width

    def draw(self):
        for i in range(0, self.width):
            print("*" * self.length)
        print()


class Rectangle(Shape):
    def __init__(self, length: int, width: int):
        super().__init__(length, width)


class Square(Shape):    
    def __init__(self, length: int):
        super().__init__(length, length)


class Triangle(Shape):
    def __init__(self, side: int):
        super().__init__(side, side)

    ## This method is overriding Shape's draw method
    def draw(self):
        for i in range(0, self.length):
            print("*" * (self.length - i))
        print()



r = Rectangle(4, 3)
s = Square(3)
t = Triangle(4)

## These two use the Shape Class' draw() method
r.draw()
s.draw()

## This one uses its own draw() method
t.draw()