# 숫자 입력 받기
n = int(input())

# 1부터 n까지의 별표 출력
for i in range(1, n + 1):
    print("* " * i)

# n-1부터 1까지의 별표 출력
for i in range(n - 1, 0, -1):
    print("* " * i)