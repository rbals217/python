import pymysql

# 1. DB 연결
def get_connection():
    conn = pymysql.connect(host="127.0.0.1", user="root", port=3306,
                           password="1234", database="mysqlDB", charset="utf8")
    return conn


def create_user_table(conn):
    cur = conn.cursor()

    # 2. 기존 테이블 삭제 및 생성
    cur.execute("DROP TABLE IF EXISTS userTable")
    cur.execute("""
        CREATE TABLE userTable (
            id CHAR(10) PRIMARY KEY,
            pwd CHAR(15),
            name CHAR(20),
            email CHAR(20),
            addr CHAR(50)
        )
    """)
    conn.commit()



def create_boardTable(conn):
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE boardTable (
            id BIGINT AUTO_INCREMENT PRIMARY KEY,
            title CHAR(20),
            text VARCHAR(1000),
            user CHAR(10),
            datetime DATETIME DEFAULT CURRENT_TIMESTAMP,
       
        )
    """)

    conn.commit()
def create_commentTable(conn):
    cur = conn.cursor()

    cur.execute("""
                CREATE TABLE commentTable
                (
                    c_id     BIGINT AUTO_INCREMENT PRIMARY KEY,
                    c_number CHAR(20),
                    user     CHAR(0),
                    text     CHAR(30),
                    datetime DATETIME,
                   
                        CONSTRAINT fk_commentTable FOREIGN KEY (id)
                REFERENCES boardTable(id)
                ON DELETE CASCADE

                )


                """)
    conn.commit()
    conn.close()


# 3. 초기 데모 데이터 삽입 (회원 6명 일괄 삽입)
def insert_initial_data(conn):
    cur = conn.cursor()
    users = [
        ('ayj1234', '12345678', '안유진', 'ayj@gmail.com', '서울시 강남구'),
        ('jwy1234', '12345678', '장원영', 'jwy@gmail.com', '서울시 강남구'),
        ('fall1234', '12345678', '가을', 'fall@gmail.com', '서울시 강남구'),
        ('ys1234', '12345678', '이서', 'ws@gmail.com', '서울시 강남구'),
        ('lay1234', '12345678', '레이', 'lay@gmail.com', '서울시 강남구'),
        ('liz1234', '12345678', '리즈', 'liz@gmail.com', '서울시 강남구')
    ]

    for user in users:
        cur.execute("INSERT INTO userTable VALUES(%s, %s, %s, %s, %s)", user)

    conn.commit()
    conn.close()


# 신규 회원 추가
def insert_user(conn):
    cur = conn.cursor()
    id = input("아이디 : ")
    pwd = input("패스워드 : ")
    name = input("이름 : ")
    mail = input("이메일 : ")
    addr = input("주소 : ")
    try:
        cur.execute("INSERT INTO userTable VALUES(%s, %s, %s, %s, %s)", (id, pwd, name, mail, addr))
        conn.commit()
        print("추가 완료!!")
    except Exception as e:
        print(f"오류 발생 : {e}")
    finally:
        conn.close()
#로그인확인
def login_user(conn):
    cur = conn.cursor()

    id = input("아이디 : ")
    pwd = input("비밀번호: ")

    cur.execute("SELECT usertable WHERE id = %s", (id,pwd))


    if cur.rowcount > 0:
        print("로그인 성공!!")
    else:
        print("해당 ID는 존재 하지 않습니다.")



# 회원 수정
def update_user(conn):
    cur = conn.cursor()
    id = input("ID: ")
    name = input("이름: ")
    email = input("이메일: ")
    addr = input("주소: ")
    cur.execute("UPDATE userTable SET name=%s, email=%s, addr=%s WHERE id=%s",
                (name, email, addr, id))
    if cur.rowcount > 0:
        print("수정 완료!!")
    else:
        print("해당 ID는 존재 하지 않습니다.")
    conn.commit()
    conn.close()


# 회원 삭제
def delete_user(conn):
    cur = conn.cursor()
    id = input("삭제할 사용자 ID : ")
    cur.execute("DELETE FROM userTable WHERE id = %s", (id,))
    if cur.rowcount > 0:
        print("삭제 성공 !!")
    else:
        print("해당 ID가 존재하지 않습니다.")
    conn.commit()
    conn.close()


# 개별 회원 조회
def search_user(conn):
    cur = conn.cursor()
    id = input("조회할 아이디: ")
    cur.execute("SELECT * FROM userTable WHERE id = %s", (id,))
    row = cur.fetchone()
    conn.close()
    if not row:
        print(f"존재하지 않는 아이디입니다: {id}")
        return
    print_users([row])


def print_users(rows):
    print("-" * 70)
    print(f"{'아이디':<12}{'패스워드':<12}{'이름':<10}{'이메일':<22}{'주소':<20}")
    print("-" * 70)
    for row in rows:
        print(f"{row[0]:<12}{row[1]:<12}{row[2]:<10}{row[3]:<22}{row[4]:<20}")
    print("-" * 70)


# 전체 회원 조회
def search_all_user(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM userTable")
    rows = cur.fetchall()
    conn.close()
    if not rows:
        print("등록된 사용자가 없습니다.")
        return
    print_users(rows)


# 메뉴 출력
def print_menu():
    print("\n===== 사용자 관리 메뉴 =====")
    print("1. 사용자 추가")
    print("2. 사용자 수정")
    print("3. 사용자 삭제")
    print("4. 사용자 조회")
    print("5. 사용자 전체 조회")
    print("0. 종료")
    print("============================")


def main():
    conn = get_connection()

    create_user_table(conn)
    create_boardTable(conn)
    create_commentTable(conn)

    insert_initial_data(conn)



    while True:
        conn = get_connection()

        print_menu()
        choice = input("선택: ")

        if choice == "1":
            insert_user(conn)

        elif choice == "2":
            update_user(conn)

        elif choice == "3":
            delete_user(conn)

        elif choice == "4":
            search_user(conn)

        elif choice == "5":
            search_all_user(conn)

        elif choice == "0":
            print("프로그램을 종료 합니다.")
            conn.close()
            break

        else:
            print("잘못된 선택입니다.")
            conn.close()


if __name__ == "__main__":
    main()