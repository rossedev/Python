arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

# print(len(arr))

colNumber = []

for i in arr:
    colNumber.append(i[0])

col = len(colNumber) - 1
count = 0
diagonal1 = 0
diagonal2 = 0
for i in arr:
    diagonal1 += i[count]
    count += 1

for j in arr:
    diagonal2 += j[col]
    col -= 1

sum = diagonal1 - diagonal2

if sum < 0:
    print(-sum)
else:
    print(sum)