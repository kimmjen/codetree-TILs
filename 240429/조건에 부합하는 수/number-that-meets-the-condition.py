a = int(input())

result = []

for num in range(1, a + 1):
    if num % 2 == 0 and num % 4 != 0:
        pass
    elif num // 8 % 2 == 0:
        pass
    elif num % 7 < 4:
        pass
    else:
        result.append(num)
        

print(" ".join(map(str, result)))