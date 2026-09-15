# 딕셔너리: 딕셔너리는 단어의 뜻 그대로 '사전'과 같이 별도의 키를 통해 각 요소를 접근 할 수 있도록 만들어진 데이터 타입
# Map ( key: value) map(가공된 배열)
from tokenize import endpats

#{} 로 선언, 각 요소는 쉼표(,)를 사용해 구분
# 키와 값이 한쌍으로 구성되고, 이 둘은 콜론(:) 으로 구분
# [] 대괄호, {} 중괄호, ()소괄호

coffe_menu = {"Americano": 2500, "Esspresso" : 2500, "Latte" : 4000, "Moca" : 4500}
print(coffe_menu)
print(coffe_menu["Esspresso"])  #키로 값 확인
print(coffe_menu.get("Latte"))  # 키로 값 확인


# 추가, 삭제, 키 존재 여부 확인
coffe_menu["ColdBrew"] = 5500   # 새로운 키와 값 추가
del coffe_menu["Latte"]         # 키와 값 제거

for e in coffe_menu:
    print(f"키:{e}, 값: {coffe_menu[e]}")

# update 함수 사용하기 : 딕셔너리 데이터를 한꺼번에 변경 가능
coffe_menu.update({"Americano": 3000, "Esspresso": 2500, "Latte": 4000, "Moca": 4500, "스무디": 5000})
print(coffe_menu)

# 문제 1. 딕셔너리 생성 및 출력
# 학생 3명의 이름을 키로 , 점수를 값으로 하는 딕셔너리 student_score를 만들고 전체를 출력하세요 (예: 철수 90 영희 85 민수 78
student_score =  {"철수": 90, "짱구": 85, "훈이":78 }
print(student_score)

# 문제 2. 값 조회
# coffe_menu 에서 "Moca"의 가격을 get() 함수를 이용해 추력하세요. 만약 존재하지 않는 메뉴("Cappuccino")를
# get() 으로조히하면 어떻게 되는지도 출력

print(coffe_menu.get("Moca"))
print(coffe_menu.get("cappuccino"))

# 문제 3. 추가와 삭제
# coffe_menu 에 카푼치노: 4800을 새로 추가하고 moca를 삭제한뒤 결과를 출력하세요
coffe_menu["cappuccino"] = 4800
del coffe_menu["Moca"]
print(coffe_menu)

# 문제 4. 반복문과 조건문 활용
# coffe_ menu 를 반복문으로 순회하면서, 가격이 4000원 이상인 메뉴만 "메뉴명 - 가격" 형태로 출력
for e in coffe_menu:
    if coffe_menu[e] < 4000:
        print(f"{e} - {coffe_menu[e]}")

# 문제 5 update()
# update()함수를 사용해 coffe_menu의 모든 가격을 10% 인상하세요,.

for key,value in coffe_menu.item():
    coffe_menu[key] =int(value * 1.1)
print(coffe_menu)

if "라떼" in coffe_menu:
    print("라떼 메뉴가 있습니다.")
else:
    print("라떼 메뉴가 없습니다.")