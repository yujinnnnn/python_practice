month = int(input("Enter month >> "))
if month ==2:
    print(month, "월 :: 28일")
elif month in [ 1,3,5,7,8,10,12]:
        print(month, "월 :: 31일")
elif month in [4,6,9,11]:
        print(month, "월 :: 30일")
else: 
    print("잘못입력")
