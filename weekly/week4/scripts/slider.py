''' Basic slider example. 
Note this is not the proper way to handle mouse interaction with a slider, 
since the slider will stop working as soon as the mouse moves away from the slider handle.
A more robust implementation would require tracking whether the mouse is being dragged.'''

from py5canvas import *

val = 50

def slider(value, x, y, w, h, max_val=100):
    """A crude slider. It takes the current value and position/size as arguments, 
    and returns the updated value."""
    # Draw slider background
    fill(200)
    rect(x, y, w, h)
    
    # Map value to position
    x2 = remap(value, 0, max_val, x, x + w)
    if dragging and dist(mouse_x, mouse_y, x2, y + h/2) < h:
        x2 = mouse_x
        x2 = constrain(x2, x, x + w)
        value = remap(x2, x, x+w, 0, max_val)
    
    # Draw slider handle
    fill(100)
    circle(x2, y + h/2, h)
    return value

def setup():
    create_canvas(400, 400)

def draw():    
    global val
    background(220)
    h = 60
    val = slider(val, 50, height/2-h/2, 300, h)

    no_stroke()
    text_size(32)
    text_align(CENTER)
    text(f"Value: {int(val)}", width/2, height/2 + 100)
run()
