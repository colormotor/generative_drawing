from py5canvas import *

"""
TASK

- Experiment with changing the starting diameter, the decrementing of diameter and the exit condition. How does it change the visual output.
- Add a second call to draw_circle inside the recursive function. Offset x so that you can see the extra circles. How many more are drawn ? 
- Add further calls to draw_circle. Adjust how x,y and diameter change between function calls to create different patterns.
- Try adding extra elements to create new patterns (Eg. recursively changing colours, random displacement, rotation)
"""

def setup():
    create_canvas(512, 512)

    stroke(0)
    no_fill()

    background(255)
        
    draw_circle(width/2, height/2, width)

def draw_circle(x, y, diameter):
    # draw the circle
    ellipse(x, y, diameter)
    
    # You must always have an exit condition or your program will enter into an infinite loop - a crash
    if diameter < 5:
        return  # leave the function
    else:
        # make a recursive function call but with a reduced diameter
        draw_circle(x, y, diameter * 0.5)

run()
