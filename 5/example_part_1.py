from copy import deepcopy

import numpy as np

data="""0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".split('\n')

class Line:
  def __init__(self, txt):
    xy1,xy2 = e.split(' -> ')

    self.x1, self.y1 = xy1.split(',')
    self.x2, self.y2 = xy2.split(',')

    self.x1 = int(self.x1)
    self.x2 = int(self.x2)
    self.y1 = int(self.y1)
    self.y2 = int(self.y2)

    if self.x1 > self.x2:
      t = self.x1
      self.x1 = self.x2
      self.x2 = t
  
    if self.y1 > self.y2:
      t = self.y1
      self.y1 = self.y2
      self.y2 = t

  def h_or_v(self):
    return self.x1 == self.x2 or self.y1 == self.y2

  def __str__(self):
    return f"{self.x1},{self.y1} -> {self.x2},{self.y2}"

class grid:
  def __init__(self, mx, my, lines):
    self.grid = np.zeros((mx+1, my+1))

    for line in l:
      if line.h_or_v():
        for x in range(line.x1, line.x2+1):
          for y in range(line.y1, line.y2+1):
            self.grid[y][x] += 1

    self.pts = np.argwhere(self.grid >= 2)

l = []
mx = 0
my = 0

for e in data:
  line = Line(e)
  mlx = max(line.x1, line.x2)
  mly = max(line.y1, line.y2)

  if mx < mlx:
    mx = mlx

  if my < mly:
    my = mly

  l.append(line)

g = grid(mx, my, l)

print(g.pts, len(g.pts))
