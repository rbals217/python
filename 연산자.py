# 연산자 : 프로그램에서  값을 계산하거나 변수에 대해 연산을 수행하는 기호
# 산술연산자 :  사칙연산 , 나머지 연산
from 자료형 import is_adult

i = 10
j = 4
print(i + j)    # 덧셈 : 14
print(i - j)    # 뺼셈  6
print(i * j)    # 곱셈 40
print(i / j)    # 나눗셈 2.5
print(i % j)    # 나머지 2
print(i // j)   # 몫 2
print(i ** j)   # 제곱 : 10 * 10 * 10 * 10

# 문자열 연산
text = "python"
print(text +"Programming") # 문자열 연결
print(text * 3) # 문자열 반복
print("=" * 10 + "성적정보" + "="*10)

# 대입 연산자
num1 = 10
num1 += 2  # num1 = num1 + 2
print(num1) # 12
num1 -= 2
print(num1)  # 10
num1 *= 2
print(num1)  # 20
num1 //= 2
print(num1)  # 10
num1 %= 2
print(num1)  # 0

# 비교 연산자 : 결과가 참과 거짓으로 반환 됨
a = 10
b = 20
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# 논리 연산자 : 참과 거짓을 반환
# and / or / not
x = 5
y = 10
print(x > 0 and x > y)  # False
print(x > 0 or x > y)   # True
print(not(x > 0 or x > y))  #True


# 삼항 연산자 :
age = 18
is_adult = "성인"if age > 19 else "미성년"
print(is_adult)

num = 100
flag = "짝수" if num % 2 == 0 else "홀수"
print(flag)



year = int(input("년도 입력: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year}년은 윤년입니다.")
else:
    print(f"{year}년은 윤년이 아닙니다.")

# 100의 자리 정수를 입력 받아 100의 자리, 10의 자리, 1의 자리 나누어 담아서 합을 구하기
# 입력:789 => 24
num = int(input("숫자 입력: "))
a = num // 100
b= num //100 % 10
c = num % 10
print(a + b + c)

# 1. 대입연산자 실습
# num = 50에서 시작해서 아래 연산을 순서대로 적용하 ㄴ뒤 , 각 단계마다 결과를 출력하세요.
# 20을 더한다
# 3배로 곱한다
# 7로 나눈 나머지를 구한다
# 2를 뺸다
# 각 연산은 대입 연산자 (+=, *=, %=,-=) 를 사용해서 작성하세요.
num = 50
print(num)
num += 20
print(num)
num *= 3
print(num)
num % 7
print(num)
num -=2
print(num)

# 2. 논리 연산자로 범위 판별
# 사용자에게 점수(0~ 100) 를 입력받아, 점수가 60 점 이상 80 점 미만이면 "보통"을 출력하고,
# 그 외에는 "보통 아님" 을 출력하는 코드를 and. or ,not 중 알맞은 논리연산자를 사용해서 작성하세요
score = int(input("점수 입력: "))
if 60 <= score < 80:
    print("보통")
else:
    print("보통아님")

# 3. 비교 연산자와 삼항 연산자
# 두 수 a. b를 사용자로부터 입력받아, 삼항 연산자를 이용해 둘 중 더 큰 값을 max_num이라는 변수에 저장하고 출력하는 코드를 작성하세요.
# (단, 두 수 가 같은 경우 " 두 수가 같습니다" 를  출력
a = int(input("첫 번쨰 수 입력 "))
b = int(input("두 번쨰 수 입력 "))
if a == b:
    print("두 수가 같습니다")
else:
    max_num = a if a > b else b
print(max_num)

# 4. 아래와 같은 형태의 출려깅 나오도록 문자열 반복(*) 과 연결(+) 연산자를 사용해서 코드를 작성하세요
# **********학생 명단 똑같이
# 1. 호ㅗㅇ길동
# 2. 김철수
# 별표
print("*" * 10 + "학생 명단" + "*" * 10)
print("1.김철수 \n \r2.홍길동")

print("*" * 10 + "학생 명단" + "*" * 10)

# 5. 짝수/홀수 판별과 나이 계싼
# 사용자에게 태어난 연도 ( 예{: 2000) 입력받아 다음을 계싼하는 프로그램을 작성하세요.
# 현재 연도(2026)를 기준으로 만 나이를 계산 ( 2026ㅅ -  태어난 연도)
#  계산된 나이가 짝수인지 홀수인지 나머지 연산자 (%)로 판별
# 삼항 연산자를 사용해서 "짝수" 또는 "홀수" 를 변수에 저장한 뒤 다음과 같이 출력

from datetime import datetime
birth_year = int(input("태어난 연도 입력:"))
current_year = datetime.now().year
age = current_year - birth_year
rst = "짝수" if age % 2 == 0  else "홀수"
print(f"당신의 나이는 {age}살이며, {rst}입니다.")



