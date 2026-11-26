from py5canvas import *

num_frames = 100

def setup():
    create_canvas(400, 400)
    fill(255, 70)
    stroke(255)
    
    num_movie_frames(num_frames)
    frame_rate(60)
    rect_mode(CENTER)

def draw_object(x, y, w, t, i):
    
    push_matrix()
    translate(x, y)
    # Draw something else here
    rotate(random(0, TWO_PI))
    square(0, 0, w)
    pop_matrix()

def draw():
    random_seed(232)
    background(0)
    w = 40
    t = frame_count/num_frames
    # We want the shape to fully disappear 
    # so the desired range is:
    wrap_dist = width+w*2
    # Draw multiple circles
    n = 10
    for i in range(n):
        # Offset of the circle on the range
        x = remap(i, 0, n, 0, wrap_dist)
        # We add the offset and modulo the result to wrap
        draw_object((frame_count + x)%wrap_dist - w, 
               height/2, 40, t, i)

    
run()