'''Simple example of using lerp to smooth out mouse motion'''
from py5canvas import *

def setup():
    global pos
    create_canvas(400, 400)
    # Store initial mouse position
    pos = mouse_pos

def draw():
    global pos
    background(255, 40)
    # new position is 
    pos = pos + (mouse_pos - pos)*0.1
    # Same thing as:
    #pos = lerp(pos, mouse_pos, 0.1)
    circle(pos, 10)

run()