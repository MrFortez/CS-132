## Dictionaries ##
# Dictionaries are sets of key-value pairs
# Keys are unique
# Values correspond to keys
# format  key:value

# Never assume a dictionary has order
# Pyhton 3.7+ maintains insertion order

myDictionary = {"first":"josh", "last":"coriell", 10: 3000}

print(myDictionary)

# Accessing Values
# food = myDictionary["food"] This will cause an error because "food" isnt in the dictionary

food = myDictionary.get("food")

# Assigning New Values
myDictionary["favorite color"] = "green"
myDictionary["first"] = "brandan"

print(myDictionary)

# Note: One way info is sent across the web is in JSON format
# use the requests library to access apis in python

## Iterating over dictionaries ##
newDictionary = {
    "first" : "Brandan",
    "last" : "Fortress",
    "favorite_number" : 42
    }

# default iteration is over the keys
for key in newDictionary:
    print(key, end=" ")
    print(newDictionary.get(key))

# can be explicit and use .keys()
for key in newDictionary.keys():
    print(key, end=" ")
    print(newDictionary.get(key))

# iterate over the values with .values()
for value in newDictionary.values():
    print(value)

# iterate over both keys and values with .items()
for key, value in newDictionary.items():
    print(key, value)

# Sidenote on design
    
# Do I use dicitonaries or objects/classes
# Answer: Up to you. It is a design decision
    
# User as a dictionary
user = {
    "username": "coriell",
    "email": "coriell@latech.edu",
    "password": 123456
}

# User as a class
class User:
    def __init__(self, username, password):
        self.username = username
        self.email = "blahblahblah"
        self.password = password

u = User("coreill", 123456)


## Dictionary Comprehension ##
epicDictionary = {x:x+1 for x in range(10) if x % 2 == 0}
# epicDictionary = {}


for x in range(10):
    if x % 2 == 0:
        epicDictionary[x] = x+1

print(epicDictionary)

names = ["Stephanie", "August", "DAB", "Fay", "Blaine", "Adam", "Nick"]
ages = [18, 78, 45, 18, 32, 112, 2]

nameDictionary = {names[i]:ages[i] for i in range(len(names))}
print(nameDictionary)