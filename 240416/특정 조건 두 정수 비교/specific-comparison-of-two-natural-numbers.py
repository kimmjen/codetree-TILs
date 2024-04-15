a , b = map(int, input().split())
c = 0
d = 0
if a > b:
    c = 0
else:
    c =1

if a==b:
    d = 1
else:
    d = 0

print(f"{c} {d}")