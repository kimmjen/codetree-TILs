n = int(input())

arr = []
for i in range(1, n + 1):
    if i % 2 == 0 or i % 10 == 5:
        continue

    elif i % 3 == 0 and i % 9 != 0:
        continue
    else:

        arr.append(i)

print(*arr)