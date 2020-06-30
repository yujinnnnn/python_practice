#end의 사용법
#기본값은 '\n'으로 엔터값이다
print("print end attribute", end=' ')

a= "파이썬 언어는 \'와 \"를 구분하지 않는다."
print(a)

a= "코로나19 사태로"
b= '온라인 강의를 합니다.'
print(a)
print(b)

a= "우리집 강아지의 이름은"
b= '야꿍이 입니다.'
print(a, end=' ') #end=" " 는 한 칸 공백임
#print(a, end='\t') 또는 print(a, end=',')
print(b)