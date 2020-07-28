items = ((1,2,3),(4,5,6,7))
print(items[0][1])
print()

for i in range(len(items)):
    for j in range(len(items[i])): 
        print("%3d"%items[i][j], end='')
    print()