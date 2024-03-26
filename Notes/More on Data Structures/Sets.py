#Sets in python are mathematical units
#Items are unique
#Sets are unordered

mySet = {1,3,3,3,2,3,3,3,4,5,6} #curly brackets for sets
# print(mySet)

# can convert lists to sets to get unique values
myList = [1,2,2,2,2,2,2,3,4,5]
myConvertedSet = set(myList)
# print(myConvertedSet)
myUnconvertedSet = list(myConvertedSet)
# print(myUnconvertedSet)

setA = {1,2,3}
setB = {3,4,5,6}

print(f"a = {setA}")
print(f"b = {setB}")

# Union
print(f"a | b = {setA | setB}")

# Intersection
print(f"a & b = {setA & setB}")

# Difference
print(f"a - b = {setA - setB}")
