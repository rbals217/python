# 문자열 : 문자가 연속으로 존재하는것, 파이썬은 문자와 ㅁ누자열을 구분하지 않음 ( 전부 문자열)
#"", '', """ """, ''' ''',




# # 인덱싱과 슬라이싱
# # 인덱싱은 인덱스로 원하는 값을 추출
# # 자료구조는 인덱스와 키 두가지
# text ="안녕하세요. 파이썬 입니다"
# print(text[0])  # 첫번쨰 글자
# print(text[7])
# print(text[-1])
#
# print(text[7:11])
# print(text[::2])
# print(text[::-1]) # 처음에서 마지막까지 역순으로 출력
# print(text[:5])

from datetime import datetime

current_time = datetime.now().now



# 주민등록번호 입력 :010222-3164414
# jumin = input("주민등록번호 : ")
# key = int(jumin[7])
# year = int(jumin[:2])
# mon = int(jumin[2:4])
# day = int(jumin[4:6])
#
#
# # 생년월일 :2001년 2월 22윌
# if key == 1 or key == 2:
#     print(f"{1900 + year}년{mon:02}월{day:02}일")
# else:
#     print(f"{2000 + year}년{mon:02}월{day:02}일")
#
#
# # 성별 : 남성
# if key == 1 or key == 3:
#     print("성별: 남성")
# else:
#     print("성별: 여성")
# # 나이 : 25살
# if key == 1 or key == 2:
#     print(f"나이: {current_time - (1900 + year)}살")
# else:
#     print(f"나이: {current_time - (2000 + year)}")

# 대소문자 바꾸기 upper()와 lower()
# a = "Hello Python Program.."
# print(a.upper())
# print(a.lower())
#
# # isupper(), islower()
# #입력 받은 문자열에서는 대문자 대문자는 소문자
# for e in a:
#     if e.islower():
#         print(f"{e.upper()}", end="")
#     elif e.isupper():
#         print(f"{e.lower()}", end="")
#     else:
#         print(f"{e}", end="")
# print()

# 문자열 변경: replace("","")
#
# input_str = "Hello Python Program.."
# new_str = input_str.replace("Python", "JavaScript")
# print(new_str)
#
# # 문자 개수 세기 :count
# text = "Google Kakao naver openAI oole"
# print(text.count("oo"))  #결과:
#



# # 문자열 길이 : len()
# text = "Hello World"
# print(len(text)) # 결과: 11

#문자열 찾기 :find()와 rfind(), 그리고 index()
# find(): 찾은 부분 문자열의 첫 번쨰 인덱스르 반환합니다. 부분 문자열을 찾지 못하면 -1 을 반환합니다.
# index(): 찾은 부분 문자열의 첫 번쨰 인덱스를 반환합니다. 부분 문자열을 찾지 못하면 ValueError 예외를 발생시킵니다.
# phrase: "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점찾기, 가장 좋은 선물은 용서"
# print(phrase.find("가장"))
# print(phrase.rfind("가장"))   #뒤에서 부터 찾지만 인덱스는 앞에서 부터
#
# print(phrase.index("포기"))
#
# print(phrase.find("나에게"))   #c찾는 결과 없으면 -1
# # print(input_b_index("나에게"))   #해당 단어가 없으므로 에러가 발생 합니다.
#
# new_phrase = phrase.replace("가장","나에게")
# print(new_phrase)





# # # 문자열 양옆의 공백제거
# # # - strip(): 양쪽 공백 제거
# # # - lstrip(): 왼쪽 공백 제거
# # # - rstrip():  오른쪽 공백 제거
# input_a = """
#      안녕하세요
#     문자열 함수를 알아 봅니다.
# s
#
#     """
# print(input_a.strip())



file_name = "password.txt"
f = open(file_name,"wt")
while True:
    url = input("사이트: ")
    if url == 'exit' :
        break
    my_str = url.replace("http://", "")
    my_str = my_str[:my_str.index(".")]  # 슬라이싱, 처음부터 . 위치 미만까지
    pwd = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + "!" + "jks"
    print(f"비밀번호 : {pwd}")  # 각 사이트 비밀번호 자동으로 만들기
    f.write(pwd + "\n")
f.close()