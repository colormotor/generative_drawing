'''
  Additive synthesis and standing waves (https://en.wikipedia.org/wiki/Standing_wave)
  - Try modifying `a` to positive integer values and observe the effect
  - Try adding more sine waves
'''

from py5canvas import *

num_frames = 150

def setup():
    create_canvas(512, 512)
    background(0)
    num_movie_frames(num_frames) 

def draw():
    background(0)
    fill(255)
    stroke(255)
    
    t = (frame_count/num_frames) * TWO_PI #0.01
    a = 2
    
    freq = 2 * TWO_PI / width

    # Create a loop over x that increments by 2 each iteration
    for x in range(0, width, 2):
        y = sin(x * freq + t) + sin(x * freq * a - t)
        circle(x, y * 100 + height / 2, 5)
    
    no_stroke()

    # Uncomment to visualize the "nodes" when `a` is an integer
    # Nodes are stationary points along the wave
    fill(255, 0, 0)
    for i in arange(0, width, width / (a * 2 + 2)):
        circle(i, height / 2, 7)

# Run the sketch
run()
