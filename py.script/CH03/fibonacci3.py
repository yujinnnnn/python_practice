def fibo_loop(n):
    f1,f2 = 1,-1
    result = []
    for i in range(n):
        tmp = f1
        f1 += f2
        f2 = tmp
        result.append(f1)
    return result

if __name__ == '__main__':
    try:
        num = int(input("fibonacci number >> "))
        print(f'{fibo_loop(num)}')
    except:
        print('wrong format')