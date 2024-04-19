a, b = map(int, input().split())

number = a

while number <= b:
    print(number, end=" ")
    if number % 2 == 0:
        number += 3
    else:
        number *= 2

    if number > b:
        berak