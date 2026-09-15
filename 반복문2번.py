# for 문 : 정해진 범위만큼 반복 수행 할 떄 효과적
# for 요소 in 시퀀스:
# for 변수 in range(시작값, 최종값, 증감값) :
# from http.cookiejar import uppercase_escaped_char
from pkgutil import resolve_name

# ive =["안유진","장원영","이서","가을","레이","리즈"]
# for e in ive:       # 시퀀스형 데이터를 자동으로 반복 수행 하면서 요소의 값을 복사 하면서 수행
#     e += "*"
#     print(e, end=" ")
# print()
# for i in range(len(ive)):
#     print(ive[i], end=" ")
# print()
# 1 - 100 사이의 3 의 배수 출력하기
# for i in range(1, 100 + 1):
#     if i % 3 == 0:
#         print(f"{i:3}", end = " ")
#         cnt += 1
#         if cnt >= 10:
#             print()
#             cnt = 0

# 입력 받은 수의 범위 내의 7의 배수 출력
# 한줄에 10개씩 출력
# 정렬 {n:5} 를 적용해 줄맞추기
# for i in range(10, 300 + 1):
#     if  i % 7 == 0:
#         print(f"{i:5}", end=" ")
#         if i % 10 == 0:
#             print()

# 입력 받은 문자열을 뒤집어 출력 하기
# 입력 : abcdef => fdecba


# for i in range(len(eng) - 1, -1, -1):
#     print(f"{eng[i]}", end=" ")
# print()
# eng = input("영어 입력: ").upper()
# for e in eng :
#     if e.isupper():
#         eng += e.lower()
#     elif e.isupper():
#         eng += e.upper()
#     print(eng)
# count = 0
# num = int(input("숫자를 입력하세요 : "))
#
# # 10줄에 5개만 출력
#
# for i in range(1, 1000 -1):
#     if i % 3 == 0 or i % 5 == 0:
#         print(f"{i:5}" , end="")
#         count += 1
#
#         if count % 10 == 5:
#             break

#   이중 for 문
#   입력 받은 수가 10이라면 10 * 10 의 행렬 출력

num = int(input("정수 입력 : "))
for i in range(1,num + 1):  # 0 ~ num 까지
    for j in (1,num + 1):
        print("*",end=" ")
    print()

# 단일 for문으로 변경해서 출력 해보기
# 반복문 범위를 num * num
# 1 % num == 0: print()
for i in range(1,num * num + 1):
    print(F"{i:4}", end=" " )
    if i % num == 0:
        print()

# 2 ~ 9단 까지 구구단 출력하기
