# 정수 n 입력 받기
n = int(input())

# 별표 출력
for i in range(1, n + 1):
    if i % 2 == 1:  # 홀수 번째 줄에는 하나의 별표만 출력
        print("*")
    else:  # 짝수 번째 줄에는 해당 줄의 번호만큼 별표가 출력됩니다.
        print("* " * (i))