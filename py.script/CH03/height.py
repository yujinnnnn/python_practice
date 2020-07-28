# students = {50: ["Alice",21], 20:["Anna",22],60:["Michle",21],10:["Jane",22],80:["John",22], 80:["John",20]}
# s_keys = list(syudents.keys())
# s_keys.sort()
# print(f'value of max key: {students[s_keys[-1]]}')
# print(f'value of min key: {students[s_keys[0 ]]}')

a=[]
a = input("단어를 입력하세요 >> ") 
while True:
    if a == "quit":
        print("program end!")
        break
    else:
        if a[0] ==a[-1]:
            print(a ,"is pailndrome")
        else: 
            print(a, "is not palindrome")
        break
        print()

