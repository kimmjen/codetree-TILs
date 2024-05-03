ages = []
while True:
    n = int(input())
    

    if n < 20 or n >= 30:
        break
    else:
        ages.append(n)

avg = sum(ages) / len(ages)
print(f"{avg:.2f}")