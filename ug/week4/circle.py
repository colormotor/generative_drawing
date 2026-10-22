from py5canvas import *

"""EXPERIMENT:

- Change the number of points. Try very low numbers.
- Modify the code to squash and stretch the circle into an ellipical form.
- Modify the code to make a spiral
- Vary the amplitude of the circle using another sine function
- What happens if you make the inputs different for cos and sin ? Try multiplying one of the inputs by a number ?
"""

num_points = 360

def setup():
    create_canvas(500, 500)

def draw():
    background(0)
    stroke(255)
    no_fill()

    push()
    translate(width/2, height/2)

    begin_shape()

    for i in range(num_points + 1):
        input_val = i * TWO_PI / num_points
        x = cos(input_val) * 100
        y = sin(input_val) * 100

        vertex(x, y)

    end_shape()

    pop()

run()
