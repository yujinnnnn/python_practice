while True:
    digit = int(input("정수를 입력하시오 > "))
    count = 0
    if digit <= 1:
        print("program end!")
        break
    else:
        for i in range(2, digit+1):
            if digit % i== 0:
                count +=1
        if count == 1:
            print("%d is prime number"% digit) 
        else:
            print("%d is not prime number"% digit)
    print()