def minMax(arr):
    array = arr.copy()
    count = 0
    a = 0
    finish = []

    size = len(array)
    while count < size:
        del array[count]
        for i in array:
            a += i
        finish.append(a)
        a = 0
        count += 1
        array = arr.copy()

    print(min(finish), max(finish))




x = [1, 2, 3, 734065819, 362748590]

minMax(x)


