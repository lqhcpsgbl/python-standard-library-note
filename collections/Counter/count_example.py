# Counter: dict subclass for counting hashable objects 

from collections import Counter

colors = ['red', 'blue', 'red', 'green', 'blue', 'blue', 'black']
colors_counts = Counter(colors)

print(colors_counts)
for i in colors_counts.elements():
  print(i)

# 取前两个最多出现的
print(colors_counts.most_common(2))

other_colors = ['red', 'blue', 'green']
# 做减法,可能出现负数
colors_counts.subtract(other_colors)
print(colors_counts)
# 做加法
colors_counts.update(other_colors)
print(colors_counts)
