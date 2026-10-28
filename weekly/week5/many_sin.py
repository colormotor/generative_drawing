from py5canvas import *

"""
TASK
- open the console and experiment with changing the values of amplitude and frequency. Change how much input is incremented by. Observe the results and try to understand how each part of the code functions.
- adapt the code so that phase_inc controls how much of the sine function is rendered by the circles
- experiment with different values of phase_inc
"""

amplitude = 100
frequency = 1
phase_inc = 1
input_val = 0

def setup():
    create_canvas(500, 500)

def draw():
    global input_val
    background(0)
    fill(255)
    
    translate(0, height/2)  # translate the coordinate space to center it around the y origin
    
    for i in range(20):
        phase = i * phase_inc  # phase increases for each circle, controlled by phase_inc
        y_pos = sin(input_val * frequency + phase) * amplitude  # calculate the y position
        ellipse(i * width/20, y_pos, 20, 20)
    
    input_val += 0.01  # input only increments once each frame

run()