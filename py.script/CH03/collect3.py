from collections import Counter

#1번
text=list("collection chocolate")
print(text)
text_c=Counter(text)
print(text_c)
print(text_c['c'])

#2번
text="Happy families are all alike; every unhappy family is unhappy in its own way.\
    All happy families are alike; each unhappy family is unhappy in its own way".lower().split()

c_dict = Counter(text)
print(c_dict)
c_list=Counter({'happy':3, 'unhappy':2})
print(list(c_list.elements()))