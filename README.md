# woodworking-cut-sheet
This project will help you layout your cut list from a base board. 

This program is meant for dividing a sheet of plywood (of any size) into portions based on whatever size boards you have. 

Termonology:
sheet: this is the plywood sheet that you are attempting to cut up
board: this is the sizes of wood you want to cut the plywood into

rotation: a board can be oriented width/length (default: rotation = False) where width is along the X-axis and length is along the y-axis
          if rotation is set to True then we swap the width and length values

          (a sheet cannot be rotated)

width: is right/left on the x-axis and comes first in declerations
length: is up/down on the y-axis and comes second in declerations
  hint: when writing double for loops, write the length and then inside write the width

claimed: a portion of the sheet is claimed when a board is cut from the sheet