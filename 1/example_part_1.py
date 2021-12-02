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

l = 199
i = 0

for e in a.split('\n'):

  if int(e) > l:
    i += 1
    print(f"{e} > {l} == {i}  (increased)")
  else:
    print(f"{e} <= {l} == {i}")

  l = int(e)

print(i)
