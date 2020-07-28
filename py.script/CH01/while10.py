# sum = 0
# num = int(input("수를 입력하세요 >> "))
# for i in range(1, num+1):
#     if i % 7 == 0:
#         continue
#     sum += i
# print("1~%d 까지의 합산은 %d"%(num, sum))

a = input("문자열을 입력하세요 >> ")
num = len(a) 
for i in range(num,0,-1):
    for j in range(i-1, num, 1):
        print(a[j], end="")
    print()
