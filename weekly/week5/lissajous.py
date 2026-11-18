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

from cmath import cos, rect, sin

from py5canvas import *

steps = 50

def setup():
    create_canvas(512, 512)

def draw():
    background(0)
    translate(width/2, height/2)

    no_fill() #fill(255, 100)
    stroke(255) #, 120)
    
    n = 1000
    # delta = TWO_PI / 4
    delta = sin(seconds()*0.5) * TWO_PI
    delta = remap(seconds(), 0, 59, 0, TWO_PI) + seconds()*0.1
    delta2 = TWO_PI / 4
    a, b = 10,11.3


    # r = remap(sin(seconds()), 0, 1, 255, 0)
    # g = random(r, 255)


    # for j in range(n2):
    #     t = remap(j, 0, n, 0, TWO_PI) + seconds()*0.5
    #     x = sin(t * a + delta2)*width
    #     y = sin(t * b)*height
    #     no_stroke()
    #     fill(y, 255)
    #     circle(x, y, 10)

    for i in range(n):
        for j in letter:
         t = remap(i, 0, n, 0, TWO_PI) + seconds()*0.01
         x = sin(t * a + delta)*width*0.4
         y = cos(t * b)*height*0.5
        no_fill()
        # rectangle(x, y, 5, 50)
        # text(str(~),x, y + 30)
        text(str("#"), x, y)


# Run the sketch
run()
