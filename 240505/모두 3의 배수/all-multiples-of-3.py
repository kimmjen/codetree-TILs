def all_multiple_of_3(numbers):
    for number in numbers:
        if number % 3 != 0:
            return 0
    return 1

# 숫자 입력 받기
numbers = [int(input()) for _ in range(5)]

# 결과 출력
print(all_multiple_of_3(numbers))