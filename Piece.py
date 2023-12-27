from tkinter import *
from settings import *

class Piece:
  def __init__(self, canvas, type, position):
    self.color = "white" if str.upper(type) == type else "black"
    self.type = type
    self.can_move = True
    self.is_moving = False

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
      print(f"Invalid coordinates: {position[0]}{position[1]} pour la pièce {type}")
      print("Veuillez fournir des coordonnées entre a1 et h8")
    
    canvas.tag_bind(self.id, "<Button-1>", self.select_piece)

  def select_piece(self, event):
    print("You clicked on", self.type)
    print("Can move:", self.can_move)
    self.is_moving = True


class King(Piece):
  def __init__(self, canvas, position):
    super().__init__(canvas, position)
    # self.moves
