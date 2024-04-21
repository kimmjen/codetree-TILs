n = int(input())

leap_years = 0

for year in range(1, n + 1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_years += 1

print(leap_years)