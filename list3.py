cars = [["so",'ava',"grand"],["tus",'aus'],["has",'min',"coop","vol"]]
for i in range(len(cars)):
    for j in range(len(cars[i])):
        print("%10s"%cars[i][j], end="")
    print()