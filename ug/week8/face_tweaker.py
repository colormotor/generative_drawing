from py5canvas import *

"""
TASK

- Add sliders for as many object properties as you can. Make sure you have the correct range, default values and step size for each slider
- Are there any properties where changing the value makes little impact? Try modifying your code to improve these.
"""

face = None

def parameters():
    # label: (default, min, max)
    return {
        "Face Width": (170.0, 80.0, 200.0),
    }

def setup():
    global face
    create_canvas(512, 512)

    # create one new face object
    face = Face(width / 2, height / 2)

def draw():
    background(0)

    # update face width from slider
    face.width = params.face_width
    face.draw()


class Face:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # object properties
        self.width = 170
        self.face_height = 200

    def draw(self):
        push_matrix()
        translate(self.x, self.y)

        # call the other draw methods
        self.draw_face()
        self.draw_eyes()
        self.draw_mouth()

        pop_matrix()

    def draw_face(self):
        fill(185, 0, 100)
        no_stroke()
        ellipse(0, 0, self.width, self.face_height)

    def draw_eyes(self):
        push_matrix()
        translate(0, -self.face_height * 0.1)

        fill(255, 255, 255)
        ellipse(-self.width * 0.15, 0, 30, 22)
        ellipse(self.width * 0.15, 0, 30, 22)

        fill(0, 0, 0)
        ellipse(-self.width * 0.15, 3, 8, 8)
        ellipse(self.width * 0.15, 3, 8, 8)

        pop_matrix()

    def draw_mouth(self):
        push_matrix()
        translate(0, self.face_height * 0.2)
        stroke_weight(2)
        no_fill()
        stroke(255)

        begin_shape()
        curve_vertex(-self.width * 0.15, 0)
        curve_vertex(-self.width * 0.15, 0)
        curve_vertex(0, 15)
        curve_vertex(self.width * 0.15, 0)
        curve_vertex(self.width * 0.15, 0)
        end_shape()

        pop_matrix()


run()
