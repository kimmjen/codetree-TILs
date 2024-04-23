n = int(input())

count = 0
for i in (1, n + 1):
    if (i % 2 and i % 3) or (i % 5):
        count += 1
    
print(count)