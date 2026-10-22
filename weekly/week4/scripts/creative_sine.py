from py5canvas import *

"""
TASK
  - here we are drawing several sinewaves together. 
  - Can you find ways to increment frequencies, amplitudes and phases to create more interesting effects ?
"""

amplitude = 100
frequency = 0.05

def setup():
    create_canvas(500, 500)

def draw():
    background(255)
    no_fill()
    stroke(0)
    
    translate(0, height/2)  # translate the coordinate space to center it around the y origin
    
    for j in range(5):
        begin_shape()
        for i in range(width):
            input_val = i
            phase = 0.0
            y_pos = sin(input_val * frequency + phase) * amplitude
            vertex(i, y_pos - j * 20)
        end_shape()

run()
