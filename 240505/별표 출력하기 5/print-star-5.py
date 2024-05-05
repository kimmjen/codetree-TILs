# 숫자 입력 받기
n = int(input())

# n부터 1까지의 별표 출력
for i in range(n, 0, -1):
    print("*" * i, end=" ")
    for _ in range(i - 1):
        print("*" * i, end=" ")

    print()