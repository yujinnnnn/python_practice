membership = ''
point = int(input("customer point >> "))
while True:
    if point <0:
        break
    else:
        if point >= 300:
            membership = "VIP"
        else:
            membership = "Family"
    print(f'customer membership is {membership}')
    break