def solve():
    read = True
    while (read):
        a = input().split(' ')
        b = input().split(' ')

        if (a == 0 or b == 0):
            read = False
            return

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
            res.append(int(b[count]) - int(a[count]))
            count += 1

        for i in res:
            if i < 0:
                i = -i
            total += i
        return total


if __name__ == '__main__':
    print(solve())








