# 자료형(Data Type)은 데이터를 저장하는 방식과 연산할 수 있는 방법을 정의 한는 ㄷ이터의 형태를 의미
# python에서는 변수를 선언할 떄 자료형을 명시하지 않아도 되며, 값이 할당될 떄 자동으로 자료형이 결정
# text = None  # "", 100. 3.14. True , None
# print(type(text))
#
# # 문자열 : 문자가 연속으로 존재하는 것, 파이썬은 문자와 문자열을 구분하지 않음. "", '' ,""" """, ''' '''
# text1 = "안녕하세요. 파이썬 입니다."
# print(text1)
# print(text1[0])  # 해당 인덱스의 내용을 추출 0번의 인덱스를 추출
# print(text1[7:10]) # 슬라이싱
# print(text1 + "!!!!!!!")
# print(text1 * 3 )

# 숫자형(number) : 정수, 실수, 복소수형이 잇음, 사칙연산 가능
num1 = 10.1
num2 = 4
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)

# 불리언(BOolean) : 참 과 거짓 두가지 값만 가짐
# age = int(input("나이를 입력: "))
# is_adult = False
# if age >= 18:
#     is_adult = True
# else:
#     is_adult = False

print(bool(1))      #True  0을 제외하면 숫자는 참
print(bool(-1))     #True
print(bool(0))      #False
print(bool(""))     #False
print(bool(" "))    #True   문자열에 값이 들어와서 참
print(bool(None))   #False 값이 정해지지 않아 거짓.


# 형변환: 데이터를 다른 자료형으로 변환 할 떄  사용
print("100" + str(200))
print(int("100")+200)

# 사용자에게 나이를 입력받아 다음 조건에 따라 메시지를 추렬갛는 프로그램을 작성하세요.
# 19세 이상이면 "성인입니다" 출력
# 19세 미만이면"미성년자입니다." 출력

age = int(input("나이를 입력: "))
is_adult = False
if age >= 18:
    is_adult = True
    print("성인입니다.")
else:
    is_adult = False
    print("미성년입니다.")

# 첫 6글자("Python") 만 출력하세요.
sentence ="Python programming is fun"
print(sentence[0:6])