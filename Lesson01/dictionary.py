# It's have key and value

dictionay = {
    "IDE": "Integrated Development Environment",
    "OOP": "Object Oriented Programming",
    "DBMS": "Database Management System"
}
print(dictionay)

# length
print(len(dictionay))

# access a element
print(dictionay["IDE"])

# other form
print(dictionay.get("OOP"))

# Modify
dictionay["IDE"] = "integrated development environment"
print(dictionay)

#iterator
for concept in dictionay:
    print(concept)

for concept in dictionay:
    print(dictionay[concept])

for value in dictionay.values():
    print(value)

# element exist
print("IDE" in dictionay)

# add
dictionay["PK"] = "Primary Key"
print(dictionay)

#remove
dictionay.pop("DBMS")
print(dictionay)

#clean
dictionay.clear()
print(dictionay)

#delete
del dictionay
print(dictionay)