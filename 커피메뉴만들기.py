# 기본 메뉴 추가 {} 중괄호를 사용해 선언,
# 각 요소는 ,(쉼표) 로 구분
# 키와 같은 :(콜론)으로구분
# 딕셔너리 내부에 리스트를 가짐
import json
from random import choice

menu = {
    "Americano": ["coffee", 2000, "기본 커피 입니다."],
    "Espresso": ["coffee", 2500, "기본 커피 입니다."],
    "Latte" : ["coffe", 4000, "우유가 들어 있는 커피"],
    "green tea": [ "tea", 4500, "녹차 입니다."],
    "black tea" : [ "tea", 4500, "홍차 입니다."]
}

# 전체 메뉴 조회
def print_menu():
    for e in menu:
        print(f"{e} - {menu[e]}")

# 개별 메뉴 조히
def get_menu(name):             # def는 함수를 만드는 키워드 print_menu(매개변수) 함수 이름
    if name in menu:                # 메뉴 딕셔너리에 전달 받은 이름이 있는 지 확인
        print(menu[name])               # 키를 사용해 메뉴의 정보 출력
    else:
        print("찾는 메뉴가 없습니다.")

# 메뉴 추가
def add_menu(name,category,price,desc):         # 메뉴의 정보를 매개 변수로 전달받은
    if name not in menu:                         # 딕셔너리에 없다면 추가
        menu[name] = [category,price,desc]       # 키를 생성하고, 값을 추가( 값이 리스트)
        print(f"{name} 메뉴가 추가 되었습니다.")
    else:
        print("메뉴가 이미 존재 합니다.")


# 메뉴 삭제
def del_menu(name):             # 함수의 매개 변수로 키값을 전달 받아 해당 메뉴를 삭제
    if name in menu:            # 삭제할 메뉴가 메뉴 딕셔너리에 존재하는지 확인
        del menu[name]          # del 키워드를 사용해 키에 해당하는 메뉴 삭제
        print(f"{name} 메뉴가 삭제 되었습니다.")
    else:
        print("삭제할 메뉴가 없습니다.")

# 메뉴 수정

def update_menu(name,category,price,desc):
    if name not in menu:
        menu[name] = [category,price,desc]
        print(f"{name} 메뉴가 업데이트 되었습니다.")
    else:
        print("이미 존재합니다.")


# 파일에서 불러오기
def load_menu():
    try:  # 예외가 발생하기 쉬운 구간에 사용
        with open("menu.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("해당 파일이 존재 하지 않습니다.")
    except json.decoder.JSONDecodeError:
        print("jSON 디코딩 실패")


#파일에서 저장하기
def save_menu():
    with open("menu.json", "w", encoding="utf-8") as file:
        json.dump(menu,file,ensure_ascii=False,indent=4)
        print("menu.json 파일에 저장되었습니다.")


# 전체 매뉴 만들기
# [1] 전체 메뉴 보기 [2] 개별 메뉴 조회 [3] 메뉴 추가 [3] 메뉴 추가 [4] 메뉴 삭제 [5] 메뉴 수정 [6] 종료 하기
while True:
    print("메뉴를 선택 하세요")
    choice = int(input("[1]전체 메뉴 [2]조회 [3]추가 [4]삭제 [5]수정 [6]로딩 [7]저장 [0]종료 : "))

    if choice == 1:
        print_menu()            # 전체 메뉴
    elif choice == 2:
        name = input("조회할 메뉴 이름 입력 : ") # 조회
        get_menu(name)
    elif choice == 3:                          # 추가
        name = input("추가할 메뉴 입력 : ")
        category = input("분류 입력: ")
        price = int(input("가격 입력 : "))
        desc = input("설명 입력 : ")
        add_menu(name,category,price,desc)
    elif choice == 4:                       # 삭제
        name = input("삭제할 메뉴 입력 : ")
        del_menu(name)
    elif choice == 5:                       # 수정
        name = input("수정할 메뉴 입력 : ")
        update_menu(name,category,price,desc)
    elif choice == 6:
        menu = load_menu()
    elif choice == 7:
        save_menu()
    elif choice == 0:
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 메뉴 선택입니다.")
# 파이썬에서는 튜플(Tuple)은 변경할 수 없는(immutable)시퀀스 자료형입니다. 튜플은 여러개의 요소를 저장하고,

# 각 요소에는 인덱스를 통해 접근 할 수 있습니다. 튜플은 괄호(())를 사용하여 정의하며ㅡ 각 요소는 쉼표, 로 구분됩니다.