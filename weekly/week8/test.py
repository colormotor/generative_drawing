from py5canvas import *

def setup():
    create_canvas(400, 400)  

def draw():
    background(0)
    translate(center)
    theta = radians(frame_count)
    circle(sin(theta)*150, 0, 30)

run()