from board import Board
from sheet import Sheet

import numpy as np

def main():
  """
  Create a Sheet
  Create a list of Boards

  findCutList
  """
  pass

def findCutList():
  """
  initial test findCutListWithLargestBoardsFirst
  """
  pass

def findCutListWithLargestBoardsFirst():
  """
  Sort Boards for biggest to smallest (by area or width/length?)
  For each Board in Boards
    For row, col in Sheet
    Try and drawBoardOnSheet 
    If doesn't fit, Board.rotate() and try again
    If still not fit continue (row, col)
    If fit then return and move onto next Board
  """
  pass

if __name__ == '__main__':
  main()