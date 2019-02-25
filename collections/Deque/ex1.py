# https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque

d = deque()

n = int(input())

for i in range(n):
  operation = input().strip()
  if operation == 'pop':
    d.pop()
  elif operation == 'popleft':
    d.popleft()
  elif 'appendleft' in operation:
    data = int(operation.split()[-1])
    d.appendleft(data)
  else:
    data = int(operation.split()[-1])
    d.append(data)

for i in d:
  print(i,end=' ')
