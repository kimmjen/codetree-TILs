# 정수 n 입력 받기
n = int(input())

# 문자 출력
for i in range(1, n):
    print("  " * (n - i) + "@ " * i)

# 역순으로 출력
for i in range(n):
    print("@ " * (n - i))