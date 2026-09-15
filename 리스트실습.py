# 3개의 햄버거와 2개의 가격을 입력ㅂ다아 제일 싼 세트메뉴의 가격 구하기 (50원 할인)
# - 콘솔로 연속해서 햄버거 3개 가격과 음료 2개의 가격을 입력 받음
# - 햄버거 3개 중 가장 싼 가격을 선택하고 음료둘 중 싼 음료의 가격을 합산하고 여기서 50원할인
menu = list(map(int,input("햄버거 가격을 입력하세요:, 음료수 가격을 입력하세요: ").split()))


bug_min = min(menu[0:3])
soda_min = min(menu[3:5])

total_price = min(menu[0:3]) + min(menu[3:5])

discount_amount = 50
final_price = total_price - discount_amount

print(f"가장 싼 세트 합산 가격: {total_price}원")
print(f" 50원할인 : {final_price}원")

# 리스트 순회 하기 ; 5대의 자동차 이름을 입력 받음
# - 범위기반 for 문으로 순회해서 출력: for i in range()
# - 시퀀스 for문으로 순회해서 출력: for e in 시퀀스
# - 오름차순, 내림차순 출력


car = ["XMC", "QMC","KHAN","SM5","KONA" ]
for car in car:
    print(car)