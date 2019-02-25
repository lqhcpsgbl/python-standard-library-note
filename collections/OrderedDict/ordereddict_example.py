# An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged.

from collections import OrderedDict

d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

od = OrderedDict()

for i in d:
  # print(i, d[i])
  od[i] = d[i]

print(od)

# pineapple 在最后位置
od['pineapple'] = 10
print(od)
# apple 位置不变
od['apple'] = 0
print(od)
