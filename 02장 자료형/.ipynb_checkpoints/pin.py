# 주민번호(13자리)를 입력받아 출생년도와 나이 성별을 출력해주는 프로그램

# 사용자 입력받기
pin = input("주민등록번호를 입력하세요: ")

# 출생년도 추출
yymmdd = pin[:6]

# 성별
gender = pin[6]

# 출생년도
year = ""

# 나이
age = 0

if gender in "12":
    year = '19'+ yymmdd[:1+1]
elif gender in "34":
    year = '20'+ yymmdd[:1+1]

age = 2022 - int(year) + 1

print("당신의 출생년도는 {}년". format(year))
print("당신의 나이는 {}세". format(age))
if int(gender) % 2 == 0 :
    print("여성입니다.")
else :
    print("남성입니다.")