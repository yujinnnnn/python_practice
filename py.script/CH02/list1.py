lists1 = []
lists2 = []
value =1
for i in range(3):
    for j in range(4):
        lists1.append(value)
        value += 1
    lists2.append(lists1)
    lists1 = [] 
for i in range(3):
    for j in range(4):
        print("%3d"%lists2[i][j],end='')
    print()