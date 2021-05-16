def cake(candles):
    maxCandles = max(candles)
    countMax = 0

    for i in candles:
        if i == maxCandles:
           countMax += 1

    print(countMax)


x = [3,2,1,3]

cake(x)
