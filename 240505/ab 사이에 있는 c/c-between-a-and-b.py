a, b,c = map(int, input().split())

result = "NO"
for i in range(a, b + 1):
    if i % c == 0:
        result = "YES"

print(result)