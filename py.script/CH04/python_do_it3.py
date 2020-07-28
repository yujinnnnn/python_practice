def phone_num(number):
    n= len(number)
    answer = number.replace(number[:n-4],'*'*(n-4))
    return answer

if __name__ == "__main__":
    num = input("enter phone number >> ")
    print(f'origin: {num}, return:{phone_num(num)}')
