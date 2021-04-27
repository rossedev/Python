for letter in "Hello":
    print(letter)
else:
    print("Finished")

# Pair numbers
#for i in range(6):
#    if i % 2 == 0:
#        print(i)

for i in range(6):
    if i % 2 != 0:
        continue
    print(i)
