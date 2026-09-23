import pymysql
from openpyxl.chart import reference


# 1. DB 연결
def get_connection():
    conn = pymysql.connect(host="127.0.0.1", user="root", port=3306,
                           password="1234", database="mysqlDB", charset="utf8")

    return conn


def select_user_table(conn):
    cur = conn.cursor()

    # 2. 로그인상태 확인

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
    conn.close()

def create_boardTable(conn):
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE boardTable (
            id BIGINT AUTO_INCREMENT PRIMARY KEY,
            title CHAR(20),
            text VARCHAR(1000),
            user CHAR(30),
            datetime DATETIME,
            id CHAR(10)
        )
        
    """)
    conn.commit()


def create_comment_table(connection=None):
    # 댓글 정보를 저장할 commentTable 생성
    conn, cur = connection()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS commentTable (
            C_num BIGINT AUTO_INCREMENT PRIMARY KEY, -- 댓글 번호 자동 증가
            C_number BIGINT NOT NULL,                -- 댓글이 작성된 게시글 번호
            C_writer CHAR(20) NOT NULL,              -- 댓글 작성자
            C_text VARCHAR(1000) NOT NULL,           -- 댓글 내용
            C_reg_date DATETIME DEFAULT CURRENT_TIMESTAMP, -- 댓글 작성시간
            -- C_number는 실제 존재하는 게시글 번호만 가능
            FOREIGN KEY (C_number)
                REFERENCES boardTable(b_id)
                ON DELETE CASCADE,
            -- C_writer는 실제 존재하는 회원 id만 가능
            FOREIGN KEY (C_writer)
                REFERENCES userTable(id)
        )
    """)
            


# 설계 제약 조건
# - 게시글을 삭제하면 그 글에 달린 댓글도 함께 자동으로 삭제되어야 합니다 (외래키 옵션을 활용하세요)
# - 존재하지 않는 회원 id로는 게시글이나 댓글을 작성할 수 없어야 합니다
# - 작성일은 별도 입력 없이 자동으로 채워지도록 설계하세요

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

        # 해당 ID가 있는지 확인

        cur.execute(
            "SELECT id FROM userTable WHERE id = %s",
            (user[0],)
        )
    count = cur.fetchone()

#id가 없으면 신규 회원으로 추가
    def signup(conn):
        cur = conn.cursor()
        id = input("ID: ")
        name = input("이름: ")
        email = input("이메일: ")
        addr = input("주소: ")
    if count == 0:
        cur.execute(
            "INSERT INTO userTable VALUES(%s, %s, %s, %s, %s, %s)",

            user
        )

        print(user[0],"신규 회원 추가")
    else:
        print(user[0], "이미 존재하는 회원")


    conn.commit()
    conn.close()
# 로그인
def login(conn):
    cur = conn.cursor()

    print("\n===== 로그인 =====")

    user_id = input("ID 입력: ")
    user_pwd = input("PWD 입력: ")

    # 입력받은 ID와 PWD가 둘 다 일치하는 회원을 DB에서 검색
    cur.execute(
        """
        SELECT *
        FROM userTable
        WHERE id=%s AND pwd=%s
        """,
        (user_id, user_pwd)
    )

    # 로그인은 id가 PK라서 결과가 최대 1개
    # 그래서 fetchone() 사용
    row = cur.fetchone()

    conn.close()

    # 검색 결과가 있으면 로그인 성공
    if row:
        print("로그인 성공")

        # row 구조
        # [0] id / [1] pwd / [2] name / [3] email / [4] addr
        print(f"{row[2]}님 환영합니다.")

        # 로그인된 사용자 id를 반환
        # 이후 게시글/댓글 작성자와 권한 확인에 사용
        return user_id

    else:
        print("ID 또는 비밀번호가 일치하지 않습니다.")

        # 로그인 실패했으므로 로그인 사용자가 없음
        return None

# 로그인 메뉴
def login_menu():
    while True:
        print("\n===== 로그인 메뉴 =====")

        print("1. 로그인")
        print("2. 회원가입")
        print("3. 종료")

        choice = input("선택: ")
        if choice == "1":
            # login() 반환값을 current_user에 저장
            current_user = login()
        # 로그인 성공 하면 게시판메뉴를 사용자 id로 이용해서 이동
        if current_user:
            board_menu(current_user)

# 사용자 추가 : insert()
def new_user_insert(conn):
    cur = conn.cursor()
    print("\n===== 회원가입 창=====")
    # id = input("아아디 : ")
    # if id == 'exit' : return "exit"
    # cur.execute("SELECT * FROM userTable WHERE id=%s", (id,))
    # rows = cur.fetchone()
    while True:
        id = input("아이디 : ")
        if id == 'exit': return "exit"
        cur.execute("SELECT * FROM userTable WHERE id=%s", (id,)) # DB 에게 검색을 시킴
        rows = cur.fetchone() # 검색 결과를 파이썬에서 가져올것
        if rows: # 가져온 결과를 판단
            print("중복된 아이디 입니다.")
            continue # 중복이 맞다고 판단시 다시 아이디로 돌아감
        else:
            break # 중복이 아니면 pwd로 이어짐
    pwd = input("패스워드 : ")
    name = input("이름 : ")
    mail = input("이메일 : ")
    addr = input("주소 : ")
    try:
        cur.execute("INSERT INTO userTable VALUES(%s, %s, %s, %s, %s)", (id, pwd, name, mail, addr))
        print("사용자 추가 완료!!")
    except Exception as e:
        print(f"오류 발생: {e}")

    conn.commit()


def write_post(conn, user_id):
    cur = conn.cursor()
    title = input("제목 입력: ")
    text = input("내용 입력")

    cur.execute("""
        INSERT INTO boardTable (title, text, user)
        VALUES (%s, %s, %s)
            """, (title, text, user_id))
    conn.commit()

    print("게시글 작성 완료")

    # 게시글 목록 조회

def list_posts():  # boardTable과 userTable을 JOIN해서
    # 글번호 / 제목 / 작성자 이름 / 작성일을 출력할 예정
    pass


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
def board_menu(current_user):
    # login()에서 반환받은 로그인 사용자 id가 들어옴

    while True:

        print("\n===== 게시판 메뉴 =====")

        # 현재 누가 로그인되어 있는지 확인
        print(f"현재 로그인 사용자: {current_user}")

        print("1. 게시글 작성")
        print("2. 게시글 목록")
        print("3. 게시글 상세 조회")
        print("4. 댓글 작성")
        print("5. 게시글 삭제")
        print("6. 로그아웃")

        choice = input("메뉴 선택: ")

        if choice == "1":
            # 게시글 작성할때 현재 로그인 사용자도 같이 전달
            write_post(current_user)


        elif choice == "0":
            print("로그아웃 합니다.")

            # 게시판 while문 종료
            # board_menu()가 끝나면서 다시 login_menu()로 돌아감
            break

        else:
            print("잘못된 입력입니다.")



    # create_user_table(conn)     # 테이블 생성

    def insert_initial_data(conn):
        cur = conn.cursor()
        create_boardTable(conn)
        create_comment_table(conn)
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
        elif choice == "6":
            login(conn)
        elif choice == "0":
            print("프로그램을 종료 합니다.")
            conn.close()
            break
        else:
            print("잘못된 선택입니다. 다시 입력 해 주세요.")
            conn.close()

if __name__ == "__main__":
    main()