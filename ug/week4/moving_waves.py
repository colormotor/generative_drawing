from py5canvas import *

"""
TASK
  - Here we have arranged things slightly differently. Can you describe the difference from the previous sketch ?
  - Try changing the values for amplitude and frequency to understand what they are doing
"""

amplitude = 100
frequency = 0.1
phase = 0

def setup():
    create_canvas(500, 500)

def draw():
    global phase
    background(255)
    no_fill()
    stroke(0)
    
    translate(0, height/2)  # translate the coordinate space to center it around the y origin
    
    begin_shape()
    for i in range(width):
        input_val = i
        y_pos = sin(input_val * frequency + phase) * amplitude
        vertex(i, y_pos)
    end_shape()
    
    phase += 0.1

run()
