# 정수 n 입력 받기
n = int(input())

# 위쪽 별표 출력
for i in range(1, n + 1):
    print("*" * i)
    print("\t")

# 아래쪽 별표 출력
for i in range(n - 1, 0, -1):
    print("*" * i)
    print("\t")