
# It's not possible to modify, add or delete
fruit = ("Orange","Banana","Apple")
print(fruit)

# tupla's length
print(len(fruit))

# indice
print(fruit[0])

# reverse
print(fruit[-1])

# range
print(fruit[0:2])
print(fruit[0:])
print(fruit[:2])

# modify list
listFruit = list(fruit)
listFruit[1] = "Little banana"
fruit = tuple(listFruit)
print(fruit)

# iterator

for fruits in fruit:
    print(fruits, end=" ")

#total delete
del fruit
print(fruit)
