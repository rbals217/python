# 함수(function) 은 코드의 특정 블록을 하나의 이름으로 묶어둔 것
# 반복적으로 사용해야 하는 코드나 논리적인 작업을 함수로 정의하면, 재사용성, 가독성, 유지보수성을 높일수 있음
# 함수는 생성 이 후 호출을 해야 실행됨
# def 키워드 사용
# 일반적으로 식별자뒤에() 소괄호 있으면 함수


# 함수의 재사용
def name_card(name,addr, phone):
    print(f"주소: {addr}")
    print(f"전화번호 : {phone}")
    print(f"이름 : {name}")
    print("-"*30)

name_card("안유진", "서울시 강남구 역삼동", "010-1234-5678")
name_card("장원영", "서울시 강남구 삼성동", "010-1234-9999")
name_card("가을", "수원시 권성구 권성동", "010-1234-1111")

# 1. 이름(name), 나이(age), 취미(hobby) 를 매개변수로 받아서 아래 형식으로 출력하는 함수 intro_card()를 작성
def intro_card(name, age, hooby):
    print(f"이름 : {name}")
    print(f"취미 : {hooby}")
    print(f"나이 : {age}")

intro_card("짱구",21 ,"게임")
intro_card("훈이"  ,20 , "산책")
intro_card("맹구",10, "돌줍기")

# 1-2 과목명(subject)과  점수(score)를 매개변수로 받아" 수학점수:90점"
# 형식으로 출력하는 함수 print_score()를 작성하고, 서로 다른 3개 과목으로 호출해보시오.
def print_score(subject,scroe):
    print(f"과목명: {subject}")
    print(f"점수: {scroe}")

print_score("수학", 21)
print_score("영어", 98)
print_score("과학", 67)



#매개변수0, 반환값0
# 2-1 두 정수를 입력받아 큰 수를 반환하는 함수 get_max(a, b)를 작성하시오 (if문 사용)
def get_max(a,b):
    if a > b:
        return a
    else:
        return b
result =get_max(20,30)
print(f"큰수 출력: {result}")
# 2_2 원의 반지름을 입력받아 원의 넓이를 반환하는 함수circle_area(r)를 작성하시오. (원주율은 3.14사용)
def circle_area(r):
    return 3.14 * (r ** 2)

print(f"원의 넓이: {circle_area(5)}")

# 2-3 정수를 입력받아 짝수면 "짝수" 홀수면 홀 을 반환하는 check_even-odd(num)를 작성하시오.
def check_even_odd(num):
    if num % 2 == 0:
        return "짝수"
    if num % 2 == 1:
        return "홀수"
print(check_even_odd(2))

# 기본값 인자: 함수 선언 시 매개 변수에 대한 기본값을 정의
# - 매개변수에 기본값이 정의 되어 있는 경우 함수 호출 시 인자값을 넣지 않으면 기본값으로 호출

# def profile(name, age, job="무직", addr= "대한민국"):
#     print(f"이름: {name}")
#     print(f"나이: {age}")
#     print(f"직업: {job}")
#     print(f"주소: {addr}")
#
# profile("안유진", 23, "아이돌", "대전시")
# profile("장원영", 22, "아이돌" )
# profile("이서", 20)
#

#가변 매개 변수
def profile(name, age, *lang):
    print(f"이름 : {name}, 나이 : {age}", end = "")
    for e in lang:
        print(e, end =" ")
    print()

profile("나희도", 18,"나희도","Java","C","C++","React","Kotlin")
profile("조세호",38, "Python","Java")
profile("유재석",48,"Python", "Java", "C", "C++" )

# 실습문제 : 표준 체중 계산기
#
# 키(cm)와 성별을 입력받아 표준 체중을 계산하는 함수를 작성하시오.
def std_weight(h,sex):
    h = h / 100  # cm > m 로 변환을 해주는것

    if sex == "남자":
      return h * h * 22
    else:
        return h * h * 21

height =int(input("키(cm)를 입력: "))
sex = input("성별을 입력하세요: (남성/여성)")
weight = std_weight(height,sex)
print(f"키 : {height}에 대한 {sex}의 표준 체중은 {weight:.2f}입니다.")


# 함수 이름은 std_weight로 하고, 매개변수는 키(h)와 성별(sex) 두개를 받는다.
# 표준 체중 공식은 다음과 같다.
# 남성: (키(m))² * 22
# 여성: (키(m))² * 21
# 단, 입력받은 키 cm단위이므로 함수 내부에서 m 단위로 변환해야함 (h / 100)
# 함수는 계산된 표준 체중 값을 반환(return)해야함 (출력x)
# input()을 이용해 사용자로부터 키 (cm)와 성별을 입력받는다.
# 키는 정수로 변환하여 저장(int(input(...)))
# 성별은 "남성" 또는 "여성" 문자열로 입력받음
# 함수 호출 결과를 아래 형식으로 출력 (소수점 둘쨰 자리까지)

def prime(n):
    is_prime = True
    for i in range(2,n):
        if n % i ==  0: is_prime = False        # 0으로 나누어 떨어졌을떄 소수가 아니라면 false 리턴 안함
    if is_prime: return n                       # 만약 is_prime 소수라면 return n 반환함
    else: return 0                              # 소수가 아니라면 0을 반환

n = int(input("정수를 입력 : "))
if prime(n):
    print(f"{n}은 소수입니다.")
else:
    print(f"{n}은 소수가 아닙니다.")

n = int(input("정수 입력: "))
sum =0      # 기존값에 더해야하므로 0
for i in range(2, n):                           # 각 숫자를 prime에 넣어서 소수인지 검사과정  n은 최종값 그래서 정수 11까지
    sum += prime(i)
print(sum)




