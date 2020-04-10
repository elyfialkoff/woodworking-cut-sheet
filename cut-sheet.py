from board import Board
from sheet import Sheet

def main():
  # initialPlacementTest()

  # Setup
  width, length = 12, 12
  sheet = Sheet(width, length)
  a = Board(2, 12, 'A')

  x_0 = 1
  y_0 = 0
  rotation = False
  if doesBoardFitOnSheetAt(sheet, a, x_0, y_0, rotation):
    sheet.drawBoardOnSheet(a, x_0, y_0, rotation)
    print(sheet)

def doesBoardFitOnSheetAt(sheet, board, x_0, y_0, rotation):
  """
  return True if the board fits on the sheet at the desired origin (x_0, y_0)
  does not tell you the rotation status of the fit
  """
  if rotation:
    doesBoardFit = (x_0 + board.smaller <= sheet.width) and (y_0 + board.bigger <= sheet.length)
  else:
    doesBoardFit = (x_0 + board.bigger <= sheet.width) and (y_0 + board.smaller <= sheet.length)
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

if __name__ == '__main__':
  main()