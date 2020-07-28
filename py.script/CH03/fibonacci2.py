#딕셔너리를 이용한 메모화(동적 프로그래밍) 기능 사용
fibo_dict = {
    1:1,
    2:1
}

def fibo(n):
    if n in fibo_dict:
        return fibo_dict[n]
    output = fibo(n-1) + fibo(n-2)
    fibo_dict[n] = output
    return output

#여러 개의 피보나치 수열 생성
def fibo(n):
    if n<0:
        print(f'range out number')
        return
    elif 0<=n<=1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

if __name__ == '__main__':
    try:
        num = int(input("fibonacci number >> "))
        result = []
        for i in range(num):
            result.append(fibo(i))
        print(f'{num}개의 피보나치 --> {result}')
    except:
        print('wrong format')