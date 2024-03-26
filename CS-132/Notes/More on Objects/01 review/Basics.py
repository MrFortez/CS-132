## Basics and Review ##

class House: 

    MIN_PRICE = 0 # class variable

    def __init__(self, price:float, sqft:int):
        self.price = price
        self.sqft = sqft

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if (value > House.MIN_PRICE):
            self._price = value

    def __str__(self):
        return f"Price: {self.price}"

    
h = House(200000.56, 1500)
h.price = -100
print(h.price)
print(h)

