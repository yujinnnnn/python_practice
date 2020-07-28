def recur_f(num):
    if num == 0: #재귀함수는 반복문으로 대체 가능하다.
        return 0
    else:
        return num+recur_f(num-1)

value = int(input("Enter number >> "))
result = recur_f(value)
print("sum of %d :: %d" %(value, result))