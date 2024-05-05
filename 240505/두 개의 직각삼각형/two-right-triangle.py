# 정수 n 입력 받기
n = int(input())

# 직각삼각형 출력
for i in range(n):
    print("*" * (n - i) + " " * (2 * i) + "*" * (n - i))