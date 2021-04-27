a = int(input("provides a value:"))
minValue = 0
maxValue = 5
insideRange = minValue <= a <= maxValue
# print(insideRange)

if insideRange:
    print("inside of range")
else:
    print("outside of range")

vacation = False
restDay = True

if vacation or restDay:
    print("You can go to the park")
else:
    print("You have homework to do")


print(not(vacation))