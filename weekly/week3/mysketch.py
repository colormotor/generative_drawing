from py5canvas import *

def setup():
    create_canvas(500, 500)

    
def draw():
    for x in range(10):
        for y in range(100):
            diameter = (x+y)%5 # Addition
            no_fill()
            rectangle(y/(x+0.3), x, diameter/10, diameter*200)
            circle(y *10, x*(-100), diameter*2)

run()