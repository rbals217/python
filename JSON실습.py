import json
books =[
    {
    "title" : "이방인",
    "author" : "카뮈",
    "publisher" : "민음사",
    "year" : 1945,
    "price" : 9000,
    "genre" : "장편소설"
    },
    {
    "title" : "아메리칸 프로메테우스",
    "author" : "카이비드",
    "publisher" : "사이언스 북스",
    "year" : 2010,
    "price" : 32500,
    "genre" : "교양과학"
    },
    {
    "title" : "해리포터 마법사의돌",
    "author": "JK 롤링",
    "publisher":"문학수첩",
    "year": 1999,
    "price":11250,
    "genre" : "판타지소설"
    },
    {
    "title" : "완득이",
    "author" :"김려령",
    "publisher": "창비",
    "year":2008,
    "price":10000,
    "genre": "소설"
    },
    {
    "title" : "햄릿",
    "author" : "셰익스피어",
    "publisher" :"민음사",
    "year": 1601,
    "price": 17000,
    "genre": "소설"

    }

]

# TODO 2: books를 JSON 문자열로 직렬화 하고 출력하세요 (한글꺠짐 방지 + 들여쓰기)
json_str = None

Json_str=  json.dumps(books, ensure_ascii=False, indent=4)
print(Json_str)

# TODO 3: json_str를  다시 Python 객체로 역직렬화 하고, for 문으로 한줄씩 출력하세요.
obj = json.loads(Json_str)
print(obj)
print("---------------------------------")
for e in obj:
    print(e)
print("---------------------------------")


# TODO 4 ; 가격이 30.000원 이상인 책만 "제목- 가격원" 형식으로 출력하세요

print("----------------------------------------------------------")
for e in obj:
    if 3000 <= int(e["price"]):
        print(f" 제목 : {e['title']}, \t\t 가격원 : {e['price']}")
print("---------------------------------------------------------")

# TODO 5 : books를 'books.json' 파일로 저장한뒤 다시 일어서 출력하라
with open('book_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(books, json_file, ensure_ascii=False, indent=4)
with open('book_data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
    print(data)

# TODO 6: (선택) 저자 이름을 입력받아 해당 저자의 책만 출력하세요.
author = input("저자 입력: ")

with open('book_data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

for e in data:
    if e["author"] == author:
        print(f"{e['title']}")