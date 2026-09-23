total = 0

file_name = "order.txt"

try:
    with open(file_name, "r", encoding="utf-8") as file:

        for e in file:
            data_list = e.split(",")

            menu = data_list[0].strip()
            count = int(data_list[1].strip())
            price = int(data_list[2].replace("원", "").strip())

            # 이상치 검사
            if price < 0 or price >= 10000 or count < 0:
                continue
            
            # 매출 계산
            total += count * price

            print(menu, count, price)

    print(f"전체 매출: {total:,}원")

except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")