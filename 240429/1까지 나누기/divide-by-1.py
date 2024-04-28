n = int(input())

divisions = 0
current_n = n
for divisor in range(1, n + 1):
    if current_n <= 1:
        break
    current_n //= divisor
    divisions += 1

print(divisions)