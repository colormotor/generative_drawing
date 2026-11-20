from py5canvas import *
import math
import numpy as np

"""
Boids simulation with sliders (Py5Canvas)

Sliders are defined in parameters(), accessible via params.<name>.
Each controls a behaviour force:
- separation: steering away from neighbours
- alignment:  matching neighbours' heading
- cohesion:   steering toward neighbours' average position
- neighbourhood_radius: distance within which boids interact
"""

# ---------------- PARAMETERS ----------------
def parameters():
    return {
        "separation": (0.1, 0.0, 1.0),
        "alignment": (0.1, 0.0, 1.0),
        "cohesion": (0.1, 0.0, 1.0),
        "neighbourhood_radius": (50.0, 5.0, 200.0),
    }

# ---------------- GLOBALS ----------------
boids = []

# ---------------- BOID CLASS ----------------
class Boid:
    def __init__(self, x, y):
        self.pos = vector(x, y)
        a = random(0, TWO_PI)
        self.direction = vector(math.cos(a), math.sin(a))

    def update(self, all_boids, params):
        # move
        self.pos += self.direction
        self.wrap_pos()

        neighbours = self.find_neighbours(all_boids, params.neighbourhood_radius)
        if len(neighbours) == 0:
            return

        # separation
        sep_force = self.sum_separation_forces(neighbours, params.neighbourhood_radius)
        sep_force = set_mag(sep_force, params.separation)
        self.direction += sep_force

        # alignment
        dir_sum = self.sum_directions(neighbours)
        heading_diff = angle_between(self.direction, dir_sum)
        self.direction = rotate_vec(self.direction, heading_diff * params.alignment)

        # cohesion
        pos_sum = self.sum_positions(neighbours)
        pos_avg = pos_sum / len(neighbours)
        pos_diff = pos_avg - self.pos
        pos_diff = set_mag(pos_diff, params.cohesion)
        self.direction += pos_diff

        # normalize speed
        self.direction = normalize(self.direction)

    def find_neighbours(self, all_boids, radius):
        neighbours = []
        for b in all_boids:
            if b is self:
                continue
            if mag(b.pos - self.pos) < radius:
                neighbours.append(b)
        return neighbours

    def sum_separation_forces(self, neighbours, radius):
        f = vector(0, 0)
        for n in neighbours:
            v = self.pos - n.pos
            d = mag(v)
            if d > 0:
                v = set_mag(v, radius - d)
                f += v
        return f

    def sum_directions(self, neighbours):
        dsum = vector(0, 0)
        for n in neighbours:
            dsum += normalize(n.direction)
        return dsum

    def sum_positions(self, neighbours):
        psum = vector(0, 0)
        for n in neighbours:
            psum += n.pos
        return psum

    def wrap_pos(self):
        if self.pos[0] > width:
            self.pos[0] -= width
        elif self.pos[0] < 0:
            self.pos[0] += width
        if self.pos[1] > height:
            self.pos[1] -= height
        elif self.pos[1] < 0:
            self.pos[1] += height

    def draw(self):
        ellipse(self.pos[0], self.pos[1], 2, 2)


# ---------------- VECTOR HELPERS ----------------
def mag(v):
    return float(np.linalg.norm(v))

def normalize(v):
    m = mag(v)
    return v / m if m != 0 else v.copy()

def set_mag(v, m):
    return normalize(v) * m if mag(v) != 0 else v.copy()

def angle_between(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    dot = x1 * x2 + y1 * y2
    det = x1 * y2 - y1 * x2
    return math.atan2(det, dot)

def rotate_vec(v, a):
    x, y = v
    c, s = math.cos(a), math.sin(a)
    return vector(x * c - y * s, x * s + y * c)


# ---------------- SETUP & DRAW ----------------
def setup():
    global boids
    create_canvas(1000, 500)
    background(0)
    no_stroke()

    for _ in range(100):
        boids.append(Boid(random(0, width), random(0, height)))


def draw(params):
    background(255, 2)
    stroke_weight(2)
    stroke(0)

    for b in boids:
        b.update(boids, params)
        b.draw()

    fill(0)
    no_stroke()
    text(f"separation: {params.separation:.2f}", 100, 25)
    text(f"alignment:  {params.alignment:.2f}", 100, 45)
    text(f"cohesion:   {params.cohesion:.2f}", 100, 65)
    text(f"radius:     {params.neighbourhood_radius:.0f}", 100, 85)

run()
