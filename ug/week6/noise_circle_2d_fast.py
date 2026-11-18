from py5canvas import *

"""
This version uses numpy arrays to significantly speed up noise computation
"""

noise_step = 0.3


def setup():
    size(512, 512)
    no_fill()
    stroke(255)
    noise_detail(8)


def draw():
    background(0)
    translate(width / 2, height / 2)
    n = 50
    for i in range(35):  # Create multiple concentric circles
        # Create an array of angles from 0 to TWO_PI (not including the endpoint TWO_PI)
        theta = np.linspace(0, TWO_PI, n, endpoint=False)
        # Compute 2D noise values for all angles at once
        noise_val = noise(
            np.cos(theta) * noise_step + i * 0.01,
            np.sin(theta) * noise_step + i * 0.02,
        )
        # Remap noise values to radius
        r = remap(noise_val, 0, 1, 0, 3 + i * 10)
        # Draw the polygon using the computed radii
        curve(np.cos(theta) * r, np.sin(theta) * r, close=True)


run()
