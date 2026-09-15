
from datetime import datetime
from random import choices

datetime.today()
datetime.today().year
datetime.today().month
datetime.today().day
datetime.today().hour
datetime.today().minute
datetime.today().second

print(datetime.today().year,"년")
print(datetime.today().month,"월")
print(datetime.today().day,"일")
print(datetime.today().hour,"시")
print(datetime.today().minute,"분")
print(datetime.today().second,"초")





# import random
# cnt = 0
# while True:
#     rand1 = random.randint(0,2)
#     rand2 = int,input("가위바위보 입력: ")
#     print("무승부! 다시 도전합니다...")
#     cnt += 1
#     print(f"총{cnt}번 만에 당신이 이겼습니다!")
#     break
import random
choices = ["가위", "바위", "보"]
user = int(input("가위(0) 바위(1) 보(2) 중 선택:"))
cnt = 0

while True:
    computer = random.randint(0,2)
    cnt += 1

    if computer == user:        # 컴퓨터랑 유저가 같은걸 넀다면
        print(f"무승부 {choices[user]} 다시 도전 합니다.")
        continue

    # 승패판정
    if (user - computer) % 3 == 1:
        print(f"컴퓨터: {choices[computer]} -> 당신의 승리 ! 총 {cnt}번 만에 승부가 났습니다.")
    else:
        print(f"컴퓨터: {choices[computer]} -> 당신의 패배 ! 총 {cnt}번 만에 승부가 났습니다.")
    break
#실습 2
# from datetime import datetime
# login = datetime.now()
# form = login.strftime("login_%Y%m%d_%H%M%S.txt")
# print(f"{}")











# 실습 1 : 나의 생일 까지 남은 일수 계산하기
today =datetime.today()
birth_year = datetime(today.year,6,17)  # 원하는 날짜로 변경
print(f"생일까지 남은날: {(birth_year - today).days}")

# 실습 2 : 요일별 인사말 출력하기


weekday = today.weekday()   #월요일 0~ 시작
if 0 <= weekday <= 4:
    print("오늘은 평일, 힘내")
else:
    print("오느릉ㄴ 휴일.푹셔")
# 실습 3 현재 시간대별 인사말 만들기

hour = datetime.today().hour
if  0 <= hour <= 11:
    print("좋은 아침이빈다.")
elif 12 <= hour <= 17:
    print("좋은 오후입니다.")
elif 18 <= hour <= 22:
    print("조ㅓㅎ은 저녁입니다.")
else:
    print("늦은 밤이네요, 얼른 주무새요.")
#실습 4 원하는 파ㅡ일명으로 생성
# strftime 을 활용해서 로그 파일명을 ㅁ나들어 보세요
# 예: :backup_20206t1014_1530."txt" 같은 형식
