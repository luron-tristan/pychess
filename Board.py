from tkinter import *
from Piece import Piece
from settings import *
from utils import *
from stockfish import Stockfish

stockfish = Stockfish(path="C:/Users/user/Downloads/stockfish/stockfish/stockfish-windows-x86-64-avx2")

class Board:
  def __init__(self, window):
    canvas = Canvas(window, bg="#FD9", height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
    canvas.pack()

    frame = Frame(window)
    frame.pack()

    self.draw_board(canvas)
    self.new_game(canvas)
  
  def draw_board(self, canvas):
    for y in range(8):
      for x in range(8):
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
          font=("Consolas", 8),
          fill=self.get_text_color(x, y),
          tag=self.get_square_coordinate(x, y)
        )
    

  def get_square_color(self, x, y):
    return "#FD9" if (x + y) % 2 == 0 else "#530"

  def get_text_color(self, x, y):
    return "#530" if (x + y) % 2 == 0 else "#FD9"

  def get_square_coordinate(self, _x, _y):
    return f"{X[str(_x)]}{Y[str(_y)]}"

  def new_game(self, canvas):
    Piece(canvas, 'K', 'e1', self.draw_possible_destinations)
    Piece(canvas, 'k', 'e8', self.draw_possible_destinations)
    Piece(canvas, '', 'c2', self.draw_possible_destinations)

  def draw_possible_destinations(self, canvas, positions):
    position_list = []
    try:
      for position in positions:
        position_id = canvas.create_oval(
          int(X_INVERT[position[0]]) * SQUARE + SQUARE - 25,
          int(Y_INVERT[position[1]]) * SQUARE + SQUARE - 25,
          (int(X_INVERT[position[0]]) + 1) * SQUARE - SQUARE + 25,
          (int(Y_INVERT[position[1]]) + 1) * SQUARE - SQUARE + 25,
          fill="brown",
          tag="position")
        position_list.append(position_id)
    except KeyError:
      invalid_coordinates(positions, "king")
    return position_list