def change(a,b, *args):
    print(args)
    print(type(args))

def testF(*var):
    x,y,*z=var
    print("%d, %d, %s" %(x,y,z)) #집합형 자료형중 list는 %s 출력가능
    print(type(z))

change(1,2,3,4,5,6)
testF(1,2,3,4,5,6)