## List Comprehension ##
# The idea of creating a list in one line with no multi line loops
#
# This is a Pythonic thing
# Danger: Sometimes it makes your code a little more readable
#   Most times it makes your code not so readable

# Typical way of adding things to lists
numbers = []
for i in range(0,10):
    numbers.append(i)

print(numbers)

names = ["Dylan", "Nick", "Tyler", "Obama", "Serenity", "Adam", "Brandon"]
firstCharacters = []

for name in names:
    firstCharacters.append(name[0])

print(firstCharacters)


# with list comp
    
numbers = [i for i in range(10)]
print(numbers)

# Normal way
for i in range(10):
    numbers.append(i)


# with list comp
firstCharacters = [name[0] for name in names]
print(firstCharacters)

# Normal way
for name in names:
    firstCharacters.append(name[0])


# with list comp
evens = [i for i in range(10) if i%2 == 0]

# normal way
for i in range(10):
    if i % 2 == 0:
        evens.append(i)


firsts = [name[0] for name in names if len(name) % 2 == 0]

for name in names:
    if len(name) % 2 == 0:
        firsts.append(name[0])


# nesting
pairs = [(x, y) for x in range(4) for y in range(5)]
print(pairs)

for x in range(4):
    for y in range(5):
        pairs.append((x, y))
