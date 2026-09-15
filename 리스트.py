# 리스트: 연속적으로 저장되는 형태의 자료형
# - 크기 지정이 필요없음
# - 같은 데이터형일 필요가없음
# - [] 대괄호로 감싸서 표현, 0개 이상의 원소가 저장 될 수 있음
# - 읽고 쓰기가 가능


# 과목의 수를 알 수 없는 성적을 입력받아, 총점과 평균 구하기
score = list(map(int,input("성적입력: ").split()))
print(f"score={sum(score)}, 평균:{sum(score)/len(score)}")


mixed = ["안유진", 23,True,[100,200,300],["서울","대전","대구","부산"],{"주소":"경기도"}]
print(mixed)

# 안유진 이름출력,
print(mixed[0])

# 100,200,300 출력
print(mixed[3])

# "안유진",23 ,True출력
print(mixed[0:3])


# 대전출력
print(mixed[4][1])
#대전 전만 출력
print(mixed[4][1][1])

# 경기도 출력
print(mixed[5]["주소"])
# 부산의 부 출력
print(mixed[4][3][0])

members = [
    {
        "name" : "규민",
        "addr" : "대전시"
    },
    {
        "name" : "정민",
        "addr" : "인천시"
    },
    {
        "name" : "성민",
        "addr" : "서울시"
    },
    {
        "name" : "승민",
        "addr" : "충청남도"
    },
]

print(members[0])

# 요소 추가
list_a = [1,2,3]
list_a.append(4)
list_a.append(5)
list_a.insert(1,1000)
print(list_a)

# 리스트 제거하기
# POP : 인덱스가 없으면 맨 마지막값 제거, 인덱스가 이씅면 인덱스 위치의 값 제거
# print(list_a.pop(1))
print(list_a.remove(1000))
print(list_a)

del list_a[1]
print(list_a)
list_a.clear()
print(list_a)

# 중복제거
my_list =['A', 'B', 'C', 'D', 'E']
new_list = []
for v in my_list:
    if v not in new_list:
        new_list.append(v)
print(new_list)

#집합
test_list = {'A','B','C','D','B','D','E'}
print(test_list)

# 10개의 임의의 숫자를 입력 받아 홀수와 짝수 리스트에 나눠 담아서 출력하기

number = list(map(int, input("숫자를 입력하세요: ").split()))

even_list = []
odd_list = []

for i in number:
    if i % 2 == 0:
        even_list.append(i)
else:
    if i % 2 == 1:
        odd_list.append(i)
    print(f"홀수: {even_list} 홀수입니다")

    print(f"짝수: {odd_list} 짝수입니다.")