n = int(input())
num_arr = [int(input()) for _ in range(n)]

total_sum = 0
for number in num_arr:
    if number % 2 != 0 and number % 3 == 0:
        total_sum += number

print(total_sum)