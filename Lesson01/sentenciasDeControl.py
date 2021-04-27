condition = False

#if condition == True:
#    print("Is true condition")
#elif not condition:
#    print("Is false condition")
#else:
#    print("condition not recognized")

print("Is true condition") if condition else print("Is false condition")

number = int(input("Provides a number between 1 and 3:"))
if number == 1:
    textNumber = "number one"
elif number == 2:
    textNumber = "number two"
elif number == 3:
    textNumber = "number three"
else:
    textNumber = "out-of-range value"

print("number provided:", textNumber)