
# 스타벅스 판매량 구하기

# with open(file_name, "r" , encoding="utf-8") as file:
#     header =file.readline()     # 줄 바꿈 기준으로 한줄을 읽어 들임
#     header_line = header.split()    # 공백 기준으로 잘라 문자열 리스트 생성
#
#     for e in file:
#         data_list = e.split()
#         espresso.append(int(data_list[1]))   # 10
#         americano.append(int(data_list[2]))   # 50
#         cafelatte.append(int(data_list[3]))   # 45
#         cappuccino.append(int(data_list[4]))  # 20
#
# # 제목/ 젠처 판매량 / 일 평균 판매량
# print("제목\t\t\t 젠처 판매량 \t\t\t 일 평균 판매량")
# print("-------------------------------------------")
# print(f"{header_line[1]:8}  {sum(espresso):6}  {sum(espresso) / len(espresso):18.2f}")
# print(f"{header_line[2]:8}  {sum(americano):6}  {sum(americano) / len(americano):18.2f}")
# print(f"{header_line[3]:8}  {sum(cafelatte):6}  {sum(cafelatte) / len(cafelatte):18.2f}")
# print(f"{header_line[4]:8}  {sum(cappuccino):6}  {sum(cappuccino) / len(cappuccino):18.2f}")
# 1. 각 메뉴별 전체 판매량
dates = []
file_name = "스타벅스일일매출.txt"
espresso = [] # 빈리스트 생성
americano = []
cafe_latte = []
cappuccino = []

with  open(file_name, "r", encoding="utf-8") as file:
    header = file.readline().split()
    for line in file:
        data_list = line.split()
        dates.append(data_list[0])
    espresso.append(int(data_list[1]))
    americano.append(int(data_list[2]))
    cafe_latte.append(int(data_list[3]))
    cappuccino.append(int(data_list[4]))

def total__sales_fucn():
    print("\n 전체 판매량")
    print(f"{header[1]:<12}: {sum (espresso)}")
    print(f"{header[2]:<12} {sum (americano)}")
    print(f"{header[3]:<12}: {sum (cafe_latte)}")
    print(f"{header[4]:<12}: {sum (cappuccino)}")
    print("-----------------------------------------")


# 2. 각 메뉴별 일 평균 판매량
def avg_sales_fucn():
    days = len(dates)
    print("\n 일 평균 판매량")
    print(f"{header[1]:<12} : {sum(espresso) / days :.2f}")
    print(f"{header[2]:<12} : {sum(americano) / days :.2f}")
    print(f"{header[3]:<12} : {sum(cafe_latte) / days :.2f}")
    print(f"{header[4]:<12} : {sum(cappuccino) / days :.2f}")
# 3.  판매량이 가장 높은 메뉴 구하기
def most_sold_menu_func():
    total_list = [sum(espresso), sum(americano), sum(cafe_latte), sum(cappuccino)]
    max_value = max(total_list)
    max_index = total_list.index(max_value) # header[0] - header[3] 에 해당 메뉴명이 있으므로 +1 필요
    print(f"\n 가장 많이 팔린 메뉴는 '{header[max_index + 1]}' ({max_value}개")
    print("-----------------------------------------")
# 4. 판매량이 가장 적은 메뉴 구하기
def less_sales_menu_func():
     total_list = [sum(espresso), sum(americano), sum(cafe_latte), sum(cappuccino)]
     min_value = min(total_list)
     min_index = total_list.index(min_value)
     print(f"\n 가장 적게 팔린 메뉴는 '{header[min_index + 1]}' ({min_value}개")
     print("-----------------------------------------")
# # 5 . 판매량이 가장 많으 ㄴ날짜 구하기
def most_sday_func():
    total_per_day = []
    for i in range(len(dates)):
        total = espresso[i] + americano[i] + cafe_latte[i] + cappuccino
        total_per_day.append(total)
    max_sales = max(total_per_day)
    max_index = total_per_day.index(max_sales)
    print(f"\n 가장 많이 팔린날은 '{dates[max_index]}'({max_sales}) 개입니다")
    print("-----------------------------------------")
# 6., 반복문이 구성된 메뉴 만들기
while True:
    print("\n ======= 스타벅스 매출 분석 ======== ")
    print(" [1] 각 메뉴별 전체 판매량 ")
    print("[2] 각 메뉴별 일 판매량 ")
    print("[3] 판먀랭이 가장 높은 메뉴")
    print("[4] 판매량이 가장 적은 메뉴")
    print("[5] 판매량이 가장 많은 날짜")
    print("[0] 종료 ")
    choice = int(input("메뉴를 선택하세요: "))

    if choice ==1:
        total__sales_fucn()
    elif choice ==2:
        avg_sales_fucn()
    elif choice ==3:
        most_sold_menu_func()
    elif choice ==4:
        less_sales_menu_func()
    elif choice ==5:
        most_sday_func()
    elif choice ==0:
        print("프로그램을 종료합니다")
    break
else:
    print("다시 하세요")