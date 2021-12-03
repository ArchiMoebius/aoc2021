path="""forward 5
down 5
forward 8
up 3
down 8
forward 2"""

class sub():
  def  __init__(self):
    self.hp = 0
    self.vp = 0
    self.move = {
      "forward": self.forward,
      "down": self.down,
      "up": self.up,
    }

  def forward(self, i):
    self.hp += int(i)

  def down(self, i):
    self.vp += int(i)

  def up(self, i):
    self.vp -= int(i)

  def load(self, path):
    for entry in path:
      action, amount = entry.split(' ')

      if self.move.get(action, False):
        self.move[action](amount)

  @property
  def position(self):
    return self.hp * self.vp

yellow = sub()

yellow.load(path.split('\n'))

print(yellow.position)
