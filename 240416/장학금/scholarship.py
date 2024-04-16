a, b = map(int, input().split())

avg = ( a+ b) // 2

if avg >= 95:
    print(100000)
elif avg >= 90:
    print(50000)
else:
    print(0)