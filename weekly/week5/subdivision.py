from py5canvas import *

offset_amt = 150 

def subdivide_and_offset(pts, amt):
    n = len(pts)
    subd = [pts[0]]
    for i in range(n-1):
        p1 = pts[i]
        p2 = pts[i+1]
        # Split the segment and offset the midpoint
        mid = (p1 + p2) / 2
        subd.append(mid + [0, random(-amt, amt)])
        subd.append(p2)
    return subd

def setup():
    global pts
    create_canvas(500, 500)
    background(255)
    # Initial polyline with two points
    pts = [Vector(0, height/2), Vector(width, height/2)]

def draw():
    background(255)
    polyline(pts)

def key_pressed():
    global pts, offset_amt
    pts = subdivide_and_offset(pts, offset_amt)
    offset_amt = offset_amt * 0.5

run()