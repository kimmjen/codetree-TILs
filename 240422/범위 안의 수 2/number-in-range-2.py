num_arr = [int(input()) for _ in range(10)]

sum_ = 0
count = 0

for num in num_arr:
    if 0 <= num and num <= 200:
        sum_ += num
        count+= 1


avg = sum_ / count if count > 0 else 0

print(sum_, round(avg, 1))