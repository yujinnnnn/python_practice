# #Property Class : 특별한 디스크립터 객체를 생성하는 내장 class

# #정의
# class Property_test:
#     def __init__(self,name):
#         self._name = name

#     def get_name(self):
#         return self._name

#     def set_name(self, name):
#         self._name = name

#     def delete_name(self):
#         del self._name

# name = property(get_name, set_name ,delete_name,'property test')

# #실습1
# me = Property_test("Korea")
# print(id(me.name))

# print(me.name) #get_name이 자동 실행
# me.name = 'Industrial' #set_name이 자동 실행
# print(me.name) #get_name 
# print(me.__dict__)

#실습2 <-더 사용하기 쉬움
class Property_test:
    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name_v):
        self._name = name_v

me = Property_test("Korea")
print(me.name) #get_name이 자동 실행
me.name = "Industrial"
print(me.name)
