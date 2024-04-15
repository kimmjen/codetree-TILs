a, b = map(int, input().split())

c = int((10000 * b) / (a * a))
if c > 25:
    print(c)
    print('Obesity')