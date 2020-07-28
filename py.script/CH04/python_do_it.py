
def real_num(num):
    var = []
    var.append(int(num))
    var.append(num-var[0])
    return var
    
def cal_data():
    num = float(input("실수값을 입력하세요 >> "))
    result = real_num(num)
    print(f'{result[0]},{result[1]:0.6f}')

if __name__ == "__main__":
    cal_data()