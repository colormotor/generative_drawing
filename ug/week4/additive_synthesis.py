'''
EXPLORE

- Adjust freq1, freq2, amp1, amp2 and observe the effects
- Try adding another sine wave to the signal to create little hills on the smaller hills
- How could you combine these effects with animation and modulation to enrich your sketches ?

'''

from py5canvas import *

freq1 = 0.01
freq2 = 0.1
amp1 = 100
amp2 = 9

def setup():
    create_canvas(800,400)

def draw():
    background(255)
    stroke(0)
    no_fill()
    translate(0,height/2)

    begin_shape()
    for x in range(width):
        y = sin(x*freq1) * amp1
        y += sin(x*freq2) * amp2
        vertex(x, y)
    
    end_shape()

run()

