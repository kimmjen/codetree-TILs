a = int(input())

def days_in_month(month):
    # 각 월에 대한 일 수를 딕셔너리에 저장
    days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    return days[month]

print(days_in_month(a))