"""
TASK

- Experiment with changing frequency, noiseAmp, and the interpolation mode to change the quality of the noise wave.
"""
from py5canvas import *

frequency = 32
noise_amp = 50
interp_mode = 1  # cosine (default)
draw_nodes = True  # draw interpolation nodes

vals = []

def setup():
    size(512, 512)
    stroke(255)
    
    global vals
    # Generate a vector of random numbers
    vals = random_uniform(0, 1, frequency)
    vals[0] = 0.5
    vals[-1] = 0.5
    
    stroke_weight(2)

def draw():
    background(0)
    translate(0, height / 2)
    
    width_step = width / (len(vals) - 1)
    for i in range(len(vals) - 1):
        no_fill()
        stroke(255)
        
        x0 = (i - 1) * width_step
        x1 = i * width_step
        x2 = (i + 1) * width_step
        x3 = (i + 2) * width_step
        
        y1 = remap(vals[i], 0, 1, -noise_amp, noise_amp)
        y2 = remap(vals[i + 1], 0, 1, -noise_amp, noise_amp)
        
        # For cubic interpolation, we need 4 values
        if i == 0:
            y0 = 0
        else:
            y0 = remap(vals[i - 1], 0, 1, -noise_amp, noise_amp)
        
        if i == len(vals) - 2:
            y3 = 0
        else:
            y3 = remap(vals[i + 2], 0, 1, -noise_amp, noise_amp)
        
        subdivision = 20
        for j in range(subdivision):
            p = j / subdivision
            
            if interp_mode == 0:
                yp = linear_interpolate(y1, y2, p)
            elif interp_mode == 1:
                yp = cosine_interpolate(y1, y2, p)
            elif interp_mode == 2:
                yp = cubic_interpolate(y0, y1, y2, y3, p)
            
            xp = x1 + (x2 - x1) * p  # linearly interpolate x
            point(xp, yp)
    
    if draw_nodes:
        for i in range(len(vals)):
            y = remap(vals[i], 0, 1, -noise_amp, noise_amp)
            x = i * width / (len(vals) - 1)
            
            no_stroke()
            fill(0, 200, 100)
            circle(x, y, 4)

def linear_interpolate(a, b, p):
    return a * (1 - p) + b * p

def cosine_interpolate(a, b, p):
    ft = p * PI
    f = (1 - cos(ft)) * 0.5
    return a * (1 - f) + b * f

def cubic_interpolate(a0, a1, a2, a3, p):
    psq = p ** 2
    t0 = a3 - a2 - a0 + a1
    t1 = a0 - a1 - t0
    t2 = a2 - a0
    t3 = a1
    return t0 * p * psq + t1 * psq + t2 * p + t3

def key_pressed(key):
    global draw_nodes, interp_mode
    if key == ' ':
        draw_nodes = not draw_nodes
    elif key == 'i':
        interp_mode = (interp_mode + 1) % 3

run()