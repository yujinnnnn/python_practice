for i in range(5):
    for j in range(i, 5):
        print("*", end = '')
    print()


#while문
i=0
while i<5:
    j=i
    while j < 5:
        print("*", end='') 
        j += 1
    print()
    i +=1

for i in range(5,0,-1):
    print("*"*i)