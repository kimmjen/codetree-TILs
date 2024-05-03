count = 0

while count < 3:
    num = int(input())
    if num % 2 == 0:  # 짝수인 경우
        print(num // 2)
        count += 1