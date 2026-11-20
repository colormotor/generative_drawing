from py5canvas import *

"""
TASKS
- This tree doesn't look very natural. Use random variation to make a more natural look. NB. random_seed will help you keep the variation consistent
- Experiment with using noise to animate the trees as if they are blowing in the wind
- Render multiple tree variants to make a small forest. NB. random_seed and noise_seed will help you generate distinct trees without the need to create many variables
"""

def parameters():
    return {
        'angle': (0, -180, 180),
    }

def setup():
    create_canvas(512, 512)
    stroke(0)

def draw():
    background(255)
    translate(width/2, height * 0.75)
    branch(100, params.angle/100)

def branch(b_length, theta):
    if b_length > 5:  # when the branch gets too short stop drawing
        line(0, 0, 0, -b_length)
        translate(0, -b_length)
        
        push()
        rotate(theta)  # rotate the branch in one direction
        branch(b_length * 0.7, theta)  # recursive function call
        pop()

        push()
        rotate(-theta)  # rotate the branch in one direction
        branch(b_length * 0.7, -theta)  # recursive function call
        pop()

run()
