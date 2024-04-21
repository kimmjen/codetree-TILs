n = int(input())
numbers = [int(input()) for _ in range(n)]

sum_ = sum(numbers)

avg = sum_ / n

print(sum_, round(avg, 1))