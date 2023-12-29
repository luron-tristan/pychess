from tkinter import *
from settings import *
from utils import *

class Piece:
  def __init__(self, canvas, type, position, draw_possible_destinations):
    self.color = "white" if str.upper(type) == type else "black"
    self.type = type
    self.position = position
    self.can_move = True
    self.is_moving = False
    self.canvas = canvas
    self.draw_position(canvas)
    self.draw_possible_destinations = draw_possible_destinations
    self.destinations = None
    # self.possible_destinations = ()



  def draw_position(self, canvas):
    try:
      self.coordinates = [self.position[0], self.position[1]]
      self.id = canvas.create_oval(
        int(X_INVERT[self.coordinates[0]]) * SQUARE,
        int(Y_INVERT[self.coordinates[1]]) * SQUARE,
        (int(X_INVERT[self.coordinates[0]]) + 1) * SQUARE,
        (int(Y_INVERT[self.coordinates[1]]) + 1) * SQUARE,
        fill=self.color,
        tag=type)

    except KeyError:
      invalid_coordinates(self.position, type)
    
    canvas.tag_bind(self.id, "<Button-1>", self.select_piece)

  def select_piece(self, event):
    self.is_moving = not self.is_moving
    print("type", self.type)
    print("self.is_moving", self.is_moving)
    if self.is_moving:
      print("Can move:", self.can_move)
      print("self.position", self.position)
      self.destinations = self.draw_possible_destinations(self.canvas, ("d1", "e2", "f1"))
      print("self.destinations", self.destinations)
    else:
      print("unselect")
      if len(self.destinations):
        print("len", len(self.destinations))
        for dest in self.destinations:
          self.canvas.delete(dest)


class King(Piece):
  def __init__(self, canvas, position):
    super().__init__(canvas, position)
    # self.moves
