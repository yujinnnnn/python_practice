from collections import defaultdict

my_list = [('a', 10),('b',20),('a',100),('c',30),('d',40),('c',300)]
my_dict=defaultdict(list)
for v1,v2 in my_list:
    my_dict[v1].append(v2)

print(my_dict)
print(my_dict.items())