from copy import deepcopy

import re

import numpy as np

d="""7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7""".split('\n')

def parse(d):

  m = False
  b = []
  tb = []
  s = False
  c = 0

  for e in d:

    if ',' in e:
      m = [int(i) for i in e.split(',')]
      continue

    if not m:
      continue

    if s:
      tb.append([int(i) for i in re.sub('\s+', 'x', e.strip()).split('x')])
      c += 1

      if c == 5:
        s = False
        b.append(tb)
        tb = []

    if e.strip() == "":
      s = True
      c = 0

  return m, np.array(b)

def board_won(board):
  for e in np.sum(board, axis=0):
    if e == -5:
      return True

  for e in np.sum(board, axis=1):
    if e == -5:
      return True

  return False

def find_winner(moves, boards):
  ba = deepcopy(boards)

  for m in moves:
    i = 0
    for board in boards:
      board[board == m] = -1

      if board_won(board):
        board[board == -1] = 0
        return board.sum() * m

      i += 1

print(find_winner(*parse(d)))
