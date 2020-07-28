import random as rd
Com_num = rd.randrange(1,31)
count = 0
your_num =[]
for i in range(3):
    temp = int(input("숫자를 입력하세요 >> "))
    if Com_num == temp:
        print("맞았습니다! ")
        your_num.append(temp)
        break
    else:
        your_num.append(temp)
        count +=1
if count ==3: 
    print("실패하였습니다.")
print("당신이 입력한 수는 " , your_num)
print("컴퓨터가 입력한 수는 " ,Com_num)
print()