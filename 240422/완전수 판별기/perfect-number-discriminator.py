n = int(input())

divi_sum = sum([i for i in range(1, n) if n % i == 0])

if divi_sum == n:
    print("P")
else:
    print("N")