# 정수 n 입력
n = int(input())

# 패턴 출력
for i in range(1, n + 1):
    if i == 1 or i == n:  # 첫 번째 줄 또는 마지막 줄 출력
        print("* " * n)
    else:  # 나머지 줄 출력
        print("* " + "* " * (i - 2) + " " * (n - i) + "* ")