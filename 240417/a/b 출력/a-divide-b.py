a, b = map(int, input().split())

result = a / b
rounded_result = int(result * 10**21) / 10**21

print("{:.21f}".format(rounded_result))