from tkinter import Tk
from Board import Board
from settings import WINDOW_WIDTH, WINDOW_HEIGHT

window = Tk()

def main():
  Board(window)
  window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
  window.mainloop()

if __name__ == "__main__":
  main()

# Sf useless for now
# next moves:
# - draw pieces on the board
# - move pieces with stockfish