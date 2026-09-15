# 리스트 순회 하기 ; 5대의 자동차 이름을 입력 받음
# - 범위기반 for 문으로 순회해서 출력: for i in range()
# - 시퀀스 for문으로 순회해서 출력: for e in 시퀀스
# - 오름차순, 내림차순 출력
from os.path import split

# 시퀀스
car = list(input("자동차 이름: ").split())

for i in range(len(car)):
    print(f"{car[i]}", end=" ")

for e in car:
    print(f"{e}", end= " ")

print(f"{sorted(car)}")
print(f"{sorted(car, reverse=True)}")