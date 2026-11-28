#!/usr/bin/env python3
from py5canvas import *

num_frames = 100

def setup():
    create_canvas(512, 512)
    # You can set it from UI also
    num_movie_frames(num_frames)
    frame_rate(60)

def draw():
    background(0,5)
    translate(center)
    fill(random(200), random(200), random(200))
    no_stroke()

    # One cycle for the loop duration
    t = frame_count/num_frames
    anim_angle = TWO_PI*t #(frame_count/num_frames)
    rotate(anim_angle)
    circle(sin(anim_angle)*200, -200, 30)
    

run()
