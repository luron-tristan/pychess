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
    self.piece_object = self.get_piece()
    self.selected = False
    self.canvas: Canvas = canvas
    self.draw_position()
    self.draw_possible_destinations = draw_possible_destinations
    self.destinations = []
  
  selected_piece = None

  def get_piece(self):
    color = "WHITE" if "WHITE" in str(self.type) else "BLACK"
    return BasePiece(self.type, self.position, color, self.stockfish)

  def draw_position(self):
    _X = self.position[0]
    _Y = self.position[1]
    try:
      self.photo_image = PhotoImage(file=r"C:\Users\user\projets\python\pychess\assets\white_king.png").zoom(3)
      self.id = self.canvas.create_image(int(X.index(_X)) * SQUARE + SQUARE // 10,
        int(Y.index(_Y)) * SQUARE + SQUARE // 10,
        image=self.photo_image,
        anchor=NW
        )

    except KeyError:
      invalid_coordinates(self.position, type)
    
    self.canvas.tag_bind(self.id, "<Button-1>", self.select_piece)
    # self.canvas.bind('<Button-1>', self.select_piece)

  def select_piece(self, event):
    if Piece.selected_piece and Piece.selected_piece != self:
      Piece.selected_piece.deselect()

    self.selected = not self.selected
    if self.selected:
      Piece.selected_piece = self
      self.destinations = self.draw_possible_destinations(
        self.piece_object.get_possible_destinations())
      print("self.destinations", self.destinations)
    elif len(self.destinations):
      Piece.selected_piece = None
      for destination in self.destinations:
        self.canvas.delete(destination)

  def deselect(self):
    self.selected = False
    self.clear_destinations()
  
  def clear_destinations(self):
    if self.destinations:
      for destination in self.destinations:
        self.canvas.delete(destination)
      self.destinations = []


class BasePiece():
  def __init__(self, type, position, color, stockfish):
    super().__init__()
    self.color = color
    self.type = type
    self.position = position
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

  def get_possible_destinations(self):
    print(self.type)
    destinations = []
    for x in X:
      destinations.extend(
        f"{x}{y}" for y in Y
        if self.stockfish.is_move_correct(move_value=f"{self.position}{x}{y}"))
    return destinations
