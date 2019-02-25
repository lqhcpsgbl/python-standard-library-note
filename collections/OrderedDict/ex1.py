# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict

n = int(input())
total = OrderedDict()

for i in range(n):
  line = input()
  line_data = line.split()
  name, price = ' '.join(line_data[:-1]), int(line_data[-1])
  if name not in total:
    total[name] = price
  else:
    total[name] += price

for key, value in total.items():
  print(key, value)