names = ["Rose", 20, "Daniel", "Baby"]
print(names)
print(len(names))

print("Zero:", names[0])
print("Latest:", names[-2])
print("Rank:", names[0:2])
print("Rank until index:", names[:2])
print("Rank before index:", names[1:])

# Change elements

names[3] = "Nene"
print(names)

for i in names:
    print(i)

# Exist element

if "Roses" in names:
    print("Exist Rose from your heart ")
else:
    print("Rose Disappeared from your heart ")

# Add element

names.append("Latest")
print(names)

# Add element in the index
names.insert(1, "Inside")
print(names)

# Remove element
names.remove("Inside")
print(names)

# Remove the last element
names.pop()
print(names)

# Remove index from list

del names[1]
print(names)


# Clean list

names.clear()
print(names)

# Delete list
del names
print(names)
