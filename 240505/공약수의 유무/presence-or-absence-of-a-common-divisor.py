def has_common_factor(a, b):
    for i in range(1920, 2881):
        if a % i == 0 and b % i == 0:
            return True
    return False

# 입력 받기
a, b = map(int, input().split())

# 결과 출력
print(0 if has_common_factor(a, b) else 1)