# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

total = 0

x = input()
line = input()
shoes_num = map(int, line.split())
shoes_left = Counter(shoes_num)
n = int(input())
lines = []
for i in range(n):
  line = input()
  lines.append(map(int, line.split()))

for ele in lines:
  shoe_size, offer = ele
  shoes_left[shoe_size] -= 1
  if shoes_left[shoe_size] >= 0:
    total += offer
print(total)

