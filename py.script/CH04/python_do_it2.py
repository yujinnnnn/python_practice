import turtle as t

def turtle_circle(n):
    t.bgcolor('black')
    t.color('pink')
    t.speed(0)
    for i in range(n):
        t.circle(100)
        t.left(360/n)

def turtle_taegeuk():
    t.bgcolor('black')
    t.speed(0)
    t.shape('turtle')
    for i in range(200):
        if i % 3 ==0:
            t.color('red')
        elif i % 3 == 1:
            t.color('yellow')
        else:
            t.color('blue')
        t.forward(i*2)
        t.left(119)

if __name__ == "__main__":
    select = int(input("번호를 1,2번 중 선택 >> "))
    if select == 1:
        turtle_circle(100) #()은 반지를 수치
    elif select == 2:
        turtle_taegeuk()
    else:
        print("번호를 잘못 입력했습니다.")

