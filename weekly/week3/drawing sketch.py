from py5canvas import *

def setup():
    create_canvas(512, 512)
    background(0)

def draw():
    #background(0)
   # circle(mouse_x, mouse_y, 50)
    
    if mouse_is_pressed:
        stroke(255)
        circle(mouse_x, mouse_y, 20)

run()