a, b = map(int, input().split())

product = 1
for num in range(a, b+1, a):
    product *= num
print(product)