from numpy import array

from collections import Counter

d = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".split('\n')

l = array([array(list(e), dtype=int) for e in d])

x = []
for y in range(0, 5):
  x.append(Counter(l[:, y]))

gamma = int(''.join([str(c.most_common()[0][0]) for c in x]), 2)
epsilon = int(''.join([str(c.most_common()[-1][0]) for c in x]), 2)

pc = gamma * epsilon

print(pc)
