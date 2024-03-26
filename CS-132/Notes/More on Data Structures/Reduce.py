## Reduce ##
# its a functions that...
# takes in: 
#   a function
#   an iterable
# returns
#   one single value
#

from functools import reduce

myList = [1,2,3,4,5,6]

def multiply(a, b):
    return a * b


result = reduce(multiply, myList)
print(result)

# another example

names = ["Brandan", "Fortress", "The", "Slayer", "Of", "Worlds"]

def combineNames(name1, name2):
    return f"{name1} {name2}"

resultAgain = reduce(combineNames, names)
print(resultAgain)