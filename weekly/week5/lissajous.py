'''
  Lissajous curve:
  https://en.wikipedia.org/wiki/Lissajous_curve
  http://paulbourke.net/geometry/harmonograph/
  - Try different parameters as show in the Wikipedia page
  - Try to animate the curve (use frame_count)
  - Experiment with modulation
  - Draw a curve replacing the circles with `begin_shape()` and `end_shape(CLOSE)` and `vertex` in the loop
  - Try to adapt ideas from the harmonograph article to the sketch
'''

from py5canvas import *

steps = 50

def setup():
    create_canvas(512, 512)

def draw():
    background(0)
    translate(width/2, height/2)

    no_fill() #fill(255, 100)
    stroke(255) #, 120)
    
    n = 300
    delta = TWO_PI / 4
    a, b = 1.0, 4.0

    for i in range(n):
        t = remap(i, 0, n, 0, TWO_PI) + seconds()*0.1
        x = sin(t * a + delta)*width*0.5
        y = sin(t * b)*height*0.5
        circle(x, y, 10)

# Run the sketch
run()
