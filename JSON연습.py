# JSON(JavaScript Object Notation)은 데이터를 저장하고 교환하는데 널리 사용되는 경량 텍스트 형식 입니다.
# - 파이썬에서는 json 기본 라이브러리를 통해 사용가능
# - 경량 텍스트 포멧
# - 키와 값으로 구성
# - 언어 독립적
# - 웹 APi 통신, 설정 파일, 데이터 저장 및 교환 등 다양한 분야에서 활용




# 파이썬 객체를 json으로 직렬화
# 회원 정보( 이름, 주소, 나이 , 성별, 전화번호 2개 ) => 딕셔너리
# 회원정보 10개 인 리스트  => 리스트
import json
members = [
    {
        "name": "안유진",
        "addr": "대전시",
        "age": 23,
        "gender": "여성",
        "position" : "리더",
        "phone" :["010-1234-5678","041-123-7899"]

    },
    {
        "name" : "제나",
        "addr" : "서울시 마포구",
        "age" : 24,
        "gender" : "여성",
        "position" : "멤버",
        "phone" : ["010-2341-8765", "041-011-6440"]

    },
    {
        "name": "이선민",
        "addr": "서울시 강동구",
        "age" : 41,
        "gender" : "남성",
        "position" : "리더",
        "phone" : ["010-0012-2314", "041-211-1231"]
    },
    {
        "name": "장원영",
        "addr" : "서울시 중구",
        "age" : 19,
        "gender": "여성",
        "position" : "멤버",
        "phone": ["010-2132-0942","041-233-2145"]
    },
    {
        "name": "신창섭",
        "addr" : "판교",
        "age" : 35,
        "gender" : "남성",
        "position" : "리더",
        "phone" : ["010-9877-6541","041-123-4541"]
    },
]


# python 객체를 JSON으로 직렬화
Json_str=  json.dumps(members, ensure_ascii=False, indent=4)
print(Json_str)

# JSON을  -> Python 으로 역직렬화
obj = json.loads(Json_str)
print(obj)
print("---------------------------------")
for e in obj:
    print(e)
print("---------------------------------")

# 파일로 저장하기
with open('data.json', 'w', encoding='utf-8') as json_file:
    json.dump(members, json_file, ensure_ascii=False, indent=4)

# 파일에서 읽기
with open('data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

print(data)