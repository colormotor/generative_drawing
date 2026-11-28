from py5canvas import *

num_frames = 60

def parameters():
    return {'rows': (10, 2, 100),
            'cols': (10, 2, 100),
            'spacing': (10, 0, 300),
            'My Color': ([255, 0, 0, 0], {'type':'color'}),
            'background': ([255,0,0], {'type':'color'}),
            'shape': (0, {'selection': ['circle', 'square', 'rounded square', 'none shape']}),
            'pattern': (0.1, -1, 1),
            'opacity c': (255, 0, 255),
            'opacity b': (255, 0, 255),
            'round': (0, 0, 20),
            'stroke': (255, 0, 255),
            'text': "A",
            }

def square_shape(x, y, w, h):
    square(x, y, w)

def rounded_square_shape(x, y, w, h):
    rectangle(x, y, w, w, params.round)

def circle_shape(x,  y, w, h):
    circle(x, y, w)

def none_shape(x,  y, w, h):
    pass

shapes = [ circle_shape,
           square_shape,
          rounded_square_shape,
          none_shape]

def setup():
    create_canvas(600, 600)
    rect_mode(CENTER)
    num_movie_frames(num_frames)
    frame_rate(60)

def draw():
    background(params.background, params.opacity_b)
    stroke(params.stroke)
    fill(params.my_color, params.opacity_c)
    text_size(40)
    text_align('center', 'center')
    rows, cols = params.rows, params.cols
    spacing = params.spacing
    t = frame_count/num_frames
    for i in range(rows): 
        for j in range(cols):
            x = remap(j, 0, cols-1, spacing, width-spacing)
            y = remap(i, 0, rows-1, spacing, width-spacing)
            d = dist((x, y), center)
            w = remap(cos(d*params.pattern + t*PI*2), -1, 1, spacing*params.pattern, spacing*2)
            # rectangle(x, y, w, w, params.round)
            push_matrix()
            shapes[params.shape](x, y, w, w)
            text_size(w)
            text(params.text, x, y) # x+w, y+w/2)
            pop_matrix()
            # circle(x, w, w)

run()