# 연산자 오버로딩은 내장 연산자를 사용자 정의 클래스에 대해 다르게 동작하도록 재정의
# add = '+' 연산자에 대응, 객체끼리 덧셈 연산 정의
# sub = '-' '', 객체끼리 뺄셈 연산 정의
# __mul__ = '*': "" 객체끼리 곱셈 연산 정의
# __div__ = '/' : 객체끼리 나눗셈 연산 정의
# __eq__ = '==' : 객체끼리 동등성 비교 정의함.

class Vector2D:
    def __init__(self,x ,y):
        self. x = x
        self. y = y

    def __add__(self,other):
        return Vector2D(self. x + other.x ,  self.y + other.y)

    def __eq__(self, other):
        return self.x ==other.x and self.y == other.y

v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)

v3 = v1 + v2        # '+' 연산자가 __add__ 메서드를 호출합니다.
print(v3.x, v3.y)

print(v1 == v2)     # '==' 연산자가 __eq__ 메서드를 호출합니다.


