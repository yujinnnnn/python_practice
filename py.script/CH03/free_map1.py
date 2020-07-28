def printer(msg):
    text="Python"
    def inner_print():
        print(text,msg) #text와 msg가 프리변수
    return inner_print #1

tmp= printer("Hello") #2 python Hello 출력안됨
tmp() #3 python Hello 출력
tmp2 = printer("hi")
tmp2() #4 Python hi 출력