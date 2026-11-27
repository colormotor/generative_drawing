from py5canvas import *

num_frames = 60

def setup():
    create_canvas(400, 400)
    fill(255, 20)
    stroke(255, 100)
    
    num_movie_frames(num_frames)
    frame_rate(60)

def draw():
    background(0)
    rows, cols = 15, 15
    spacing = 20
    t = frame_count/num_frames
    for i in range(rows): 
        for j in range(cols):
            x = remap(j, 0, cols-1, spacing, width-spacing)
            y = remap(i, 0, rows-1, spacing, width-spacing)
            d = dist((x, y), center)
            w = remap(sin(d*0.1 + t*PI*2), -1, 1, spacing*0.5, spacing*2)
            circle(x, y, w)

run()