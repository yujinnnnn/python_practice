class YouClass:
    "데이터를 정상적으로 설정하고 반환하는 데이터 디스크립터"
    def __init__(self,val=None, name='you'):
        self.val = val
        self.name= name

    def __get__(self, obj, objtype):
        print(f'YouClass, {self.name}')
        return self.val

    def __set__(self, obj, val):
        print(f'ReBinding, {self.name}')
        self.val= val

class MeClass:
    x = YouClass(100,'x')
    y = 5

me = MeClass()
print(me.x)
me.x = 200