def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def has_common_factor(a, b):
    gcd_result = gcd(a, b)
    return 1920 % gcd_result == 0 and 2880 % gcd_result == 0

# 입력 받기
a, b = map(int, input().split())

# 결과 출력
print(1 if has_common_factor(a, b) else 0)