class Board():
  def __init__(self, width, length, color):
    self.width = width
    self.length = length

    self.color = color

  def __repr__(self):
    return "{}".format('\n'.join(["{}".format([self.color for i in range(self.length)]) for _ in range (self.width)]))
