## Multiple Inheritance ##
# When a class DIRECTLY inherits from more than one
# super class.
#
# What it is not:
#   when a class has 1 super class and that
#   super class has 1 super class

class Bread: 
    def __init__(self, flourType:str, isMoldy:bool):
        self.flourType = flourType
        self.isMoldy = isMoldy

    def __str__(self) -> str:
        return f"Flour: {self.flourType}; Moldy: {self.isMoldy}"
    
class SaleItem:
    def __init__(self, price:float):
        self.price = price

    def __str__(self) -> str:
        return f"Price: {self.price}"
    
class Bun(Bread, SaleItem):
    def __init__(self):
        Bread.__init__(self, "Wheat", False)
        SaleItem.__init__(self, 20.00)

    def __str__(self) -> str:
        return f"Bun: {self.flourType}; Price: {self.price}"

bunnyBun = Bun()

print(bunnyBun)