'''
- Experiment with different combinations of sin and cos 
  inside the `wave` function. 
    - Try addition of sine and cosine waves (additive synthesis)
        - e.g. return cos(t) + cos(t*4)*0.5
    - Try amplitude modulation 
        - e.g. return sin(t)*cos(t)
    - Try frequency modulation
        - e.g. return sin(t*(1 + sin(t*2)))

- Try animating the wave, by using the phase variable 
    - HINT: use frame_count multiplied by a small number (< 1)

- Try shifting the origin to the left 
  by setting the first parameter of translate to a number less than zero 
  - e.g translate(-30, height/2)

- Try modifying also the circle radii with a wave function (the same or a new one)

- Replace the `circle` command with another transformed shape.
  Control scale/rotation based on a wave function 
    - You can do something like this:
    push()
    translate(x, y)
    rotate(wave(t*freq*0.5 + phase)*2)
    scale(1)
    square(0, 0, 40)
    pop()

    - To draw a square/rectangle from the center use
    rect_mode('center')

- Once you are comfortable with `noise` use that too
'''

from py5canvas import *

def wave(t):
    return sin(t)
    
def setup():
    create_canvas(600, 400)

def draw():
    background(255)
    translate(0, height/2)

    amp = 100
    freq = 1
    phase = 0 
    for x in linspace(0, width, 200):
        t = (x/width)*TWO_PI
        y = wave(t*freq + phase)*amp
        circle(x, y, 20) 
        
run()