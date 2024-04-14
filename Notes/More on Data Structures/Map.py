## Map ##
#   a function(not really but who cares)
#   that maps some input to an output
#   Takes In:
#       -A function that defines the maping
#       -an iterable
#   Returns:
#       -a map object that typically gets converted to a list
#       -it contains the result of applying the given function to each
#           item in the list

favoriteFoods = ["cabbages", "spaghetti", "crawfish", "krabby patty",
                 "diet dr. kelp", "saLADs", "krusty krab pizza",
                 "caf nuggets", "communion wafers", "spaghetti again"]

def makeSentence(food):
    return f"My least favorite food is {food}"

unfavoriteFoods = list(map(makeSentence, favoriteFoods))
print(unfavoriteFoods)

# .. lambda example

notFavoriteFoods = list(map(lambda food : f"My favorite food is {food}", favoriteFoods))
print(notFavoriteFoods)


# another more practical example
incomingData = [
    ["Jeffery", "krabby patty"],
    ["Dylan", "krusty krab pizza"],
    ["Brandon", "spaghetti"],
    ["Sage", "burger"],
    ["Josh", "tacos"]
]

def listToDict(item):
    return {"name": item[0], "favorite_food" : item[1]}

result = list(map(listToDict, incomingData))
print(result)