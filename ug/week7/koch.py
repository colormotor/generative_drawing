from py5canvas import *
"""
TASK
- Complete the generate function
- Experiment with modifying the length of the points and angle of rotation top change the character of the Koch line
- Adapt the code to make a Koch snowflake 
"""

lines = []

def setup():
    create_canvas(600, 300)
 
    # Left side of window
    start = vector(0, 200)

    # Right side of window
    end = vector(width, 200)
 
    # The first KochLine object
    lines.append(KochLine(start, end))
    

def draw():
    background(255)
    for i in range(len(lines)):
        lines[i].display()
        

def key_pressed():
    generate()


def generate():
    # We need to replace lines here so declare it global
    global lines
    # make a place to temporarily store our lines
    new_lines = []
    
    for i in range(len(lines)):
        # get the five points from the KochLine
        
        # construct four new Kochlines out of the five points and push them to new_lines
        
        # A-B
        new_lines.append(KochLine(lines[i].get_point_a(), lines[i].get_point_b()))
        
        # B-C
        new_lines.append(KochLine(lines[i].get_point_b(), lines[i].get_point_c()))
        
        
        # C-D
        new_lines.append(KochLine(lines[i].get_point_c(), lines[i].get_point_d()))
        
        # D-E
        new_lines.append(KochLine(lines[i].get_point_d(), lines[i].get_point_e()))
        
        
    # replace the old lines with the new_lines
    lines = new_lines


class KochLine:
    def __init__(self, a, b):
        self.start = a
        self.end = b

    def display(self):
        stroke(0)
        # Draw the line from start to end.
        line(self.start[0], self.start[1], self.end[0], self.end[1])
    
    def get_point_a(self):
        # start of the line
        return self.start.copy()
    
    def get_point_b(self):
        # one third way point
        v = self.end - self.start
        v = v * (1/3)
        return self.start + v
    
    def get_point_c(self):
        # the raised mid-way point
        # this is the hardest point to calculate
        p = self.get_point_b()
        v = self.end - self.start
        v = v * (1/3)
        # Rotate vector by -PI/3
        angle = -PI/3
        v_rotated = vector(v[0] * cos(angle) - v[1] * sin(angle), 
                          v[0] * sin(angle) + v[1] * cos(angle))
        return p + v_rotated
    
    def get_point_d(self):
        # two thirds way point
        v = self.end - self.start
        v = v * (2/3)
        return self.start + v
    
    def get_point_e(self):
        # end of the line
        return self.end.copy()

run()
