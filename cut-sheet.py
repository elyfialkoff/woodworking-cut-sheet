from board import Board
from sheet import Sheet

import numpy as np

def main():
  # initialPlacementTest()

  # Test: initialSmartPlacementTest
  initialSmartPlacementTest()

  # # Setup
  # width, length = 12, 12
  # sheet = Sheet(width, length)
  # a = Board(2, 12, 'A')

  # x_0 = 0
  # y_0 = 0
  # rotation = False
  # if doesBoardFitOnSheetAt(sheet, a, x_0, y_0, rotation):
  #   sheet.drawBoardOnSheet(a, x_0, y_0, rotation)
  #   print(sheet)

def doesBoardFitOnSheetAt(sheet, board, x_0, y_0, rotation):
  """
  return True if the board fits on the sheet at the desired origin (x_0, y_0)
  does not tell you the rotation status of the fit
  """

  # I need to check if the board fits at the current location (and nothing is its in its way)
  # This currently does not work
  # Idea - take the sub matrix at x_0 to x_0 + board.smaller, and y_0 to y_0 + board.bigger and see if all items are unCut
  flatSheet = sheet.sheet[x_0:x_0+board.smaller][y_0:y_0+board.bigger].flatten()
  print(flatSheet)

  for item in flatSheet:
    if item is not sheet.notCutYet:
      return False
  # 

  if rotation:
    doesBoardFit = (x_0 + board.width <= sheet.width) and (y_0 + board.length <= sheet.length)
  else:
    doesBoardFit = (x_0 + board.length <= sheet.width) and (y_0 + board.width <= sheet.length)
  return doesBoardFit

def initialPlacementTest():
  width, length = 12, 12
  sheet = Sheet(width, length)

  a = Board(2, 12, 'A')
  b = Board(4, 8, 'B')
  c = Board(4, 8, 'C')

  cutList = list()
  cutList.append([a, 0, 0, True])
  cutList.append([b, 2, 0, True])
  cutList.append([c, 2, 8, False])

  doesBoardFitOnSheet = True
  while doesBoardFitOnSheet and cutList:
    board, x_i, y_i, rotation = cutList.pop()
    doesBoardFitOnSheet = sheet.drawBoardOnSheet(board, x_i, y_i, rotation)

  print(sheet) 

def initialSmartPlacementTest():
  """
  Take a Sheet, and a Board and place the board on the sheet by trying several options
  """
  width, length = 12, 12
  sheet = Sheet(width, length)

  a = Board(2, 8, 'A')
  x = Board(2, 4, 'X')
  y = Board(4, 4, 'Y')

  cutList = list()
  cutList.append([x, 0, 0, True])
  cutList.append([y, 4, 4, False])

  doesBoardFitOnSheet = True
  while doesBoardFitOnSheet and cutList:
    board, x_i, y_i, rotation = cutList.pop()
    doesBoardFitOnSheet = sheet.drawBoardOnSheet(board, x_i, y_i, rotation)

  for r in range(sheet.width):
    for c in range(sheet.length):
      if doesBoardFitOnSheetAt(sheet, a, r, c, True):
        sheet.drawBoardOnSheet(a, r, c, True)
        print("Row: {}, Column: {}".format(r, c))
        break

  print(sheet)

  # cutList.append([a, 0, 0, True])

if __name__ == '__main__':
  main()