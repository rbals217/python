# 판다스: Pandas 는 테이블 형태의 데이터를 쉽게 다룰 수 있도록 설계된 파이썬 데이터 분석 라이브러리
# - 데이터 전처리, 탐색, 변환 및 시각화 등에 작업에 널리 사용
# - 행과 열의 구조로 구성된 데이터를 직관적으로 다룰수 있게 해줌
# - Series( 1차원), DataFrame(2차원) 구조 지원
# - 다야한 데이터 파일(csv, Excel, SQL, JSOn)불러오기 가능
# - 결측치 처리, 정렬, 그룹화, 필터링, ㅗㅌㅇ계 분석 등 풍부한 기능 제공
# - 시계열 데이터 처리 기능 내장

# Series - 1차원  데이터 구조 : 리스트와 유사 하지만, 각 데이터에 인덱스(라벨)가 붙음
import pandas as pd
s1 = pd.Series([10,20,30,40,50])
print(s1)

# DataFrame _ 2차원 데이터 구조: 여러개의 Series가 모여 이루어짐. 행과 열로 구성됨
data = {
    '이름': ['민지','하니','다니엘'],
    '수학': [95,85,75],
    '영어': [90,85,94]

}
df = pd.DataFrame(data)
print(df)

# 특정 행 및 열 추출
print(df['수학']) # 열 추출
print(df.loc[0])    # 행 추출
print(df.loc[1,'영어'])   # 특정 행의 열 추출


# 새로운 열 및 행 추가
df['과학'] =[93,89,87]        # 새 열 추가
df.loc[3] = ['혜인',92,89,77]
print(df)

# 기본 연산
print(df['수학'].sum())   #합계
print(df['수학'].mean())  #평균
print(df['수학'].max())   # 최대값
print(df['수학'].min())   #최소값

# 열 추가
df['반']= [1,1,2,2]
print(df)

print(df.groupby('반')['수학'].mean())

# 1 exam.csv 를 읽어오고 전체 행 개수를 출력
df = pd.read_csv('exam.csv')
print(len(df))
# 2 . 수학만 출력
print(df['math'])
# 3. 수학점수가 50점 이상인 학생만 필터링
filtered_df = df[df['math']>50]
print(filtered_df)

# 4.    영어 점수의 평균을 계산하여 출력
print(df['english'].mean())

# 5 데이터 프레임을 새로운 CSV 파일로 저장하세요.
df.to_csv('exam.csv', index=False)

 # 6. 각 학급별 수학과 영어 점수의 평균을 동시에 구하시오,.
print(df.groupby('nclass')[['math', 'english']].mean())

# 7 각 학급별 수학 점수의 최대값과 최소값을 동시에 구하시오
print(df.groupby('nclass')['math'].agg(['max','min']))

# 8 새 데이터 프레임으로 만들어서 추가
data = {
    '제품': ['사과', '딸기', '수박'],
    '가격': [1800,1500,3000],
    '판매량': [24,38,13]
}
df = pd.DataFrame(data)
print(df)