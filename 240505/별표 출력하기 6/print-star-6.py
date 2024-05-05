n = int(input())

# 위쪽 삼각형 출력
for i in range(n):
    print("  " * i, end="")
    print("* " * (2 * (n - i) - 1))

# 아래쪽 삼각형 출력
for i in range(n - 2, -1, -1):
    print("  " * i, end="")
    print("* " * (2 * (n - i) - 1))