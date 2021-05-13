x = "FA0ETASINAHGRI0NATWON0QA0NARI0"


def splits(array, size):
    arrayInit = [array]
    arrayInitial = arrayInit[0]
    arrayFinal = []
    while len(arrayInitial) >= size:
        piece = arrayInitial[:size]
        arrayFinal.append(piece)
        arrayInitial = arrayInitial[size:]
    print(arrayFinal)
    return arrayFinal


A = splits(x, 6)


def reverse(array):
    var = ""
    for i in array:
        var += i[::-1]
    return var


definitive = reverse(A)
print(definitive)


def solve():
    read = True
    while (read):
        inline = input().split(' ')
        size = int(inline[0])
        if (size == 0):
            read = False
            return
        array = inline[1]
        arrayInit = [array]
        arrayInitial = arrayInit[0]
        arrayFinal = []
        while len(arrayInitial) >= size:
            piece = arrayInitial[:size]
            arrayFinal.append(piece)
            arrayInitial = arrayInitial[size:]

        print(arrayFinal)
        var = ""
        for i in arrayFinal:
            var += i[::-1]
        print(type(var))
        return var


if __name__ == '__main__':
    print(solve())


