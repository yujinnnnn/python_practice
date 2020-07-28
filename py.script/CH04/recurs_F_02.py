#1
def fact(n):
    if n <0 or n!= int(n):
        print("wrong input!!")
        return
    elif n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

n=int(input("factorial number >> "))
result = fact(n)
print(f'{n}! == {result}')

#2
import math

n=int(input("factorial number >> "))
result = math.factorial(n)
print(f'{n}! == {result}')

#3
def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i 
    return fact

value = int(input("Enter number >> "))
result = factorial(value)
print("factorial of %d :: %d" %(value, result))