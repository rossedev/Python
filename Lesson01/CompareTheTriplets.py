def myFunction(a, b):
    alice = 0
    bob = 0
    count = 0
    size = len(a)

    while count < size:
        if a[count] > b[count]:
            alice += 1
        elif a[count] < b[count]:
            bob += 1

        count += 1

    return alice, bob


a = [17, 28, 30]
b = [99, 16, 8]

myFunction(a, b)
