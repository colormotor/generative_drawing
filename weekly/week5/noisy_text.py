from py5canvas import *

offset_amount = 40

def setup():
    create_canvas(512, 512)
    fill(255)
    no_stroke()
    translate(center)
    text_size(70)
    text_align(CENTER, CENTER)

def draw():
    background(0)
    translate(center)
    t = seconds()*0.2 # Number of seconds since we started
    points = text_points('HELLO', 0, 0, 6)
    v = t
    for p in points:
        offset_x = remap(noise(v), 0, 1, -1, 1)*offset_amount
        offset_y = remap(noise(v+0.32), 0, 1, -1, 1)*offset_amount
        circle(p[0] + offset_x, p[1] + offset_y, 3)
        v += 0.01

# Run the sketch
run()
