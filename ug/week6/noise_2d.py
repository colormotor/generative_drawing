from py5canvas import *

"""
TASK 
- Try adjusting pixel_scale and noise_scale to understand what they do.
- Try animating the noise like you did with 1D noise.
- Try moving in different directions across the noise plane.
- Experiment with different ways for rendering the noise pattern.
"""

octaves = 2
falloff = 0.5
noise_scale = 0.01
pixel_scale = 5

def setup():
    size(340, 340)
    no_stroke()
    noise_detail(octaves, falloff)

def draw():
    background(0)
    # Create two arrays for x and y coordinates
    x = np.linspace(0, width, width // pixel_scale)
    y = np.linspace(0, height, height // pixel_scale)
    # Compute 2d noise values for the grid of points
    # The resulting array has shape (num_rows, num_cols)
    noise_vals = noise_grid(x * noise_scale,
                            y * noise_scale)
    

    num_cols = noise_vals.shape[1] 
    num_rows = noise_vals.shape[0]
    w = width / num_cols
    h = height / num_rows

    for i in range(num_rows):
        for j in range(num_cols):
            fill(noise_vals[i,j] * 255)
            rect(j * w, i * h, w, h)

run()
