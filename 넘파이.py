# numpy(Numerical Python)은 파이썬에서 수치 계산과 과학적 연산을 위한 핵심 라이브러리입니다.
# - 데이터의 언어는 '숫자'와 '행렬'이며 이를 효율적으로 처리 하기 위해 Numpy를 사용
# - 빅데이터 환경에서 파이썬 기본 리스트로 반복문(for) 을 돌리는 것은 매우 느립니다.
# - Numpy ㅡ이 벡터화 연산을 쓰면 수백만 개의 데이터를 순간에 처리할 수 있습니다.
# - 대규모 다차원 배열 처리
# - 고속 수학 연산 지원
# - 머신러닝, 딥러닝, 데이터 분석에서 필수적으로 사용 됨

import numpy as np # 일반적으로 np라는 별칭을 부여해 사용 함
from pandas.core.reshape import reshape
from setuptools.namespaces import flatten

# 기본 배열 생성
data = [0,1,2,3,4,5]
a1 = np.array(data)  # 리스트를 넘파이 배열로 만듬
print(data)
print(a1)

data2 = [0,1,2,3,4,.4,5.14,6.75]        # 하나의 타입으로 통일 되어 있다.
a2=np.array(data2)
print(a2)

# 문자열, 실수, 정수를 포함하는 배열을 만들어서 출력결과
data3 = [0,1,2,3,4.1,5,"1"]
a3=np.array(data3)
print(a3)
print(data3)

# 속성 확인
x = np.array([0.1,0.2,0.3])
print(x)
print(x.shape)  # 배열의 형태를 나타남
print(x.dtype)  # 요소의 데이터 타입을 반환

#특정 범위의 배열 생성
a4 = np.arange(0,10,2)     # 0~ 10 미만까지, 간격은 2
print(a4)

# 1 ~ 100까지, 간격은 3
a5 = np.arange(1,101,3)
print(a5)
# 0 ~ 50 미만, 간격은 5
a6 = np.arange(0,50,5)
print(a6)

# 2차원 배열 생성
a7 = np.arange(12). reshape(4,3)
print(a7)
print(a7.shape)


# 동일한 간격으로 데이터 생성
a8 =np.linspace(1,10,11)
print(a8)

# numpy 기초 실습

# 1. 리스트 [10,20,30,40,50]을 Numpy 배열로 만들어 arr1에 저장하고, 배열과 type(arr1)을 출력하세요
arr1 = np.array([10,20,30,40,50])
print(arr1.dtype)
print(arr1)

# 2. np.array([True, 1,2])의 출력 결과와 dtype의 무엇일까요
arr2= np.array([True,1,2])
print(arr2)
print(arr2.dtype)


# 3. 2행 2열 배열 [[1,2,3,]] , [4,5,6] ]을 만들고 shape와 dtype을 출력하세요
arr3 = np.array([[1,2,3],[4,5,6]])
print(arr3.shape)
print(arr3.dtype)

# 4. np.arange()을 사용해 2부터 20까지 (20포함 ) 짝수 배열을 만드세요
arr4 = np.arange(2,21,2)
print(arr4)

# 5. np.arange()을 사용해 [10 ~ 1까지 역순을만드세요.
arr5 = np.arange(10,0,-1)
print(arr5)

# 6. np.arange() 을 사용해0부터 1 미만까지 0.1 간격의 배열을 만들고 요소가 몇 개인지 출력 결과로 확인하세요
arr6= np.arange(0,1,0.1)
print(arr6)
print(len(arr6))


# 특정 숫자로 채워진 배열
a8 = np.zeros(10)
print(a8)
a9 = np.zeros((3,4))
print(a9)

a10 =np.ones(10)
print(a10)

a11 =np.eye(4)      # 4 x 4
print(a11)


#배열의 데이터 타입의 변환

a13 = np.array(['1.5','0.62','2','3.14','3.141592' ])
print(a13)
print(a13.dtype)        # <U8의 의미는 데이터 형식이 유니코드이며 문자의 수는 최대 8개라는 의미

num_a13 = a13.astype(float)  # 문자열을 실수 타입으로 변환
print(num_a13)

a14 = np.array(['1','3','5','7','9'])
num_a14 = a14.astype(float)  # 문자열을 정수 타입으로 변환
print(num_a14)

# 난수 배열의 생성
# rand() : 0 ~ 1 미만의 실수로 난수배열을 생성
a15 = np.random.rand(2,3)
print(a15)

a16 = np.random.rand(2,3,4)
print(a16)

# randimt(): 지정된 범위에 해당하는 정수로 난수 배열을 생성
a17 = np.random.randint(10, size =(5,4))     # 0 ~ 9 사이의 난수
print(a17)

# 실습 문제2
# 1.  0 으로 채워진 요소 5개짜리 1차원 배열을 만들고, 배열과 dtype을 출력하세요.
arr7 = np.zeros(5)
print(arr7)
print(arr7.dtype)

# 2. 0 채워진 3행 5열을 만들고 shape을 출력하세요.
arr8 = np.zeros((3,5))
print(arr8.shape)
# 3.  1로 채워진 2행 4열 배열을 만든 뒤, astype()을 사용해 정수행으로 변환하여 출력하세요
ar3 = np.ones((2, 4)).astype(int)
print(ar3)
# 4. np.eye()로 5 x 5배열을 만들어 출력하고, 이런 형태의 행렬을 무엇이라고 부르는지, dtype은 무엇인지 확인하세요.
arr10=np.eye(5)
print(arr10)
print(arr10.dtype)
# 5. 배열 np.array(['10', '20', '30', '40'])의 dtype을 출력한 뒤 , 정수형으로 변환하고 변환 후의 dtype도 출력
arr11= np.array(['10','20','30','40'])
print(arr11.dtype)
num_arr11 = arr11.astype(float)
print(num_arr11.dtype)

# 6. 0 ~ 1 미만의 실수 난수로 4행 3열 배열을 만들고 shape를 출력하세요.
arr12 = np.random.rand(4,3)
print(arr12)
print(arr12.dtype)
print(arr12.shape)

# 7 . np.random.randint를 사용해 주사위를 10번 던진뒤 결과 (1~6)를 1차원 배열로 만드세요.
arr13 = np.random.randint(1,7,size=(10))
print(arr13)

# 8. 0~ 99 사이의 정수 난수 12개를 1차원 배열로 만든뒤, 다음을 순서대로 수행하세요.
arr14 = np.random.randint(0,99,size=(12))
arr14 = arr14.reshape(3,4)
arr14 = arr14.astype(float)
print(arr14)
print(arr14.dtype)


# 연산과 함수
a18 = np.array([1,2,3])
a19 = np.array([4,5,6])
print(a18 + a19)
print(a18 * a19)
print(a18 / a19)

a20 = np.array([10,20,30,40,50])
print(a20>20)   # True/ False 반환

# 통계 연산

a21 = np.arange(10)
print(f"합계: {a21.sum()}, 평균 : {a21.mean()}")
print(f"표준편차 : {a21.std()}, 분산 : {a21.var()}")
print(f"최솟값: {a21.min()}, 최댓값 : {a21.max()}")

# 문제1 배열 생성 및 연산
ar1= np.arange(1,11)
result =ar1 +5
print(result)

# 문제 2 2차원 배열 만들기 1- 9까지 3x3크기의 2차원 배열 생성하고 출력하기
ar2 = np.arange(1,10).reshape(3, 3)
print(ar2)


# 문제 3 배열 의 통계연산
ar3 = np.arange(21)
print(f"합계: {ar3.sum()}, 평균 : {ar3.mean()}")
print(f"표준편차 : {ar3.std()}, 분산 : {ar3.var()}")
print(f"최솟값: {ar3.min()}, 최댓값 : {ar3.max()}")

#문제 4 난수생성 및 필터링   0에서 100 사이의 난수를 10개 생성하고, 50 이상인 값을 출력
ar4 = np.random.randint(0, 101, size=10)
print(ar4[ar4 >= 50])

#동전 던지기 확률 시험
# 1. 100번의 동전던지기
coin = np.random.randint(0,2,size=100)


# 2. 각 면이 나온 횟수 계산
heads =np.sum(coin ==1) # 앞면의 수 : 1의 개수
tails =np.sum(coin == 0)    # 뒷면의 수: 전체-앞면

# 3. 확률 계산
head_ratio = heads/ len(coin) * 100
tail_ratio = heads/ len(coin) * 100

# 4. 결과 출력
print( "앞면 횟수:", heads, f"({head_ratio:.1f}%)")
print( "뒷면 횟수:", tails, f"({tail_ratio:.1f}%)")
