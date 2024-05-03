# 출석부 딕셔너리 생성
attendance = {
    1: "John",
    2: "Tom",
    3: "Paul",
    4: "Sam"
}

while True:
    # 출석번호 입력 받기
    num = int(input())
    
    # 출석번호가 딕셔너리에 있는지 확인하고 이름 출력
    if num in attendance:
        print(attendance[num])
    else:
        print("Vacancy")
        break