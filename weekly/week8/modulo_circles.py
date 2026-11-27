'''
 Modulo can be useful to do "infinite" animations
 Here we animate a series of concentric circles and use
 the modulo operator to animate just the movement between a circle and the distance to the next
 giving the illusion of a continuous movement.

 Ideas:
 - Try changing/varying shapes, stroke weights, adding colors
 - The animation is intentionally inside a funtion:
   - try superimposing multiple "ripples" at different positions
   - try varying the parameters for different ripples
 - Note that in Python the % operator will also work with non-integer values
'''


from py5canvas import *

step = 60

def setup():
    create_canvas(512, 512)
    stroke(10)
    no_fill()
    num_movie_frames(step)

def ripple(x, y, step):
    t = frame_count
    stroke_weight(step / 3)
    for i in range(width):
        circle(x, y, i*step + t % step)

def draw():
    background(255)
    ripple(width / 2, height / 2, step)
    # Try adding ripples 
    ripple(width / 2 + 100, height / 2 + 10, step)

run()