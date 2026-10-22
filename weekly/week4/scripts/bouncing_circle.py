# THINGS TO TRY ...

# 1. make a second circle which moves at a different speed
# 2. make a third circle which moves by a different amount
# 3. make a fourth circle which starts at a different point in the cycle

from py5canvas import *

def setup():
    create_canvas(500, 500)

def draw():
    background(0)
    translate(center)
    fill(255)
    y = sin(frame_count*0.01) * 200
    circle(0, y, 10)
    
run()
