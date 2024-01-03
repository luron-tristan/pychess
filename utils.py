from stockfish import Stockfish
from abc import ABC

class Sf(ABC):
  def __init__(self):
    self.stockfish = Stockfish(path="C:/Users/user/Downloads/stockfish/stockfish/stockfish-windows-x86-64-avx2")

def invalid_coordinates(position, type):
  print(f"Invalid coordinates: {position[0]}{position[1]} pour la pièce {type}")
  print("Veuillez fournir des coordonnées entre a1 et h8")
