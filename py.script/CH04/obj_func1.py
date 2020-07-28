#객체의 함수화

class Call_Object:
    def __init__(self,n):
        self.n = n
    def __call__(self,x):
        return self.n + x

add_3 = Call_Object(3)
print(add_3(5))

#callable 내장 함수를 이용하여 객체의 호출여부를 판단
print(callable(add_3))