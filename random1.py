import random as rand

print(rand.random())
print(rand.uniform(0,20))
print(rand.randrange(10))
print(rand.randrange(1,47))
print(rand.choice(["p","y","t","h","o","n"]))
o_list=["p","y","t","h","o","n"]
rand.shuffle(o_list)
print(o_list)
print(rand.sample([1,2,3,4,5,6],k=2))