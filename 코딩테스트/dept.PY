def save_point(amount, rate): # (구매액, 적립률) 
    print("당신의 적립금액은 {}원입니다.".format(amount * (rate / 100)))

while True:
    gender = input("성별을 입력하세요(여자:F, 남자:M, 종료:Q 또는 q): ")
    if gender in ['Q', 'q']:
        print("프로그램을 종료합니다.")
        break
    if gender not in ['F', 'M']:
        print("잘못 입력하셨습니다.")
        continue

    # while True: 유효성 검사
    age = int(input("나이를 입력하세요: "))
    amount = int(input("제품의 총 구매액을 입력하세요: "))
    
    if gender == 'M':
        rate = 3
    elif gender == 'F':
        if age >= 40: rate == 6
        elif age >= 30: rate = 4.5
        elif age >= 20: rate = 3
        else: rate = 1.5

    save_point(amount, rate)
    print()