import numpy as np

from numpy.lib.stride_tricks import sliding_window_view

a = """199
200
208
210
200
207
240
269
260
263"""

window_sums = np.sum(sliding_window_view(np.array(a.split('\n'), dtype=int), window_shape=3), axis = 1)

l = window_sums[0]
i = 0

for e in window_sums:

  if int(e) > l:
    i += 1
    print(f"{e} > {l} == {i}  (increased)")
  else:
    print(f"{e} <= {l} == {i}")

  l = int(e)

print(i)
