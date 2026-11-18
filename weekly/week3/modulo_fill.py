"""
Modulo can be useful to work with grid structures
- Try experimenting with different increments when filling the grid
- Try adding different colors or shades of gray when filling (use modulo)
- Try modifying the sketch so it is constantly changing
Note: to test results faster, you can put the body of the draw function inside a loop (e.g., 20/30 iterations)
"""

from py5canvas import *


cell_size = 10
nrows = 50
ncols = 50
counter = 0
pattern = 11

# most prime numbers will give us nice patterns that fill the grid in (nrows * ncols) iterations
primes = [1, 2, 3, 5, 7, 11, 13, 17, 19,
          23, 29, 31, 37, 41, 43, 47,
          53, 59, 61, 67, 71, 73, 79,
          83, 89, 97, 101, 103, 107,
          109, 113, 127, 131, 137, 139,
          149, 151, 157, 163, 167, 173,
          179, 181, 191, 193, 197, 199,
          211, 223, 227, 229, 233, 239,
          241, 251, 257, 263, 269, 271,
          277, 281, 283, 293, 307, 311,
          313, 317, 331, 337, 347, 353,
          359, 367, 373, 379, 383, 389,
          397, 401, 409, 419, 421, 431,
          433, 439, 443, 449, 457, 461,
          463, 467, 479, 487, 491, 499,
          503, 509, 521, 523, 541]

def setup():
    create_canvas(cell_size * ncols, cell_size * nrows)
    fill(0)
    background(255)

def draw():
    global counter # <- to modify a global we need to explicitly declare it
    
    for k in range(10): # We do this in a loop to increase speed
        i = (counter * primes[pattern]) % (nrows * ncols)
        counter += 1

        # Given a "flat" index we can use the modulo operator and integer division (//)
        # to recover the row and column in a grid
        x = i % ncols  # the column
        y = (i - x) // ncols  # the row
        rectangle(x * cell_size, y * cell_size, cell_size, cell_size)

# key_pressed gets called automatically if user pressed a key on the keyboard.
# k is the character that was pressed
def key_pressed(k):
    global pattern
    if k==" ":
        # if user pressed space, restart filling
        background(255)
        pattern = (pattern + 2) % len(primes)

run()