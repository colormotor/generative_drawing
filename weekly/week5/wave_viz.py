'''
Use this sketch to visualize different waveforms 
At the beginning we set the function to visualize with
`func = sin`
- try replacing `sin` with `cos`, `triangle_wave`, `noise` 
- Try creating your own `wave` function, and set `func` to that
    - E.g. 
    def wave(t):
        return sin(t) + cos(t*2)*0.5
'''

from py5canvas import *

amp = 200

def triangle_wave(t):
    # modified from https://en.wikipedia.org/wiki/Triangle_wave
    period = 2*PI
    return 1 - 2 * abs(2*(t/period - floor(t/period + 0.5)))

# Define the function as sine
func = sin 

def setup():
    create_canvas(800, 600)

def draw():
    background(0)
    no_fill()

    stroke_weight(1.0)
    stroke(255, 110)
    line((0, height/2), (width, height/2))  # Horizontal line
    line((width/2, 0), (width/2, height))   # Vertical line

    # Map mouse position to degrees
    num_degrees = remap(mouse_x, (0, width), (-360, 360))


    # Display text information about degrees, radians, and function value
    push_matrix()
    translate(0, height/2 + 100)
    fill(255)
    text_size(20)
    text(f"Degrees: {round(num_degrees)}", (20, 50))
    text(f"Radians: {round(num_degrees/180.0 * PI, 2)}", (20, 100))
    text(f"Value: {round(func(radians(num_degrees)), 2)}", (20, 150))
    pop_matrix()

    # Draw the sine wave
    push_matrix()
    translate(0, height/2)
    no_fill()
    stroke(255, 0, 0)
    stroke_weight(3.0)

    begin_shape()
    for x in range(width):
        # Calculate the y position using the sine function and amplitude
        y = -func(remap(x, (0, width), (-TWO_PI, TWO_PI))) * amp
        vertex((x, y))
    end_shape()

    # Draw an ellipse and a line to indicate the current position on the wave
    y = -func(remap(mouse_x, (0, width), (-TWO_PI, TWO_PI))) * amp
    fill(255)
    ellipse((mouse_x, y), 10, 10)
    stroke_weight(1.0)
    stroke(255)
    line((mouse_x, y), (mouse_x, 0))

    pop_matrix()

# Run the sketch
run()
