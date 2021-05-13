def swap(a,b):
    maxA = max(a)
    maxB = max(b)
    count = 0
    total = 0
    res = []

    while count < len(a):
        if a[count] == maxA:
            posMAxA = count
        count += 1

    count = 0

    while count < len(b):
        if b[count] == maxB:
            posMAxB = count
        count += 1

    change = b[posMAxA]
    b[posMAxA] = b[posMAxB]
    b[posMAxB] = change

    count = 0

    while count < len(a):
        res.append(b[count] - a[count])
        count += 1

    for i in res:
        if i < 0:
            i = -i
        total += i
    print(total)

a = [1, 3]
b = [4, 2]
swap(a, b)