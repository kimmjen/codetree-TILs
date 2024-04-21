a, b = map(int, input().split())

sum = 0
count = 0

for number in range(a, b + 1):
    if number % 5 == 0 or number % 7 == 0:
        sum += number
        count += 1

avg = sum / count

print(sum, round(avg, 1))