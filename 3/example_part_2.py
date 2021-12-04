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

def gd(d):
  l = array([array(list(e), dtype=int) for e in d])

  x = []
  for y in range(0, len(d[0])):
    x.append(Counter(l[:, y]))

  return [c.most_common() for c in x]

def cd(descrim):
  ox = []
  co = []

  for e in descrim:

    if len(e) > 1 and len(e[0]) > 1 and len(e[1]) > 1:
      if e[0][1] == e[1][1]:
        ox.append(1)
        co.append(0)
      else:
        ox.append(e[0][0])
        co.append(e[1][0])
    else:
        ox.append(-1)
        co.append(-1)
    
  return co, ox

def reduce(canidates, index, dsc, bt):
  x = cd(dsc)
  descrim = x[bt]
  cn = []

  for e in canidates:
    if int(e[index]) == descrim[index]:
      cn.append(e)

  if len(cn) > 1:
    return reduce(cn, index+1, gd(cn), bt)
  elif len(cn) == 1:
    return int(cn[0], 2)
  else:
    return cn

descrim = gd(d)
print(reduce(d, 0, descrim, 1)*reduce(d, 0, descrim, 0))
