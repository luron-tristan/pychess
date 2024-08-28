from tkinter import *
from settings import *
from utils import *
from abc import ABC
# from Stockfish import Sf

class Piece():
  def __init__(self, canvas, type, position, draw_possible_destinations):
    self.color = "white" if str.upper(type) == type else "black"
    self.type = type
    self.position = position
    self.can_move = True # False if piece pinned to king or king in check
    self.piece_object = self.get_piece()
    self.is_moving = False
    self.canvas: Canvas = canvas
    self.draw_position()
    self.draw_possible_destinations = draw_possible_destinations
    self.destinations = None

  def get_piece(self):
    if str.upper(self.type) == 'K':
      return King(self.position, self.can_move)
    elif str.upper(self.type) == 'N':
      return Knight(self.position, self.can_move)
    else:
      return Pawn(self.position, self.can_move)

  def draw_position(self):
    try:
      # coordinates = [self.position[0], self.position[1]]
      # self.id = self.canvas.create_oval(
      #   int(X_INVERT[coordinates[0]]) * SQUARE,
      #   int(Y_INVERT[coordinates[1]]) * SQUARE,
      #   (int(X_INVERT[coordinates[0]]) + 1) * SQUARE,
      #   (int(Y_INVERT[coordinates[1]]) + 1) * SQUARE,
      #   fill=self.color,
      #   tag=type)
      # self.canvas.create_text(
      #   int(X_INVERT[coordinates[0]]) * SQUARE + SQUARE // 2,
      #   int(Y_INVERT[coordinates[1]]) * SQUARE + SQUARE // 2,
      #   text=self.type,
      #   font=("Consolas", 20),
      #   fill="red")
      
      photo_image = PhotoImage(file="./assets/white_king.png").zoom(50)
      my_image = self.canvas.create_image(100,100,
        image=photo_image,
        anchor=NW)

    except KeyError:
      invalid_coordinates(self.position, type)
    
    # self.canvas.tag_bind(self.id, "<Button-1>", self.select_piece)
    # self.canvas.bind('<Button-1>', self.select_piece)

  def select_piece(self, event):
    print("event", event)
    self.is_moving = not self.is_moving
    if self.is_moving:
      self.destinations = self.draw_possible_destinations(
        self.canvas,
        self.piece_object.get_possible_destinations())
      print("self.destinations", self.destinations)
    elif len(self.destinations):
      for destination in self.destinations:
        self.canvas.delete(destination)

class BasePiece(ABC):
  def __init__(self, position, can_move):
    super().__init__()
    self.position = position
    self.can_move = can_move
    # print(self.stockfish)
    

  def get_possible_destinations(self):
    if not self.can_move:
      return []
    destinations = []
    for x in XX:
      destinations.extend(
        f"{x}{y}" for y in YY
        if self.stockfish.is_move_correct(move_value=f"{self.position}{x}{y}"))
    return destinations

  # @abstractmethod
  # def move_piece(self):
  #   pass
    

class King(BasePiece):
  def __init__(self, position, can_move):
    super().__init__(position, can_move)

class Pawn(BasePiece):
  def __init__(self, position, can_move):
    super().__init__(position, can_move)


class Knight(BasePiece):
  def __init__(self, position, can_move):
    super().__init__(position, can_move)
