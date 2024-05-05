# 자연수 n 입력 받기
n = int(input())

# 위쪽 삼각형 그리기
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

# 아래쪽 삼각형 그리기
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)