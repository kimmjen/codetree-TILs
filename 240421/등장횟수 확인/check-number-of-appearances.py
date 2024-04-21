num_arr = []
for _ in range(5):
    num_arr.append(input())

count = 0

for number in num_arr:
    if int(number) % 2 == 0:
        count += 1

print(count)