month = int(input("Provides one month of year (1 at 12): "))
station = None

if month == 1 or month == 2 or month == 12:
    station = "Winter"
elif month == 3 or month == 4 or month == 5:
    station = "Spring"
elif month == 6 or month == 7 or month == 8:
    station = "Summer"
elif month == 9 or month == 10 or month == 11:
    station = "Fall"
else:
    station = "Incorrect month"

print("Station:", station, "for the month:", month)