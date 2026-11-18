from py5canvas import *

num_points = 20
spacing = 5

def setup():
    create_canvas(600, 600)

def draw():
    random_seed(10)
    background(0)
    stroke(255)
    no_fill()

run()