# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

from collections import defaultdict

line = input()
n, m = map(int, line.split())
a_group = []
b_group = []

occor_index = defaultdict(list)

for i in range(n):
  a_group.append(input())

for i in range(m):
  b_group.append(input())

for index, num in enumerate(a_group):
  occor_index[num].append(index + 1)

for num in b_group:
  if num in occor_index:
    print(' '.join(map(str, occor_index[num])))
  else:
    print(-1)