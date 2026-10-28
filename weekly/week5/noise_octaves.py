"""
TASK
- Try changing the value for persistence and see how the noise detail changes.
- See if you can modify the code to add more octaves of noise.
"""
from py5canvas import *

vals = []
freqs = []
amps = []
max_amp = 1
persistence = 0.5
summed_vals = []

def setup():
    size(1024, 800)
    stroke(255)
    
    global freqs
    freqs = [4, 8, 16, 32]
    
    recalc()

def draw():
    background(0)
    
    for i in range(len(freqs)):
        draw_graph(vals[i], 0, i * 150, 250, 150)
        
        fill(255)
        text(f"frequency: {freqs[i]}", 0, i * 150 + 25)
        text(f"amp: {amps[i]}", 0, i * 150 + 40)
    
    text(f"persistence: {persistence}", 300, 40)
    text(f"octaves: {len(freqs)}", 300, 60)
    
    draw_graph(summed_vals, 300, 100, 600, 360)
    text("summed octaves: ", 310, 120)

def recalc():
    global vals, amps, summed_vals
    vals = []
    amps = []
    amp_total = 0

    subdivision = freqs[-1] * 50

    for i in range(len(freqs)):
        amp = max_amp * pow(persistence, i)
        amps.append(amp)
        amp_total += amp
        
        octave_vals = [0]
        for _ in range(freqs[i] - 1):
            octave_vals.append(random(-amp, amp))
        octave_vals.append(0)
        
        vals.append(calc_octave(octave_vals, subdivision))
    
    summed_vals = vals[0][:]
    for i in range(1, len(vals)):
        for j in range(len(vals[i])):
            summed_vals[j] += vals[i][j]
    
    for j in range(len(summed_vals)):
        summed_vals[j] /= amp_total

def draw_graph(vals, x, y, w, h):
    no_loop()
    
    push()
    no_fill()
    stroke(255)
    rect(x, y, w, h)
    translate(x, y + h / 2)
    no_fill()
    stroke(255)
    begin_shape()
    
    for i in range(len(vals) - 1):
        xp = remap(i / (len(vals) - 1), 0, 1, 0, w)
        yp = remap(vals[i], -max_amp, max_amp, -h / 2, h / 2)
        vertex(xp, yp)
        
    end_shape()
    pop()

def calc_octave(vals, num_samples):
    v = []
    step = num_samples / (len(vals) - 1)

    for i in range(len(vals) - 1):
        x0 = (i - 1) * step
        x1 = i * step
        x2 = (i + 1) * step
        x3 = (i + 2) * step
        
        y1 = vals[i]
        y2 = vals[i + 1]
        
        y0 = 0 if i == 0 else vals[i - 1]
        y3 = 0 if i == len(vals) - 2 else vals[i + 2]
        
        for j in range(int(x1), int(x2)):
            p = (j - x1) / (x2 - x1)
            yp = cubic_interpolate(y0, y1, y2, y3, p)
            v.append(yp)
    
    return v

def cubic_interpolate(a0, a1, a2, a3, p):
    psq = p ** 2
    t0 = a3 - a2 - a0 + a1
    t1 = a0 - a1 - t0
    t2 = a2 - a0
    t3 = a1
    
    return t0 * p * psq + t1 * psq + t2 * p + t3

run()
