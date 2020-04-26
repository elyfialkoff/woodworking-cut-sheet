from board import Board
from sheet import Sheet

import numpy as np

def main():
  # Test: initialSmartPlacementTest
  initialSmartPlacementTest()

def initialSmartPlacementTest():
  """
  Take a Sheet, and a Board and place the board on the sheet by trying several options
  """
  width, length = 10, 14
  sheet = Sheet(width, length)

  addBoardsToSheet(sheet)
  # print(sheet)

def addBoardsToSheet(sheet):
  a = Board(2, 8, 'A')
  b = Board(8, 4, 'B')
  # a.rotate()
  print(a)

  boards = list()
  boards.append(a)
  boards.append(b)

  X = Board(2, 4, 'X')
  Y = Board(4, 6, 'Y')

  cutList = list()
  cutList.append([X, 0, 0])
  cutList.append([Y, 4, 0])

  doesBoardFitOnSheet = True
  while doesBoardFitOnSheet and cutList:
    board, x_i, y_i = cutList.pop()
    doesBoardFitOnSheet = sheet.drawBoardOnSheet(board, x_i, y_i)

  origins = list()
  for board in boards:
    origins.append(findAndDraw(sheet, board))

  # Demonstrate removing a board from a sheet
  x, y = origins[0]
  board = boards[0]

  print(sheet)
  sheet.removeBoardFromSheet(board, x, y)
  print(sheet)

def findAndDraw(sheet, board):
  for y in range(sheet.length):
    for x in range(sheet.width):
      fit = sheet.doesBoardFitOnSheetAt(board, x, y)
      print("Does the board fit at ({}, {})? {}".format(x, y, fit))
      if fit:
        sheet.drawBoardOnSheet(board, x, y)
        return [x, y]

if __name__ == '__main__':
  main()