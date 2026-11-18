from py5canvas import *
import numpy as np

"""
TASK
- Add code to randomly reposition the particles when they go off canvas.
- Add code to change the colour of the particles based on the same or different noiseVals.
- Experiment with changing parameters such as noiseScale, octaves and falloff.
- Experiment with moving through the noise plane with incrementing values (in the flow function).
- Experiment with adding a third incrementing dimension to the noise plane (in the flow function).
"""

octaves = 8
falloff = 0.5
particles = []
noise_scale = 0.01

fast = True

def setup():
    global particles
    size(512, 512)
    noise_detail(octaves, falloff)
    for i in range(100):
        particles.append(vector(random(width), random(height)))
    # To make this faster we will use numpy arrays
    # This will be identical to a list, but will allow accessing the rows and columns directly
    particles = np.array(particles)
    
    background(0)
    draw_flow_field()

def flow(x, y):
    noise_val = noise(x * noise_scale + frame_count * 0.02, 
                      y * noise_scale,
                      0) 
    angle = remap(noise_val, 0, 1, -1, 1)*TWO_PI 
    return cos(angle), sin(angle)

# def flow(x, y):
#     x = remap(x, 0, width, -1, 1)
#     y = remap(y, 0, height, -1, 1)
#     return -y, x

def draw_flow_field():
    stroke_weight(1)
    background(0)
    stroke(255, 0, 255, 255)
    step = 10
    # Slow 
    if not fast:
        for y in range(0, height, step):
            for x in range(0, width, step):
                dx, dy = flow(x, y)
                line(x, y, x + dx * step, y + dy * step)
    else:
        # Fast with numpy
        # Create a grid of points, storing the y and x coordinates as separate arrays
        # Each resulting array has shape (num_rows, num_cols)
        ys, xs = np.mgrid[0:height:step, 0:width:step]
        dxs, dys = flow(xs, ys)
        for i in range(xs.shape[0]): # rows
            for j in range(xs.shape[1]): # cols
                x = xs[i, j]
                y = ys[i, j]
                dx = dxs[i, j]
                dy = dys[i, j]
                line(x, y, x + dx * step, y + dy * step)      

def draw():
    stroke_weight(2)
    stroke(255, 100)
    if not fast:
        for particle in particles:
            d = flow(particle[0], particle[1])
            particle += d
            point(particle)
    else:
        # Compute all particles in one go
        dxs, dys = flow(particles[:,0], particles[:,1]) 
        particles[:,0] += dxs
        particles[:,1] += dys
        # Draw particles
        for particle in particles:
            point(particle)
    
run()
