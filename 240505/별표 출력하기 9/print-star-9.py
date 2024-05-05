# 정수 n 입력 받기
n = int(input())

# 별표 출력
for i in range(n):
    print("  " * (n - i - 1) + "* " * (2 * i + 1))