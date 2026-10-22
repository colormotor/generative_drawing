''' 
Visualizes point along a circle as a combination of an 
"x axis" and "y_axis" vectors, scaled by the cosine and sine of an angle 
'''

from py5canvas import *

def setup():
    create_canvas(500, 500)

def draw():
    background(0)

    # X and Y axes, scaled by the radius
    radius = width/4
    x_axis = Vector(1, 0)*radius
    y_axis = Vector(0, 1)*radius
    
    # The corresponding circle
    stroke(255, 100)
    no_fill()
    circle(center, radius)

    # Find a vector going from the center to the mouse position
    # The orientation of this vector is the angle we visualize
    dir = mouse_pos - center
    angle = heading(dir)

    # Get the x axis scaled by cosine 
    x_vec = x_axis*cos(angle)
    # Get the y axis scaled by cosine
    y_vec = y_axis*sin(angle)

    # The point on the circle is the sum of these two vectors
    # added to the center o the circle
    p = center + x_vec + y_vec

    # Visualize the point with an arrow
    stroke(255)
    arrow(center, p)

    # Parallelogram rule (in this case a rectangle)
    stroke_weight(1)
    stroke(128)
    arrow(center + x_vec, p)
    arrow(center + y_vec, p)

    # Draw the "axes" and their weighted versions
    stroke_weight(3)

    # X
    stroke(255, 0, 0, 100)
    line(center, center + x_axis)
    stroke(255, 0, 0)
    arrow(center, center + x_vec)

    # Y
    stroke(0, 255, 0, 100)
    line(center, center + y_axis)
    stroke(0, 255, 0)
    arrow(center, center + y_vec)
    
    fill(255)
    no_stroke()
    text_size(15)
    text_x = 20
    text_y = height - 70
    text(f"Degrees: {round(degrees(angle))}", (text_x, text_y))
    text(f"Radians: PI * {round(angle/PI, 2)}", (text_x, text_y + 20))
    text(f"cos: {round(cos(angle), 2)}", (text_x, text_y + 40))
    text(f"sin: {round(sin(angle), 2)}", (text_x, text_y + 60))
    
    
run()