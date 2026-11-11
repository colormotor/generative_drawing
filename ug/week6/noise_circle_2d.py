from py5canvas import *

"""
TASK
- Annoyingly the circle doesn't close properly. Can you explain why?
- There's a solution to this problem using 2D noise. Can you work out what it is?
- Have a go at implementing it.
- Use a for loop to create concentric circles (like a tree trunk).
- Can you change the parameters to make these varied as the circles move outwards?
"""

noise_step = 0.01


def setup():
    size(512, 512)
    no_fill()
    stroke(255)
    noise_detail(2)

    background(0)
    translate(width / 2, height / 2)
    n = 200
    for i in range(5):  # Create multiple concentric circles
        begin_shape()
        for j in range(n):
            theta = remap(j, 0, n, 0, TWO_PI)
            noise_val = noise(theta * noise_step * 70)
            # How would you use 2D noise here to remove the "kink" from the circle?
            r = remap(noise_val, 0, 1, 100, 200)
            x = sin(theta) * r
            y = cos(theta) * r
            vertex(x, y)
        end_shape(CLOSE)


run()
