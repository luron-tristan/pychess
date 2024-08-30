from tkinter import *
from Piece import Piece
from settings import *
from utils import *
# from Stockfish import Sf
from stockfish import Stockfish

class Board:
  def __init__(self, window: Tk):
    self.canvas = Canvas(window,
                    bg="#FD9",
                    height=WINDOW_HEIGHT,
                    width=WINDOW_WIDTH,
                    )

    self.draw_board()
    
    self.stockfish = Stockfish(path=r"C:\Users\user\projets\python\pychess\stockfish\stockfish-windows-x86-64-avx2.exe")
    self.new_game()
    
  
  def draw_board(self):
    for y in range(8):
      for x in range(8):
        self.canvas.create_rectangle(
          x * SQUARE,
          y * SQUARE,
          (x + 1) * SQUARE,
          (y + 1) * SQUARE,
          fill=self.get_square_color(x, y),
          outline="#000")
        self.canvas.create_text(
          (x + 1) * SQUARE - int(OFFSET),
          (y + 1) * SQUARE - int(OFFSET),
          text=self.get_square_coordinate(x, y),
          font=("Consolas", 8),
          fill=self.get_text_color(x, y),
          tag=self.get_square_coordinate(x, y)
        )
    self.canvas.pack()
    

  def get_square_color(self, x, y):
    return "#FD9" if (x + y) % 2 == 0 else "#530"

  def get_text_color(self, x, y):
    return "#530" if (x + y) % 2 == 0 else "#FD9"

  def get_square_coordinate(self, _x, _y):
    return f"{X[_x]}{Y[_y]}"

  def new_game(self):
    fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    self.stockfish.set_fen_position(fen)
    print("Game reset")
    # Piece(self.canvas, 'k', 'e8', self.draw_possible_destinations)
    print(self.stockfish.get_board_visual())
    for y in Y:
      for x in X:
        square = f"{x}{y}"
        if piece := self.stockfish.get_what_is_on_square(square):
          Piece(self.canvas, piece, square, self.stockfish, self.draw_possible_destinations)

  def draw_possible_destinations(self, positions):
    position_list = []
    try:
      for position in positions:
        position_id = self.canvas.create_oval(
          int(X.index(position[0])) * SQUARE + SQUARE - 25,
          int(Y.index(position[1])) * SQUARE + SQUARE - 25,
          (int(X.index(position[0])) + 1) * SQUARE - SQUARE + 25,
          (int(Y.index(position[1])) + 1) * SQUARE - SQUARE + 25,
          fill="gray",
          tag="position")
        position_list.append(position_id)
    except KeyError:
      invalid_coordinates(positions, "king")
    return position_list