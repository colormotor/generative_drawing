from py5canvas import *

"""
TASK
- Experiment with changing the faceWidth and faceHeight properties. Note how this changes the character of the face.
- Inspect the code in drawEyes and drawMouth. Replace the hard-coded constants with meaningful properites of the face object. 
- Try modifying the values of your new properties to make different facial expressions and characters
- Continue to add to the face constuctor function. You might add a function hair, ears, a nose, or less human features like tenticles or horns ! Use your imagination ! For each feature avoid hard-coded constants and instead use adaptable properties.
- Now set each property randomly inside the constructor function so that you see a different version of the face each time you refresh the screen
- Finally make an array of face objects and draw multiple ones to the screen
"""

face = None

def setup():
    global face
    create_canvas(512, 512)

    # create one new face object
    face = Face(width / 2, height / 2)


def draw():
    background(0)
    face.draw()


class Face:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # object properties
        self.face_width = 170
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
        ellipse(0, 0, self.face_width, self.face_height)

    def draw_eyes(self):
        push_matrix()
        translate(0, -self.face_height * 0.1)

        # white of the eyes
        fill(255, 255, 255)
        ellipse(-self.face_width * 0.15, 0, 30, 22)
        ellipse(self.face_width * 0.15, 0, 30, 22)

        # pupils
        fill(0, 0, 0)
        ellipse(-self.face_width * 0.15, 3, 8, 8)
        ellipse(self.face_width * 0.15, 3, 8, 8)

        pop_matrix()

    def draw_mouth(self):
        push_matrix()
        translate(0, self.face_height * 0.2)
        stroke_weight(2)
        no_fill()
        stroke(255)

        begin_shape()
        curve_vertex(-self.face_width * 0.15, 0)
        curve_vertex(-self.face_width * 0.15, 0)
        curve_vertex(0, 15)
        curve_vertex(self.face_width * 0.15, 0)
        curve_vertex(self.face_width * 0.15, 0)
        end_shape()

        pop_matrix()


run()
