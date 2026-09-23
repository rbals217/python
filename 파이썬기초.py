# 공백을 기준으로 10명의 성적으로 입력받습니다.
scores_input = input("성적 입력 : ")

# 입력된 문자열을 공백을 기준으로 분리하여 리스트로 변환합니다.
scores = list(map(int,scores_input.split()))

#scores =list(map(int,input("성적 입력 : ").split())) 한줄로 표현하기

# 총점 계산
total_socre = sum(scores)

#평균 계산
average_score = total_socre/len(scores)

#최소 점수 계산
min_score = min(scores)

# 최대 점수 계산
max_score = max(scores)

# 결과 출력
print(f"총점: {total_socre}")
print(f"평균: {average_score}")
print(f"최소 점수 {min_score}")
print(f"최대 점수 {max_score}")

n= int(input("정수 입력: " ))
for i in range(1, n*n+1):
    print(f"{1:4}", end=" ")
    if i % n == 0: print()



import random
print("번호 자동 생성 : ", end="")

# 중복 숫자 제거
ls = []
while True:
    rand = random.randrange(1, 46)
    if rand not in ls:
        ls.append(rand)
    if len(ls) == 6: break
print(ls)


# 영화표 예매하기
TICKET_PRICE = 12000
seat =[0] * 10

# 좌석 상태를 표시하는 메뉴 만들기
def print_seat():
    for e in seat :     # 향상된 for 문으로 좌석의 갯수 만큼 순회
        if e == 0: print("[]", end=" ")     #판매안된 좌석
        else: print("[v]", end=" ") 
    print()
    
#총 매출액 구하기
def amount():
    cnt = 0
    for e in seat:
        if e == 1: cnt += 1 # 팔린 좌석의 총 갯수 구하기
    return cnt * TICKET_PRICE

# 좌석 예약하기
def select_seat():
    print_seat()        #현재 예약 가능한 좌석 보여 주기
    num = int(input("좌석 번호를 선택하세요 :")) - 1  # 선택한 좌석번호는 1 부터 시작하고 인덱스느 0부터  시작 떄문 -1
    if seat[num] == 0:
        seat[num] = 1
        print_seat()
    else: print("이미 예약된 좌석 입니다.")

while True:
    sel = int(input("[1] 예매하기 [2] 종료하기 : "))
    if sel == 1:
    # else:
        print(f"총 매출액 : {amount()}원")
        break
