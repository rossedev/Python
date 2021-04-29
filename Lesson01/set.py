# No es posible modificar, se puede agregar o eliminar. Esta en desorden y los elementos son unicos

planets = {"Marte", "Jupter", "Venus" }

print(planets)

# length
print(len(planets))

# element exist
print("Marte" in planets)
print("Saturno" in planets)

# add
planets.add("Tierra")
print(planets)
planets.add("Tierra")
print(planets)

# delete
planets.remove("Tierra")
print(planets)
planets.discard("Jupiters")
print(planets)

#clean
planets.clear()
print(planets)

# total delete
del planets
print(planets)
