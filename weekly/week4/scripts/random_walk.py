from py5canvas import *

def setup():
    create_canvas(500, 500)
    random_seed(10)
    background(255)
    no_fill()
    stroke(0, 100)

    n = 10
    step = 10
    for i in range(n):  
        begin_shape()
        # Copy the center position
        # We need a copy otherwise we will keep modifying it at each iteration
        pos = vector(center) 
        vertex(pos) # First vertex
        for j in range(130):
            #pos += random(-step, step, 2)
            pos += random_gaussian(0, step, 2) 
            #pos += direction(random(-1, 1)*TWO_PI*0.2)*step
            vertex(pos)
        end_shape()
    

run()
