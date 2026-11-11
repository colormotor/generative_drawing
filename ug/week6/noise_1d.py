"""
TASK
- Experiment with changing the size of noiseStep. What happens when it increases and decreases ?
- Draw the noise across the screen as a continuous line using begin_shape, end_shape and vertex
- Increment the noise input to make the noise scroll across the screen
- Imagine this is a mountain range. Use noise several times to make multiple overlaid mountain ranges. How do you make sure that each mountain range is different
- Scroll through each mountain range at a different speed to make a parallax effect

For later ....
- Experiment with changing num_octaves and falloff - observe the different effects
- Compare this with changing the noise_step. How do the effects differ ?
"""
from py5canvas import *

noise_step = 0.02
noise_amp = 50

def setup():
    size(512, 512)
    stroke(255)
    no_stroke()
    fill(255)
    noise_detail(2, 0.5) # Number of octaves and falloff
    
def draw():
    background(0, 5)
    n = noise(mouse_x * 0.05)
    y = remap(n, 0, 1, -noise_amp, noise_amp)
    translate(0, height / 2)
    circle(mouse_x, y, 5)

run()