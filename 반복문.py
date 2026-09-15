# # 반복문 : 주어진 조건이 참인 동안 반복 수행 함
# # while문 : 주로 반복횟수를 알수 없을 떄
# # for문 : 반복횟수가 정해져 있을떄
#
# n = int(input("정수 입력 :"))
# total =0        # 합계를 저장할 변수
# # while n > 0:    # 반복문의 조건인 n의 값이 0보다 크면 참 이므로 반복 수행
# #     total += n  # total = total + n
# #     n -= 1      # n = n - 1 , n의 값을 변경해서 반복문을 빠져 나가게 함.
# #
# # print(f"합: {total}")
#
# for i in range(1,n+1):   # 최종 값 미만
#     total += i
#
# print(f"합:{total}")
#
# # while 문은 반복 횟수를 알 수 없을 떄 사용 하면 좋음
# # 성별을 입력 받는데 남성은 M. 여성은 F로 입력 받음. 잘 못된 입력이면 계속 다시입력 받음.
#
# while True:     # 무한 반복문 이므로 탈출 조건 필요
#     gender = input("성별을 입력하세요: ").upper()
#     if gender == "M" or gender == "F":
#         break
#     print("성별을 잘 못 입력하셨습니다.")
#
# print(f"{'남성' if gender == 'M' else '여성'}입니다.")
#
#
# while True:
#     name = input("이름입력: ")
#     kor = int(input("국어 성적 입력: "))
#     eng = int(input("영어 성적 입력: "))
#     math = int(input("수학 성적 입력: "))
#
#     if  (0 <= kor <= 100) and (0 <= eng <= 100) and (0 <= math <= 100):
#         break
#     print("성적이 잘못 입력되었습니다.")
#
#
#
#     total = kor + eng + math
#     avg = total / 3
#
#     if avg >= 90:
#         grade = "A"
#     elif avg >= 80:
#         grade = "B"
#     elif avg >= 70:
#         grade = "C"
#     elif avg >= 60:
#         grade = "D"
#     else:
#         grade = "F"
#
#     print(f"총점: {total}, 평균: {avg:.2f}")
#     print(f"{name}님의 등급은 {grade}입니다.")

# num = int(input("숫자를 입력하세요 : "))

# 10줄에 5개만 출력

for i in range(1, 1000, -1):
    if i % 3 == 0 or i % 5 == 0:
        print(f"{i}" , end="")
        if i % 10 == 0:
            print()