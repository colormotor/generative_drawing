'''
Visualization of sin and cos along a circle
'''

from py5canvas import *

t = 0
steps = 50

def setup():
    create_canvas(512, 512)

def draw():
    global t

    background(255)

    r = 50     # radius
    cx = r + 10  # center x, y
    cy = r + 10

    stroke(0)
    no_fill()
    circle(cx, cy, r * 2)  # circle defined by diameter

    # Draw an arc displaying the angle
    fill(0, 198, 250)
    arc(cx, cy, r * 2, r * 2, 0, t)

    # draw a circle travelling along the circle
    fill(0)
    px = cx + cos(t) * r
    py = cy + sin(t) * r
    circle(px, py, 10)

    no_fill()
    # Draw cos(t) -> X
    stroke_weight(3)
    stroke(255, 0, 0)
    for i in range(steps * 2):
        point(cx + cos(t + i * TWO_PI / steps) * r, cy + r * 2 + i * 2)
    
    # with a line connecting it to the current position
    stroke_weight(1)
    line(px, py, px, cy + r * 2)

    # Draw sin(t) -> y
    stroke_weight(3)
    stroke(0, 0, 0, 50)
    for i in range(steps * 2):
        point(cx + r * 2 + i * 2, cy + r * 2 + cos(t + i * TWO_PI / steps) * r)

    stroke(0, 255, 0)
    for i in range(steps * 2):
        point(cx + r * 2 + i * 2, cy + sin(t + i * TWO_PI / steps) * r)
    
    stroke_weight(1)
    line(px, py, cx + r * 2, py)

    t -= TWO_PI / steps

run()
