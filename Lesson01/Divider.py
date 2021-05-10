arr = [-4, 3, -9, 0, 4, 1]
countArr = len(arr)

positives = []
zeros = []
negatives = []

for i in arr:
    if i < 0:
        positives.append(i)
    elif i == 0:
        zeros.append(i)
    if i > 0:
        negatives.append(i)

countPositives = len(positives)
countNegatives = len(negatives)
countZeros = len(zeros)

divPositives = 0
divNegatives = 0
divZeros = 0

divide1 = countPositives/countArr
divide2 = countNegatives/countArr
divide3 = countZeros/countArr

print(round(divide2, 6))
print(round(divide1, 6))
print(round(divide3, 6))
