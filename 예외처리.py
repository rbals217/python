# 파이썬에서 예외처리(Exception Handling)은 프로그램 실행중 에 발생할 수 있는 오류를 적절히
#  처리하여 프로그램이 비정상저긍로 종료되지 않도록 하는 방법입니다.
# 예외 처리는 주로 try, except, else, finally 블록을 사용하여 처리합니다.


while True:
 try:


     print("나눗셈 계산기 입니다.")
     num1 = int(input("첫 번쨰 숫자 입력 : "))
     num2 = int(input("두 번쨰 숫자 입력: "))
     print(f"{num1} / {num2} = {int(num1/num2)}")
 except ValueError:
     print("에러 !!! 잘못된 값을 입력하였습니다.")
 except ZeroDivisionError as err:
     print(err)
 except Exception as err:
     print(err)
 else:
     print("정상 처리 되었습니다.")
     continue
 finally:
     print("프로그램 실행 완료!!")
     break

print("프로그램 실행 종료!!!!!")