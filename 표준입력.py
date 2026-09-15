# 표준입력이란? 콘솔로 부터 사용자의 입력을 받음
# - 기본적으로 문자열로 반환되며, 다른데이터형으로 변환하려면 형변환 함수 사용해야 함
from os.path import split

# 이름(문자열), 나이(정수), 성별(문자열), 주소(문자열), 평균(실수)입력 출력해보기
# name =input("이름 입력: ")
# age = int(input("나이 입력: ")) # 문자열로 입력 받은 나이를 정수로 반환
# gender = input("성별 입력(M/f): ").upper()  #대문자로 반환
# addr = input("주소 입력: ")
# avg = float(input("평균 입력: "))
# kor = int(input("국어 입력: "))
# eng = int(input("영어 입력: "))
# mat = int(input("수학 입력: "))
# 국어 , 영어 , 수학 성적을 입력 받아, 총점과 평균으로 출력
# score = list(map(int, input("국어 영어 수학: ").split()))

# print(f"이름: {name}")
# print(f"나이: {age}")
# print(f"성별: {'남성'if gender == 'M' else '여성'}")
# print(f"주소: {addr}")
# print(f"총점: {sum(score)}")
# print(f"평균: {sum(score) / 3 : .2f}")

# 시간을 24제로 예) 23;56;45 입력 ㅂ다아 12제로 변환해서 11시 56분 45초 형태로 출력하기
# split(";")

# hour,minute,sec = input("24시간 시:분:초 >").split(":")
# hour = int(hour)
# minute = int(minute)
# sec = int(sec)
# if hour == 12:
#     print(f"오후{hour:02}시{minute:02}분{sec:02}초")  # 앞자리가 0이면 앞자리 값이 0으로 변환
# elif hour > 12:
#     hour -= 12 # hour = hour - 12
#     print(f"오후{hour:02}시{minute:02}분{sec:02}초")
# else:
#     print(f"오전{hour:02}시{minute:02}분{sec:02}초")

# "이름과 주소 입력 : " 안내 문구로 이름과 주소를 공백으로 구분해서 한 번에 입력받고 (split() 활용), 두 값을 각각 출력하세요

name,addr = input("이름과 주소: ").split()
print("이름: " + name)
print("주소: " + addr)

# "시:분:초 : 안내 문구로 "14:5:9" 형태의 시간을 콜론(;) 기준으로 입력받아 map*int로 정수 변환한 뒤,,
# 각자리를 2자리 폭에 채워서 출력
hour,minute,sec = map(input("24시간 시:분:초 >").split(":"))
print(f"{hour:02}{minute:02}{sec:02}")

# 국어 영어 수학 공백 받아 map( int , input(), split())) 평균 구하고
# 평균 60점 이상이라면 합격, 불학겹 삼항 연산자 출력
kor, eng, mat = map(int, input("국어 영어 수학: ").split())
avg = (kor+eng+mat)/3
print(f"{'합격' if avg >= 60 else '불합격'}")
