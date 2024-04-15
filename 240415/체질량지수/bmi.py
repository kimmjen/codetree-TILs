a, b = map(int, input().split())

c = (a ** 2) // (10000 * b)
if c > 25:
    print(c)
    print('Obesity')