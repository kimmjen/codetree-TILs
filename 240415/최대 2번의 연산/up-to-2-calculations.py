a = int(input())

while a % 2 == 0:
    a //= 2
else:
    a = (a + 1) // 2

print(a)