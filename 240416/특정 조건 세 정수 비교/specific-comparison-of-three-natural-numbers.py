a, b, c = map(int, input().split())
min_v = min(a, b, c)

r1 = 1 if a == min_v else 0
r2 =1 if a == b == c else 0
print(f"{r1} {r2}")