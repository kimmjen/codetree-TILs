a, b = map(int, input().split())

start = min(a, b)
end = max(a, b)
sum_ = 0

for num in range(start, end + 1):
    if num % 5 == 0:
        sum_ += num

print(sum_)