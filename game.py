from tkinter import *

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
SQUARE = 70
OFFSET = SQUARE / 8

X = {
  0: 'a',
  1: 'b',
  2: 'c',
  3: 'd',
  4: 'e',
  5: 'f',
  6: 'g',
  7: 'h'
}

Y = {
  0: '1',
  1: '2',
  2: '3',
  3: '4',
  4: '5',
  5: '6',
  6: '7',
  7: '8'
}


window = Tk()

def get_square_color(x, y):
  return "#FD9" if (x + y) % 2 == 0 else "#530"

def get_text_color(x, y):
  return "#000" if (x + y) % 2 == 0 else "#FFF"

def get_square_coordinate(_x, _y):
  return f"{X[_x]}{Y[_y]}"

def main():
  canvas = Canvas(window, bg="#fff", height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
  canvas.pack()

  for x in range(0, 8):
    for y in range(0, 8):
      canvas.create_rectangle(
        x * SQUARE,
        y * SQUARE,
        x * SQUARE + SQUARE,
        y * SQUARE + SQUARE,
        fill=get_square_color(x, y),
        outline="#000")
      canvas.create_text(
        x * SQUARE + SQUARE - int(OFFSET),
        y * SQUARE + SQUARE - int(OFFSET),
        text=get_square_coordinate(x, y),
        font=("consolas", 8),
        fill=get_text_color(x, y)
        )

  window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
  window.mainloop()

if __name__ == "__main__":
  main()