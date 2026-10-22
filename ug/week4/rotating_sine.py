  
'''
EXPERIMENT ...
- Try changing phase_inc to different values and observe the different effects
- Try values of PI, TWO_PI, PI/2 ... what is special about these values ?
- Why do they result in the different effects ?
'''
from py5canvas import *

num_circles = 40
amplitude = 100
phase_inc = 1

def setup():
    create_canvas(400,400)

def draw():  
    background(0)
    fill(255)

    translate(center) # Move origin to center of canvas

    input = frame_count * 0.01
        
    for i in range(num_circles):
        phase = i * phase_inc
        x = sin(input + phase) * amplitude;
        # spread the circles evenly across the y axis of screen
        y = -height/2  + (i + 1) * height/num_circles
        circle(x, y, 5)

run()