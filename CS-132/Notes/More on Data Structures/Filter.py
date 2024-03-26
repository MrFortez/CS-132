## FILTER ##
# - a function (that isnt a function, its a class)
#   that filters items out of an iterable based on a function
#   Takes in:
#       a function that returns a boolean
#       an iterable
#   Returns:
#       a filter object (that we almost always convert to a list)
#       that contains the items that the input function returned 
#       True for

names = ["collin", "dylan", "jeff", "jackson", "blaine", "josh", "craig", "jonathan", "john", "james", "jolene"]

def startsWithJ(name:str) -> bool: #type hints
    return name[0] == "j"


for name in names:
    print(startsWithJ(name))

jNames = filter(startsWithJ, names)

print(list(jNames))

# .. with lambda functions

jNames2 = filter(lambda name : name[0].lower() == "j", names)

print(list(jNames2))


## Example with dictionaries
users = [
    {"username" : "Aang", "age" : 112},
    {"username" : "Goku", "age" : 37},
    {"username" : "Mercy", "age" : 39},
    {"username" : "Master Chief", "age" : 49},
    {"username" : "The Lorax", "age" : 70}
]

def isOld(user:dict) -> bool:
    return user["age"] >= 49

olds = filter(isOld, users)
print(list(olds))

## ... as a lambda function
olds2 = filter(lambda user:user["age"] >= 49, users)
print(list(olds2))