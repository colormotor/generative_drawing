#!/usr/bin/env python3
from py5canvas import *

num_frames = 200

def setup():
    create_canvas(512, 512)
    # You can set it from UI also
    num_movie_frames(num_frames)
    frame_rate(30)

def draw():
    background(0)
    translate(center)
    fill(255)
    no_stroke()

    # One cycle for the loop duration
    t = frame_count/num_frames
    anim_angle = TWO_PI*t #(frame_count/num_frames)
    anim_angle = remap(frame_count, 0, num_frames, 0, TWO_PI)
    #rotate(anim_angle)
    #circle(200, 0, 50)
    circle(sin(anim_angle*2)*200, 0, 50)
    

run()
