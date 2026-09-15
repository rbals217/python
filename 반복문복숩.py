# while문
# for i in range(초기값 , 최종값 , 증감값)
# for e  in sequence
from os.path import split

# from 기본 import gender

# n = int(input("정수 입력: "))
# total = 0
#
# while n > 0:   # 최종값
#     total += n
#     n -= 1      # 증감값
#
# for i in range(1, n + 1):  # 1이 증감값
#     total += i
#
# while True:
#     total += n
#     n -= 1
#     if n == 0:break
#
# print(total)

# 입력 받은 숫자의 합 구하기
# score = list(map(int, input("정수 입력: ").split()))
# total = 0
# # for i in range(0, len(score)):
# #     total  += score[i]
# #
#
#
# for e in score :
#     total += e
# print(total)

# for i in range(len(score) -1, -1, -1):
#     print(score[i], end="")

# 별 100개 채우기
# for i in range(10):
#     print(f"|i={i}|", end="")
#     for j in range(10):
#         print("*", end=" ")
#         print()

# 별 숫자 차례대로 증가


# n = int(input("입력 :"))
# for i in range(n):
#     for j in range(i + 1):
#         print("*",end=" ")
#     print()

# 반대
# n = int(input("입력 :"))
# for i in range(n -1 ,-1, -1):
#     for j in range(i + 1):
#         print("*",end=" ")
#     print()

# continue : 반복문에서 아래의 문장을 수행하지 않고 반복문으로 이동
#
# n = int(input("정수 입력"))
# for i in range(n):
#     if i % 2 == 0: continue
#     print(i)
n = int(input("정수 입력"))
for i in range(n):
    if i % 3 == 0 and i % 5 == 0: continue
    print(i)





name = input("이름을 입력 하세요 : ")
while True:
    age = input("나이를 입력하세요 : ")
    if age.isdigit():  # 문자열이 '숫자'로만 이루어져있는지 확인하는 함수
        age = int(age)
        if 0 < age < 200:
            break
    print("나이를 잘못 입력 하셨습니다. 다시 입력 하세요.")

while True:
    gender = input("성별 입력: M/F").lower()
    if gender == "m" or gender == "f": break
    print("성별을 잘못 입력하셨습니다.")

while True:
    jobs = input("직업을 입력 하세요: ")
    if jobs.isdigit():
        jobs = int(jobs)
        if 0 < jobs < 5: break
    print("직업이 잘못 입력되었습니다. 다시 입력해주세요.")

if gender == 'M' or gender =='m':
    gen_name ="남성"
else:
    gender = 'F' or gender == 'f'
    gen_name = '여성'
jobs_name = ("", "학생", "회사원", "주부", "무직") # 튜플 사용

print("="*3, "회원정보", "="*3)
print(f"이름 : {name}")
print(f"나이 : {age}")
print(f"성별 : {gen_name}")
print(f"직업 : {jobs_name}")

# 짝수/ 홀수 개수 세기 if 2 % == 0
even_cnt = 0
odd_cnt = 0
while True:
    n = int(input("정수입력( -1 종료):"))
    if n == -1:
        break
    if n % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1

    print(f"짝수 개수: {even_cnt}")
    print(f"홀수 개수: {odd_cnt}")
# 구구단 출력
while True:
    dan = int(input("2 ~ 9 사이의 정수 입력: "))
    if 2 <= dan <= 9:
        break
    print("잘못된 입력 입니다.")
for i in range(1,10):
    print(f"{dan} x {i} = {dan*i}")

sum = 0 # 초기화해줘야함. 기존 변수에 들어가있는 값을 기준으로 더해야하기떄문
for i in range(1, n+1):
    sum += i
print(sum)

# 사각형 찍기
n = int(input("정수를 입력하세요: "))
for i in range(1, n * n + 1):
    print(f"{i:3}", end=" ")
    if i % n == 0: print()





