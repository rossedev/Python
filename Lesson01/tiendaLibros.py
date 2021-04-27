print("Provides the following book's data: ")
name = input("Provides the name:")
id = int(input("Provides the ID:"))
price = float(input("Provides the price: "))
freeShipping = input("Indicates whether shipping is free(Yeah/Nop): ")

if freeShipping == "Yeah":
    freeShipping = True
elif freeShipping == "Nop":
    freeShipping = False
else:
    freeShipping = "Incorrect value, it must be True or False"

print("Name:", name)
print("ID:", id)
print("price:", price)
print("free shipping?", freeShipping)
