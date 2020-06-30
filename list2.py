

total, avg = [0,0,0], [0.0,0.0,0.0]
points = [[90,70,100],[85,99,94],[87,89,98]]
for i in range(3):
    for j in range(3):
        total[i] += points[i][j]
    avg[i] = total[i]/3
for i in range(3):
    print("#%d :: %.2f"%(i+1, avg[i]))