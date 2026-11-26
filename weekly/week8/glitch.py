
#!/usr/bin/env python3
from py5canvas import *

num_frames = 300

def parameters():
    return {'seed': (10, 1, 1000)}

def setup():
    create_canvas(512, 512)
    # You can set it from UI also
    num_movie_frames(num_frames)
    frame_rate(30)

def draw():
    random_seed(params.seed)
    background(0)
    translate(center)
    no_fill()
    stroke(255, 180)
    rect_mode(CENTER)
    # One cycle for the loop duration
    anim_angle = remap(frame_count%num_frames, 0, num_frames, 0, TWO_PI)
    n = 13
    #blend_mode(DIFFERENCE)
    for i in range(15):
        push_matrix()
        rotate(anim_angle*(1+i))
        x = remap(i, 0, n, 0, width/2)
        translate(x, 0)
        line(0, 0, width, 0)
        #square(0, 0, 10*width/n)
        pop_matrix()


# https://necessarydisorder.wordpress.com/2017/11/15/drawing-from-noise-and-then-making-animated-loopy-gifs-from-there/
run()
