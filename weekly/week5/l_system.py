from py5canvas import *

"""
    Basic L-system implementation
  TASKS:
  - Modify the distance and angle parameters and the number of iterations and understand how these affect the drawing
  - Try inserting different rules and axioms
    + E.g. from here // https://fedimser.github.io/l-systems.html or other resources on the internet.
  - Examine the draw_l_system function. How can you add random variations to the drawing?
    + The result is known as a stochastic L-system
    + Use random_seed to avoid the drawing changing each frame
  - draw_turtle function currently draws a line. Modify this function to change how the L-system is visualized
  - Harder challenge: can you modify the L-system code so we also get information on the recursion depth for each symbol?
"""

# A tree
rules = { 'X': 'F+[[X]-X]-F[-FX]+X',
          'F': 'FF'}
axiom = 'X'
angle = 30
iterations = 6
length = 30

## Koch curve/snowflake
rules = { 'F': 'F-F++F-F' }
axiom = 'F';
# axiom = 'F++F++F' # snowflake
angle = 60

# iterations = 5
# length = 10

## Bush
# rules = {'F': 'FF+[+F-F-F]-[-F+F+F]' }
# axiom = 'F'
# angle = 30
# iterations = 4
# length = 40

def setup():
    create_canvas(800, 800)
    background(245)
    stroke(0)
    translate(width/2, height/1.3)
    rotate(radians(-90)) 
    
    symbols = l_system(iterations, axiom, rules)
    print(symbols)
    draw_l_system(symbols, length/iterations, angle)
    

def l_system(num_iters, axiom, rules):
    symbols = axiom
    for i in range(num_iters):
        symbols = apply_rules(symbols, rules)
    return symbols

def apply_rules(symbols, rules):
    # Apply the rules to each character in a string and return a new string
    newstr = ""
    for symbol in symbols:
        if symbol in rules:
            newstr += rules[symbol]
        else:
            newstr += symbol
    return newstr

def draw_turtle(x1, y1, x2, y2):
    line(x1, y1, x2, y2)

def draw_l_system(symbols, distance, angle):
    # Parse the L-system symbols and move the turtle accordingly
    stack = []  # For push/pop operations
    
    for symbol in symbols:
        if symbol == "F" or symbol == "G" or symbol == "A":
            # forward and draw
            draw_turtle(0, 0, distance, 0)
            translate(distance, 0)
        elif symbol == "f" or symbol == "B":
            # forward without drawing
            translate(distance, 0)
        elif symbol == "+":
            # turn right
            rotate(radians(-angle))
        elif symbol == "-" or symbol == "−":
            # turn left
            rotate(radians(angle))
        elif symbol == "[":
            # save turtle state
            push_matrix()
        elif symbol == "]":
            # restore turtle state
            pop_matrix()
            
run()
