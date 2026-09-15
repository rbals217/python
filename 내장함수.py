# 내장함수: 파이썬에서 기본 제공, import 없이 사용

# ls = [32, 45 , 48, 57, 84, 99] # 연속된 값을 저장할때 리스트를 사용
# print(f"리스트 출력: {(ls)}")
# print(f"합계:{sum(ls)}")     #값을 전부 더함
# print(f"평균: {sum(ls)/len(ls)}" )    #평균 구하기
# print(f"최대값: {max(ls)}")
# print(f"최소값: {min(ls)}")
# print(f"몫과 나머지: {divmod(11,5)}")    #몫 나머지 한번에 다 가져옴
# print(f"오름차순 정렬: {sorted(ls)}")
# print(f"내림차순: {sorted(ls,reverse=True)}" )


# name = "규민"
# ls = [ 32,45,48,57,99]
# print(f"{name}총점: : {sum(ls)}")
# print(f"{name}평균: : {sum(ls) / len(ls)}")
# print(f"{name}최대값: {max(ls)}")
# print(f"{name}최소값: {min(ls)}")

name = input("이름 입력:")
score = list(map(int,input("5과목 성적 입력:").split()))

print(f"이름: {name}, 총점: {sum(score)}, 평균: {sum(score)/len(score)}")
print(f"이름: {name}, 최대값: {max(score)}, 최소값: {min(score)}")