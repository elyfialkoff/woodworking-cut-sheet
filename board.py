class Board():
  def __init__(self, side_1, side_2, color):
    if side_1 < side_2:
      self.smaller = side_1
      self.bigger = side_2
    else:
      self.smaller = side_2
      self.bigger = side_1

    self.color = color