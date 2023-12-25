from tkinter import Canvas
from settings import *

class Piece:
  def __init__(self, canvas, type, position):
    self.color = "white" if str.upper(type) == type else "black"

    try:
      self.coordinates = [position[0], position[1]]
      canvas.create_oval(
        int(X_INVERT[self.coordinates[0]]) * SQUARE,
        int(Y_INVERT[self.coordinates[1]]) * SQUARE,
        (int(X_INVERT[self.coordinates[0]]) + 1) * SQUARE,
        (int(Y_INVERT[self.coordinates[1]]) + 1) * SQUARE,
        fill=self.color,
        tag=type)
    except KeyError:
      print(f"Invalid coordinates: {position[0]}{position[1]} pour la pièce {type}")
      print("Veuillez fournir des coordonnées entre a1 et h8")
