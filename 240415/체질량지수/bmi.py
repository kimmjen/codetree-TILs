a, b = map(int, input().split())

c = (10000 * b) // (a * a)
print(c)
if c > 25:
    
    print('Obesity')