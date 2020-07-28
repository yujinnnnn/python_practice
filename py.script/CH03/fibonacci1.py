def fibo(n):
    if n<0:
        print(f'range out number')
        return
    elif 0<=n<=1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

fibo_n = int(input("fibonacci number >> "))
print(fibo(fibo_n))