from tkinter import *
from Piece import Piece
from settings import *

class Board:
  def __init__(self, window):
    canvas = Canvas(window, bg="#FD9", height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
    canvas.pack()

    frame = Frame(window)
    frame.pack()

    for x in range(0, 8):
      for y in range(0, 8):
        canvas.create_rectangle(
          x * SQUARE,
          y * SQUARE,
          (x + 1) * SQUARE,
          (y + 1) * SQUARE,
          fill=self.get_square_color(x, y),
          outline="#000")
        canvas.create_text(
          (x + 1) * SQUARE - int(OFFSET),
          (y + 1) * SQUARE - int(OFFSET),
          text=self.get_square_coordinate(x, y),
          font=("consolas", 8),
          fill=self.get_text_color(x, y)
          )
    

    Piece(canvas, 'K', 'e1')
    Piece(canvas, 'k', 'e8')

  def get_square_color(self, x, y):
    return "#FD9" if (x + y) % 2 == 0 else "#530"

  def get_text_color(self, x, y):
    return "#530" if (x + y) % 2 == 0 else "#FD9"

  def get_square_coordinate(self, _x, _y):
    return f"{X[str(_x)]}{Y[str(_y)]}"
