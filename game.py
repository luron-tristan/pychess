from tkinter import Tk
from Board import Board
from settings import *

window = Tk()

def main():
  Board(window)
  window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
  window.mainloop()

if __name__ == "__main__":
  main()