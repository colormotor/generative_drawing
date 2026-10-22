'''
- experiment with changing the values inside the map function to make different minimum and maximum frequencies.
- experiment with incrementing freq_mod_phase by different amounts.  Make sure you understand why this changes the effect.
- This looks like a spring. Could you introduce a further modulation to make the spring expansion and contraction go faster and slower over time ?
- Can you change the carrier_freq variable to have a modulation that changes across the wave?
    - To do so do something similar to the amplitude modulation example
    - Add a `freq_mod_freq` variable and set it to something small 
    - Inside the `sin` controlling `carrier_freq` use 
'''

from py5canvas import *

freq_mod_freq = 1.0

def setup():
    create_canvas(400,400)

def draw():
    background(0)
    no_fill()
    stroke(255)

    freq_mod_phase = frame_count*0.01

    translate(width/2,0)
    begin_shape()
    for y in range(height):
        carrier_freq = remap(sin(freq_mod_freq), -1, 1, 0.01, 0.1)
        x = remap(sin(y * carrier_freq), -1, 1, -50, 50)
        vertex(x, y)
    end_shape()

run()