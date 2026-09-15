num = int(input("번호입력: "))

num1 = 1100
num2 = 1000
num3 = 700
num4 = 600

if num == 1:
    cost =int(input(f"{num}번 상품입니다. 가격 입력:"))

    if cost < num1:
        print("금액이 적습니다.")
    elif cost == num1:
        print("나왔습니다.")
    else:
        print("거스름돈이 포함되어 나왔습니다.")

# if chocie == 1:
#   name = "콜라"
#   price = 1100
# elif choice == 2:
#   name = "사이다"
#   price = 1000
# elif choice == 3:
#   name = "커피"
#   price = 700
# elif choice == 4:
#   name = "생수"
#   price = 600
