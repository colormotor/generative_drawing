from py5canvas import *

def setup():
    create_canvas(600, 400)
    noise_detail(2)

def draw():
    background(255)
    translate(0, height/2)
    no_fill()
    phase = 0

    nodes = 5
    n = 200
    amplitude = 200
    begin_shape()
    for i in range(n):
        x = remap(i, 0, n-1, 0, width)
        input = remap(i, 0, n-1, 0, nodes)
        y = remap(noise(input + phase), 0, 1, -amplitude, amplitude)
        vertex(x, y)
    end_shape()

    # Draw the zero 
    stroke(255, 0, 0, 128)
    line(0, 0, width, 0)
    for i in range(nodes):
        x = remap(i, 0, nodes, 0, width)
        circle(x, 0, 4)
    stroke(0)
    
run()