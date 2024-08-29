from tkinter import *
from settings import *
from utils import *
from abc import ABC
# from Stockfish import Sf

class Piece():
  def __init__(self, canvas, type, position, stockfish, draw_possible_destinations):
    self.type = type
    self.position = position
    self.stockfish = stockfish
    self.can_move = True # False if piece pinned to king or king in check
    self.piece_object = self.get_piece()
    self.is_moving = False
    self.canvas: Canvas = canvas
    self.draw_position()
    self.draw_possible_destinations = draw_possible_destinations
    self.destinations = None

  def get_piece(self):
    color = "WHITE" if "WHITE" in str(self.type) else "BLACK"
    return BasePiece(self.type, color, self.stockfish)

  def draw_position(self):
    _X = self.position[0]
    _Y = self.position[1]
    try:
      self.id = self.canvas.create_oval(
        int(X.index(_X)) * SQUARE + SQUARE // 10,
        int(Y.index(_Y)) * SQUARE + SQUARE // 10,
        (int(X.index(_X)) + 1) * SQUARE - SQUARE // 10,
        (int(Y.index(_Y)) + 1) * SQUARE - SQUARE // 10,
        fill=self.piece_object.color,
        tag=type)
      self.canvas.create_text(
        int(X.index(_X)) * SQUARE + SQUARE // 2,
        int(Y.index(_Y)) * SQUARE + SQUARE // 2,
        text=self.piece_object.symbol,
        font=("Consolas", 20),
        fill="red")
      
      self.photo_image = PhotoImage(file=r"C:\Users\user\projets\python\pychess\white_king.png").zoom(2)
      self.canvas.create_image(int(X.index(_X)) * SQUARE + SQUARE // 10,
        int(Y.index(_Y)) * SQUARE + SQUARE // 10,
        image=self.photo_image,
        anchor=NW
        )

    except KeyError:
      invalid_coordinates(self.position, type)
    
    # self.canvas.tag_bind(self.id, "<Button-1>", self.select_piece)
    # self.canvas.bind('<Button-1>', self.select_piece)

  # def select_piece(self, event):
  #   print("event", event)
  #   self.is_moving = not self.is_moving
  #   if self.is_moving:
  #     self.destinations = self.draw_possible_destinations(
  #       self.canvas,
  #       self.piece_object.get_possible_destinations())
  #     print("self.destinations", self.destinations)
  #   elif len(self.destinations):
  #     for destination in self.destinations:
  #       self.canvas.delete(destination)

class BasePiece():
  def __init__(self, type, color, stockfish):
    super().__init__()
    self.color = color
    self.type = type
    self.stockfish = stockfish
    self.symbol = self.get_symbol()

  def get_symbol(self):
    symbol = None
    if "KING" in str(self.type):
      symbol = "k"
    elif "QUEEN" in str(self.type):
      symbol = "q"
    elif "ROOK" in str(self.type):
      symbol = "r"
    elif "BISHOP" in str(self.type):
      symbol = "b"
    elif "KNIGHT" in str(self.type):
      symbol = "n"
    else:
      symbol = "p"
    
    return str.upper(symbol) if self.color == "WHITE" else symbol

  # def get_possible_destinations(self):
  #   if not self.can_move:
  #     return []
  #   destinations = []
  #   for x in XX:
  #     destinations.extend(
  #       f"{x}{y}" for y in YY
  #       if self.stockfish.is_move_correct(move_value=f"{self.position}{x}{y}"))
  #   return destinations

  # @abstractmethod
  # def move_piece(self):
  #   pass
