from collections import OrderedDict

d = OrderedDict()
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['q'] = 400
print(d)

from collections import defaultdict

my_dict=defaultdict(lambda:0)
print(my_dict['a'])