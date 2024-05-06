# 정수 n 입력
n = int(input())

# 패턴 출력
for i in range(1, n + 1):
    if i == 1:  # 첫 번째 줄 출력
        print("* " * n)
    else:
        print("  " * (i - 1) + "* " * (n - (i - 1)))