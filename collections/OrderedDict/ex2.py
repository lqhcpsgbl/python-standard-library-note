#!/bin/python3

from collections import OrderedDict

if __name__ == '__main__':
  n = int(input())
  adict = OrderedDict()

  for i in range(n):
    word = input()
    if word not in adict:
      adict[word] = 1
    else:
      adict[word] += 1
  print(len(adict))
  for key in adict:
    print(adict[key], end=' ')