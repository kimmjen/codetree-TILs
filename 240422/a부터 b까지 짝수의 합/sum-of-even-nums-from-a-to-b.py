a, b = map(int, input().split())

sum_ = 0

for num in range(a, b + 1):
    if num % 2 == 0:
        sum_ += num


print(sum_)