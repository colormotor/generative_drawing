from py5canvas import *

"""
TASK

- Experiment with different values of falloff (0-0.5) and observe the difference.
- Experiment with different values of increment in combination with falloff. How many different types of motion can you make?
- Use a for loop to create many particles.
- Can you add an extra offset to your noise functions to make them move in a trail?
- Can you increase the offset so that the trail becomes less obvious?
"""

octaves = 4 
falloff = 0.5  # try 0 - 0.5
increment = 0.01
input_val = 0
offset = 0.65

def setup():
    global offset
    size(512, 512)
    noise_detail(octaves, falloff)
    offset = random(5, 10)
    no_stroke()
    background(0)

def draw():
    global input_val

    background(0, 10)

    n_x = noise(input_val*1)
    n_y = noise(input_val*1 + offset)  # offset y to get different noise values
    #print(n_x, n_y)
    x = remap(n_x, 0, 1, 0, width)
    y = remap(n_y, 0, 1, 0, height)
    circle(x, y, 5)

    input_val += increment

run()
