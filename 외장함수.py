# 외장함수:파이썬에서 기본제공. 단 import 해서 사용

# 랜덤 함수: 난수 발생기
# randint(m.n): 지정된 범위 안의 임의의 정수 생성



# for i in range(20):
#     print(f"{random.randint(1,10)}", end=" ")    # 1~ 10 싸이의 임의의 값 생성
# print()
#
# # randrange(m,n,p)
# for i in range(20):
#     print(f"{random.randrange(1,10,2 )}", end=" ")    # 1~ 10 미만의 임의의 값 생성
# print()


# 무인도 탈출 게임
# 두개의 주사위를 굴려 같은 값이 나오면 " 무인도를 탈출 했습니다." 두개의 주사위 값"
import random
cnt = 0
while True:
    rand1 = random.randint(1,6)
    rand2 = random.randint(1,6)
    print("탈출 시도...")
    cnt +=1
    if rand1 == rand2:
        print(f"무인도를 탈출합니다. 시도횟수:{cnt}, 주사위 값: {rand1}")
        break

# 로또 번호 생성하기 (1 ~ 45 사이의 임의 의 수 7개, 단, 중복되면 안됨
lotto = []
while True:
    value = random.randint(1,45)
    if value not in lotto:  # 생성된 난수가 로또 리스트에 포함되어 있지 않으면,
        lotto.append(value) #리스트의 마지막에 값 추가
    if len(lotto) == 6:     # 중복되지 않은 번호가 6개가 되면 반복문 탈출
        break
print(lotto)

# 날짜 및 시관 관련 처리 모듈
# from datetime import datetime
# datetime.today()
# datetime.today().year
# datetime.today().month
# datetime.today().day
# datetime.today().hour
# datetime.today().minute
# datetime.today().second
#
# print(datetime.today().year,"년")
# print(datetime.today().month,"월")
# print(datetime.today().day,"일")
# print(datetime.today().hour,"시")
# print(datetime.today().minute,"분")
# print(datetime.today().second,"초")

# 오늘은 2024년 10월 12일 토요일 10시 31분 입니다.
# 현재 시간 가져오기
# %Y : 4자리 연도
# %m : 2자리 월
# %d : 2자리 일
# %A : 요일 표시
# %H : 24시간 형식의 시간
# %M 분 표시
from datetime import datetime

now = datetime.now()
# 원하는 출력 형식 만들기
formatted = now.strftime("오늘은 %Y년 %m월%d일 %A %H시%M분 입니다.")
print(formatted)

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
# strftime을 활용해서 로그 파일명을 ㅁ나들어 보세요
# 예: :backup_20206t1014_1530."txt" 같은 형식

from datetime import datetime
now = datetime.now()
form = now.strftime("backup_%Y%m%d_%H%M%S.txt")
print(form)

# math 모듈
import math
print(math.sin(100))
print(math.cos(100))
print(math.tan(100))
print(math.log(100))
print(math.ceil(100.01)) #소수점 이하를 올림
print(math.floor(100.9))    #소수점 이하를 내림

from simple_colors import *
print(green('hello'))
print(red('world','bold'))
print(yellow('world',['bold','italic']))