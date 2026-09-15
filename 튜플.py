# 파이썬에서는 튜플(Tuple)은 변경할 수 없는(immutable)시퀀스 자료형입니다. 튜플은 여러개의 요소를 저장하고,
# 각 요소에는 인덱스를 통해 접근 할 수 있습니다. 튜플은 괄호(())를 사용하여 정의하며ㅡ 각 요소는 쉼표, 로 구분됩니다.

ls = [1,2,3]
tp1 = (1,2,3)
tp2 = 1,2,3
ts = 1
ts2 = "1"
ts3 = 1,
print(type(ls))
print(type(tp1))
print(type(tp2))
print(type(ts))
print(type(ts2))
print(type(ts3))

member ="안유진", 23 ,"대전시", True  #패킹
name, age, addr, is_adress = member #언패킹

def get_name_card(name, phone):
    position = f"{name} 연구원"
    addr = "서울시 강남구"
    phone = f"082+{phone}"
    return position, addr, phone #여러개의 값 반환

result = get_name_card("곰돌이","1234-5678")
print(f"{result}")