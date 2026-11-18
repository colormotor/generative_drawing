'''
 Modulo can be useful to do "infinite" animations
 Here we animate a series of concentric circles and use
 the modulo operator to animate just the movement between a circle and the distance to the next
 giving the illusion of a continuous movement.

 Ideas:
 - Try changing/varying shapes, stroke weights, adding colors
 - The animation is intentionally inside a function:
   - try superimposing multiple "ripples" at different positions
     - this can be done easily by using transformations and calling the ripple function multiple times
   - try varying the parameters for different ripples
 - Note that in Python the % operator will also work with non-integer values
'''


from py5canvas import *

def setup():
    create_canvas(512, 512)
    stroke(100)
    no_fill()
    # no_loop()

def ripple(x, y, step):
    t = frame_count
    stroke_weight(step / 3)
    for i in range(5, width*3, step):
        circle(x, y, i + t % step)

def draw():
    background(255,0,0)
    ripple(width / 2, height / 2, 10)
    
run()