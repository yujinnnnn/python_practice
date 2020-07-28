# count= 1
# while True:
#     print("Hi Python")
#     count += 1
#     if count>5:
#         break #if문이랑 함께 자주 사용함


import time
number = 0
tick = time.time() +5    #5초 동안 반복 수를 출력하는 코드 작성
while time.time()< tick:
    number +=2
print(f'5초 동안 {number}번 반복했습니다.') 


