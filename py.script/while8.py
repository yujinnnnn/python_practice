lower_s, upper_s = '',''
print("입력되는 모든 영문자들을 대문자로 변환하는 프로그램")
print("*"*60)
while True:
    lower_s = input("문자를 입력하세요 >> ")
    if lower_s == 'quit':
        break
    upper_s = lower_s.upper()
    print(lower_s, "-->", upper_s)
