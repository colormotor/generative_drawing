'''
TASK
- use begin_shape and end_shape to join the dots to make a circle. (HINT curve_vertex will make a smoother shape)
- make each point on the circle randomly walk so that it gradually deforms
- experiment with removing the ellipses and change the background refresh to build up static images of the deformation
- experiment with adding motion in a fixed direction to the points so that the pattern can be seen more clearly
- experiment with adding biases to random walks to create different effects
'''
from py5canvas import *

positions = []
num_points = 10

def setup():
    create_canvas(512, 512)

    # initialize_positions_on_circle
    for i in range(num_points):
        t = i * TWO_PI / num_points
        pos = vector(sin(t), cos(t))
        pos *= 100  # scale the vector to a radius of 100
        positions.append(pos)

def draw():
    background(0)
    fill(255)
    
    translate(width / 2, height / 2)
    
    # draw_circles_at_each_position
    for pos in positions:
        ellipse(pos, 10, 10)

run()