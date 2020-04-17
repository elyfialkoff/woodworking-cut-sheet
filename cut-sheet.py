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

# def doesBoardFitOnSheetAt(sheet, board, x_0, y_0, rotation):
#   """
#   return True if the board fits on the sheet at the desired origin (x_0, y_0)
#   does not tell you the rotation status of the fit
#   """

#   # Check to current placement of the board to determine if it will fit withint the sheets bounderies. 
#   if rotation:
#     doesBoardFit = (x_0 + board.width <= sheet.width) and (y_0 + board.length <= sheet.length)
#   else:
#     doesBoardFit = (x_0 + board.length <= sheet.width) and (y_0 + board.width <= sheet.length)

#   if not doesBoardFit:
#     return doesBoardFit

#   # Check the current placement of the board to determine if it will have any conflicts. 
#   for r, row in enumerate(sheet.sheet):
#     if r >= x_0 and r <= x_0 + board.width:
#       for c, col in enumerate(row):
#         if c >= y_0 and c <= y_0 + board.length:
#           if col != sheet.notCutYet:
#             print("Row: {}, Col: {}, Value: {}".format(r+1, c+1, col))
#             return False

#   return doesBoardFit

def initialPlacementTest():
  width, length = 12, 12
  sheet = Sheet(width, length)

  a = Board(2, 8, 'A')
  b = Board(4, 8, 'B')
  c = Board(4, 8, 'C')

  cutList = list()
  cutList.append([a, 0, 0])
  cutList.append([b, 2, 0])
  cutList.append([c, 2, 8])

  doesBoardFitOnSheet = True
  while doesBoardFitOnSheet and cutList:
    board, x_i, y_i, rotation = cutList.pop()
    doesBoardFitOnSheet = sheet.drawBoardOnSheet(board, x_i, y_i)

  print(sheet) 

def initialSmartPlacementTest():
  """
  Take a Sheet, and a Board and place the board on the sheet by trying several options
  """
  width, length = 10, 14
  sheet = Sheet(width, length)

  addBoardsToSheet(sheet)
  print(sheet)

def addBoardsToSheet(sheet):
  a = Board(2, 8, 'A')
  a.rotate()
  print(a)
  x = Board(2, 4, 'X')
  y = Board(4, 6, 'Y')

  cutList = list()
  cutList.append([x, 0, 0])
  cutList.append([y, 4, 4])

  doesBoardFitOnSheet = True
  while doesBoardFitOnSheet and cutList:
    board, x_i, y_i = cutList.pop()
    doesBoardFitOnSheet = sheet.drawBoardOnSheet(board, x_i, y_i)

  print(sheet.doesBoardFitOnSheetAt(a, 2, 0))
  sheet.drawBoardOnSheet(a, 2, 0)

  # for r in range(sheet.width):
  #   for c in range(sheet.length):
  #     if sheet.doesBoardFitOnSheetAt(a, r, c):
  #       sheet.drawBoardOnSheet(a, r, c)
  #       return

  return

if __name__ == '__main__':
  main()