for i in range(1,10):
    if i <= 5:
        for j in range(6-i):
            print(" ", end='')
        for k in range(0,i*2-1):
            print('\u2665', end='')
        print()
    else:
        for j in range(i-4):
            print(" ", end='')
        for k in range(0,(9-i)*2+1): 
            print('\u2605', end='')
        print()