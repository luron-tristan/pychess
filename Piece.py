from tkinter import *
from settings import *
from utils import *
from abc import ABC, abstractmethod

class Piece:
  def __init__(self, canvas, type, position, draw_possible_destinations):
    self.color = "white" if str.upper(type) == type else "black"
    self.type = type
    self.position = position
    self.can_move = True # False if piece pinned to king or king in check
    self.piece_object = self.get_piece()
    self.is_moving = False
    self.canvas = canvas
    self.draw_position()
    self.draw_possible_destinations = draw_possible_destinations
    self.destinations = None

  def get_piece(self):
    if str.upper(self.type) == 'K':
      return King(self.position, self.can_move)
    else:
      return Pon(self.position, self.can_move)

  def draw_position(self):
    try:
      coordinates = [self.position[0], self.position[1]]
      self.id = self.canvas.create_oval(
        int(X_INVERT[coordinates[0]]) * SQUARE,
        int(Y_INVERT[coordinates[1]]) * SQUARE,
        (int(X_INVERT[coordinates[0]]) + 1) * SQUARE,
        (int(Y_INVERT[coordinates[1]]) + 1) * SQUARE,
        fill=self.color,
        tag=type)
      self.canvas.create_text(
        int(X_INVERT[coordinates[0]]) * SQUARE + SQUARE // 2,
        int(Y_INVERT[coordinates[1]]) * SQUARE + SQUARE // 2,
        text=self.type,
        font=("Consolas", 20),
        fill="red")

    except KeyError:
      invalid_coordinates(self.position, type)
    
    self.canvas.tag_bind(self.id, "<Button-1>", self.select_piece)
    # self.canvas.bind('<Button-1>', self.select_piece)

  def select_piece(self, event):
    print("event", event)
    self.is_moving = not self.is_moving
    if self.is_moving:
      self.destinations = self.draw_possible_destinations(
        self.canvas,
        self.piece_object.get_possible_destinations())
      print("self.destinations", self.destinations)
    else:
      if len(self.destinations):
        for destination in self.destinations:
          self.canvas.delete(destination)

class BasePiece(ABC):
  def __init__(self, position, can_move):
    self.position = position
    self.can_move = can_move
    
  @abstractmethod
  def get_possible_destinations(self):
    # 2 solutions:
    # - pass all moves to stockfish and let it decide if move is valid
    # - have a set of moves per piece type
    pass
    

class King(BasePiece):
  def __init__(self, position, can_move):
    super().__init__(position, can_move)

  def get_possible_destinations(self):
    if not self.can_move:
      return []

    current_x = XX.index(self.position[0])
    destination_x = [XX[current_x]]
    if current_x - 1 >= 0:
      destination_x.append(XX[current_x - 1])
    if current_x + 1 <= 7:
      destination_x.append(XX[current_x + 1])

    current_y = YY.index(self.position[1])
    destination_y = [YY[current_y]]
    if current_y - 1 >= 0:
      destination_y.append(YY[current_y - 1])
    if current_y + 1 <= 7:
      destination_y.append(YY[current_y + 1])

    print("x:", destination_x)
    print("y:", destination_y)
    destinations = []
    for i in destination_x:
      for j in destination_y:
        # check if square attacked by enemy piece
        if f"{i}{j}" != self.position:
          destinations.append(f"{i}{j}")
    
    return destinations

class Pon(BasePiece):
  def __init__(self, position, can_move):
    super().__init__(position, can_move)
    
  def get_possible_destinations(self):
    print("pon pos >", self.position)
    return ("c3", "c4")
