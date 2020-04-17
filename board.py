class Board():
  def __init__(self, width, length, color):
    self.width = width
    self.length = length

    self.rotation = False
    self.color = color

  def __repr__(self):
    return "{}".format('\n'.join(["{}".format([self.color for i in range(self.length)]) for _ in range (self.width)]))

  def rotate(self):
    # Something that I am concerned about, if a Board is placed on a Sheet, and then it is rotated for some reason, what happens?
    self.width, self.length = self.length, self.width
    # Toggle rotation each time rotate is called. 
    self.rotation != self.rotation
