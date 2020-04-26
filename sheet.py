import numpy as np

from board import Board

class Sheet():

  notCutYet = '-'

  def __init__(self, width, length):
    self.width = width
    self.length = length
    self.sheet = np.array([[Sheet.notCutYet] * width] * length)

    self.boards = list()

  def __repr__(self):
    return "{}".format(self.sheet) 

  def drawBoardOnSheet(self, board, x_0, y_0):
    """
    This method will take a board (width, length) and alters the sheet to indicate where the board can be cut from
    This method uses a starting position of x_0, y_0 (and uses the width, length of the board)
    This method can rotate the board so no need to worry about widths and lengths
    """
    x_1 = x_0 + board.width - 1
    y_1 = y_0 + board.length - 1
    
    # loop over width, length
    for i in range(self.length):
      for j in range(self.width):
        # validate current width, length iterators are within the size of the board
        if i >= y_0 and i <= y_1 and j >= x_0 and j <= x_1:
          # validate that the current position has not be claimed already
          if self.sheet[i][j] == Sheet.notCutYet:
            self.sheet[i][j] = board.color
          # throw an error if the sheet has already been claimed
          else:
            return False
            # msg = 'board cannot be cut at [{}][{}] since the sheet has already allocated this portion to another board'.format(j, i)
            # raise Exception(msg)

    # I want to keep track of the boards, and where they are located on the sheet so that I can remove it later
    self.boards.append(board)

    return True

  def removeBoardFromSheet(self, board, x_0, y_0):
    """
    set the board's color back to notCutYet, and make the space free
    """
    for r, _ in enumerate(range(self.length)):
      if r >= y_0 and r <= y_0 + board.length: 
        for c, _ in enumerate(range(self.width)):
          if c >= x_0 and c < x_0 + board.width:
            if self.sheet[r][c] == board.color:
              self.sheet[r][c] = self.notCutYet
            else:
              print("Something appears wrong at ({}, {})".format(r, c))


  def doesBoardFitOnSheetAt(self, board, x_0, y_0):
    """
    return True if the board fits on the sheet at the desired origin (x_0, y_0)
    does not tell you the rotation status of the fit
    """
    fitWithinBounderies = self.doesBoardFitWithinBounderiesOfSheet(board, x_0, y_0)
    internalConflictFree = self.isBoardFreeOfConflictsOnSheet(board, x_0, y_0)
    return fitWithinBounderies and internalConflictFree

  def doesBoardFitWithinBounderiesOfSheet(self, board, x_0, y_0):
    result = (x_0 + board.width <= self.width) and (y_0 + board.length <= self.length)
    return result

  def isBoardFreeOfConflictsOnSheet(self, board, x_0, y_0):
    # Check the current placement of the board to determine if it will have any conflicts. 
    for r, row in enumerate(self.sheet):
      if r >= y_0 and r < y_0 + board.length:
        for c, col in enumerate(row):
          if c >= x_0 and c < x_0 + board.width:
            if col != self.notCutYet:
              return False
    
    return True