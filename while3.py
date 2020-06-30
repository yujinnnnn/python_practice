# for i in range(0,3,1):
#     for k in range(0,2,1):
#         print("출력함수 실행, i: %3d\tk:%3d"%(i,k))
#     print("*"*30)


number = int(input("수를 입력하세요 >> "))
sum = 0
while True:
    if number < 0:
        print("program end!")
        break
    else:
        for i in range(0,number+1):
            sum += i
        print("1 ~ %d 까지의 합산은 %d"% (number, sum))
    break

for i in range(1,10):
    print("i: %d" % i)
    #continue
    print("%d 의 거듭제곱: %d"%(i, i**2))


