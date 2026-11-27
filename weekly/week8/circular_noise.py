#!/usr/bin/env python3
from py5canvas import *

num_frames = 300
def parameters():
    return {'seed': (10, 1, 1000)}

def setup():
    create_canvas(512, 512)
    num_movie_frames(num_frames) # You can set it from UI but here is nicer
    noise_detail(4, 0.5, gradient=True)

def draw():
    random_seed(params.seed)
    background(0)
    translate(center)
    no_fill()
    stroke(255, 180)
    anim_theta = remap(frame_count%num_frames, 0, num_frames, 0, TWO_PI)

    # Show line for debug
    line([0, 0], direction(anim_theta)*100)

    n = 15
    nz = random(0, 100, n)
    fill(255, 5)

    for j in range(20):
        rmul = remap(j, 0, 10, 1, 5)
        angs = np.linspace(0, TWO_PI, n, endpoint=False)
        noise_radii = np.linspace(0.2, 0.3, n)
        nx = np.cos(anim_theta)*noise_radii
        ny = np.sin(anim_theta)*noise_radii

        radii = remap(noise(nx, ny, nz + j*0.1), 0.0, 1.0, 0, 100+j*30) #350-j*30, 0)
        polyline(np.cos(angs)*radii,
              np.sin(angs)*radii,
              close=True)

    return

    n = 15
    for j in range(10):
        rmul = remap(j, 0, 10, 1, 5)
        begin_shape()
        for i in range(n):
            ang = remap(i, 0, n, 0, TWO_PI)
            r_noise = remap(i, 0, n, 0.2, 0.5)
            r = (noise(cos(anim_theta)*r_noise,
                    sin(anim_theta)*r_noise,
                    random(0, 100))*150 + 10)*rmul
            curve_vertex(cos(ang)*r, sin(ang)*r)
        end_shape(CLOSE)


run()
