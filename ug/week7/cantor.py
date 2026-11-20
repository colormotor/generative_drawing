from py5canvas import *

def setup():
    create_canvas(512, 512)
    stroke(0)
    background(255)
    stroke_weight(5)
    stroke_cap(SQUARE)
    cantor(10, 50, width - 20)

def cantor(x, y, len_val):
    # Stop at 1 pixel!
    if len_val >= 1: # 1:
        line(x, y, x + len_val, y)
        # Length of one third
        one_third = len_val / 3
        cantor(x, y + 20, one_third)
        # Complete with a second call to cantor, drawing the right segment
        cantor(x + one_third*2, y + 20, one_third)
run()
