# 숫자 입력 받기
n = int(input())

# n부터 1까지 감소하면서 별표 출력
for i in range(n, 0, -1):
    print("* " * i)