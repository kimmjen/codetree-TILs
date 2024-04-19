n = int(input())

classroom_ = 0
corridor_ = 0
restroom_ = 0

for day in range(1, n + 1):
    if day % 12 == 0:
        restroom_ += 1
    elif day % 3 == 0:
        if day % 12 != 0:
            corridor_ += 1
    elif day % 2 == 0:
        if day % 3 != 0 and day % 12 != 0:
            classroom_ += 1

print(classroom_, corridor_, restroom_)