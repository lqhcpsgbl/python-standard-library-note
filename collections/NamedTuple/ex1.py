# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

n = int(input())
columns = input()

total = 0
fileds = ','.join(columns.split())
Record = namedtuple("Record", fileds)

for i in range(n):
  line = input()
  record = Record(*line.split())
  total += float(record.MARKS)

res = '%.2f' % (total / n)
print(res)
