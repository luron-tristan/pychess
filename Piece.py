from tkinter import *
from settings import *
from utils import *

class Piece:
  def __init__(self, canvas, type, position, draw_possible_destinations):
    self.color = "white" if str.upper(type) == type else "black"
    self.type = type
    self.can_move = True
    self.is_moving = False
    self.canvas = canvas
    self.draw_possible_destinations = draw_possible_destinations
    # self.possible_destinations = ()

    try:
      self.coordinates = [position[0], position[1]]
      self.id = canvas.create_oval(
        int(X_INVERT[self.coordinates[0]]) * SQUARE,
        int(Y_INVERT[self.coordinates[1]]) * SQUARE,
        (int(X_INVERT[self.coordinates[0]]) + 1) * SQUARE,
        (int(Y_INVERT[self.coordinates[1]]) + 1) * SQUARE,
        fill=self.color,
        tag=type)

    except KeyError:
      invalid_coordinates(position, type)
    
    canvas.tag_bind(self.id, "<Button-1>", self.select_piece)

  def select_piece(self, event):
    print("You clicked on", self.type)
    print("Can move:", self.can_move)
    self.is_moving = not self.is_moving
    if self.is_moving:
      self.draw_possible_destinations(self.canvas, ("d1", "e2", "f1"))


class King(Piece):
  def __init__(self, canvas, position):
    super().__init__(canvas, position)
    # self.moves
