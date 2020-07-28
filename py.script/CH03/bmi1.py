def bmi_f(h,w):
    b=0.0
    h=h/100
    b=w/(h**2)
    return b

height, weight, bmi =0.0,0.0,0.0
height = float(input("Enter your height >> "))
weight = float(input("Enter your weight >> "))

bmi = bmi_f(height, weight)
if bmi >= 20 and bmi<= 24:
    print("표준체중")
elif bmi < 20:
    print("저체중")
else:
    print("과체중")