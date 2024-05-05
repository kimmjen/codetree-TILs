def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 입력 받기
n = int(input())

# 결과 출력
print("P" if is_prime(n) else "C")