n = int(input())

result = False

if n <= 1:
    result = False
for i in range(2, n):
    if n % i == 0:
        result = True

if result:
    print("C")
else:
    print("N")