a , b = map(int, input().split())
if a > b:
    c = 0
else:
    c = 1

if a == b:
    d = 1
else:
    d = 0

print(f"{c} {d}")