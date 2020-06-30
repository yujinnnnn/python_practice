import collections
person = collections.namedtuple('person',['name','age','grade'])
p= person('고려',20, '1학년')
print(p[0])
print(p.name)