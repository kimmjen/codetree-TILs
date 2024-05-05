# 숫자 입력 받기
n = int(input())

# 짝수일 경우, 별표 출력
if n % 2 == 0:
    for i in range(1, n + 1):
        if i % 2 == 0:
            print("* " * i)
# 홀수일 경우, 별표 출력
else:
    for i in range(1, n + 1):
        print("* " * i)
    for i in range(n - 1, 0, -1):
        print("* " * i)