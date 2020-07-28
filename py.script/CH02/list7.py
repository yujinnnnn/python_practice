import random
x = []
while True:
    x.append(random.randrange(1,46))
    for i in range(len(x)):
        for j in range(i):
            if x[i] == x[j]:
                x.pop(j) 
                break
    if len(x) ==6:
        break
for i in range(6):
    print("%4d"%x[i], end='')
print()

temp =[]
for i in range(1,46):
    temp.append(i)
lotto = random.sample(temp, k=6)
print(lotto)