from dataclasses import dataclass

data="""3,4,3,1,2""".split(',')

@dataclass
class lf:
  t: int = 8

  def cycle(self):
    n = False

    if self.t == 0:
      self.t = 7
      n = True

    self.t -= 1

    return n

f = []
for i in data:
  f.append(lf(int(i)))

for day in range(1, 81):
  for sh in f:
    if sh.cycle():
      f.append(lf(9))
  print(f"After {day} {len(f)}")
