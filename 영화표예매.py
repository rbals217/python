# - 사용자로부터 좌석번호(index)를 입력받아 예매하는 시스템이다.
# - 예매가 완료되면 해당 좌석 값을 1로 변경한다.
# - 이미 예매가 완료된 좌석은 재구매 할 수없다
# - 한 좌석당 예매 가격은 12000원입니다.
# - 프로그램 종류후, 해당 영화관의 총 매출액을 출력한다

# 좌석 개수 리스트 만들기
seat = [0] * 10
price = 12000


#좌석 출력 함수
def print_seat():
    for e in seat:
        if e == 0:
            print("[]", end=" ")
        else:
            print("[v]", end=" ")
    print()


# 좌석 선택 함수
def select_seat():
    print_seat()
    seat_num = int(input("좌석번호 입력 : ")) - 1     #0번 인덱스부터 시작
    if seat[seat_num] == 0: # 아직 예약안된 좌석
        seat[seat_num] = 1
        print_seat()                                #예약 성공시 결과 보여줌
    else:
        print("이미선택된 좌석입니다.")

def cancel_seat():
    print_seat()
    seat_number = int(input("좌석번호 입력 : "))
    if seat_number == 0:
        seat[seat_number] = 1
        print_seat()
    else:
        print("예약 좌석이 아닙니다.")
# 판매 금액계산 함수
def total_account():
    cnt = 0     # 판매된 자석 개수를 누적시켜줌
    for e in seat:
        if e == 1:
            cnt += 1
        return price * cnt      #티켓 가격 * 판매 좌석 수
# 입력 메뉴 구성
while True:
    print("[1] 예매하기")
    print("[2] 종료하기")
    print("[3] 취소하기")
    sel = int(input("메뉴 선택 : "))
    if sel == 1:
        select_seat()
    elif sel == 0:
        select_seat()
    else:
        print(f"총 매출액 : {total_account():,}원")
        break

def second_num(ls,n):
    cnt = 0
    for i in range(len(ls)):
        if ls[i] == n:          # ls의 i번쨰값이 n가 같은데
            if cnt > 0: return i + 1            # 만약 0보다 크다면 i 에 1을 더한값을 반환하고,
            else: cnt += 1                      # 아니라면 카운트에 1을 더하라
        return -1                               # 값을 찾지 못한경우 반환?

ls = list(map(int,input("리스트 입력: ").split()))
n = int(input("찾는 숫자 : "))
print(second_num(ls,n))

a = b = c =0
def num_split(input):
    global a, b, c
    a = input // 100            # 백의 자리
    b = (input % 100) // 10     # 십의 자리
    c = (input % 100) % 10      # 일의 자리

def compare_num():
    if  a > b:                  # a 가 b보다 크다면
        if a < c : return a     # c가 더크다, a 리턴
        else : return c         # c가 작을경우 c 리턴

    else:
        if b > c: return b
        else: return c

n= int(input())
num_split(n)
print(compare_num())