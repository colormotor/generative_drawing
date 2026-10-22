from py5canvas import *

def setup():
    create_canvas(500, 500)
    random_seed(10)
    background(255)
    no_fill()
    stroke(0)

    n = 50
    for i in range(n):
        angle = remap(i, 0, n, 0, 360) # Turtle uses degrees
        t = create_turtle(center)
        t.angle(angle)
        for j in range(130):
            #t.rotate(random(-20, 20))
            t.rotate(random_gaussian(0, 20))
            t.forward(3) #

    

run()
