# DefaultDict: dict has default value of any key

from collections import defaultdict

colors = ['red', 'blue', 'red', 'green', 'blue', 'blue', 'black']

d = defaultdict(list)
for i in colors:
  d[i].append(i)

print(d)
