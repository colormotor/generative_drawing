'''
TASK
- make multiple particles in an array
- try giving each one a different directional bias 
- draw the trails of each particle in a different colour
'''
from py5canvas import *

pos = Vector(0, 0)

def setup():
    create_canvas(512,512)
    no_stroke()
    background(0)

def draw():
    global pos
    translate(center)

    #pos[0] += random_gaussian()*5
    #pos[1] += random_gaussian()*5
    # or
    pos += random_gaussian(size=2)*5
    fill(255)
    circle(pos, 2)
    print(pos)

run()



