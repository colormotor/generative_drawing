from py5canvas import *
# Converted from https://editor.p5js.org/codingtrain/sketches/sPvZsg2w4
# See https://youtu.be/MY4luNgGfms?si=en8zn1_nBLf2k_7i
# Coding Challenge 130.3: Drawing with Fourier Transform and Epicycles
# Daniel Shiffman
# https://thecodingtrain.com/CodingChallenges/130.1-fourier-transform-drawing.html
# https://thecodingtrain.com/CodingChallenges/130.2-fourier-transform-drawing.html
# https://thecodingtrain.com/CodingChallenges/130.3-fourier-transform-drawing.html
# https://youtu.be/7_vKzcgpfvU

USER = 0
FOURIER = 1

x = []
fourier_x = None
time = 0
path = []
drawing = []
state = -1

def dft_np(x):
    x = np.asarray(x, dtype=np.float64)

    # Convert to complex vector
    x = x[:,0] + 1j * x[:,1]

    #x = np.asarray(x, dtype=np.complex128)
    N = x.size

    # Your code divides each DFT bin by N, so match that normalization:
    X = np.fft.fft(x) / N

    re = X.real
    im = X.imag
    freq = np.arange(N)
    amp = np.abs(X)
    phase = np.angle(X)

    res = [
        {'re': float(re[k]),
         'im': float(im[k]),
         'freq': int(freq[k]),
         'amp': float(amp[k]),
         'phase': float(phase[k])}
        for k in range(N)
    ]

    res.sort(key=lambda a: a['amp'], reverse=True)
    return res

def dft(x):
    X = []
    N = len(x)
    for k in range(N):
        sum = complex(0, 0)
        for n in range(N):
            phi = (TWO_PI * k * n) / N
            c = complex(cos(phi), -sin(phi))
            sum += x[n]*c # Complex multiplication
                          # differently from vector multiplication,
                          # it has a geometric meaning (rotation and scaling)
            
        sum = sum/N 

        freq = k
        amp = sqrt(sum.real * sum.real + sum.imag * sum.imag)
        phase = atan2(sum.imag, sum.real)
        X.append({ 're': sum.real, 
                   'im': sum.imag, 
                   'freq': freq, 
                   'amp': amp,
                   'phase': phase })
        
    print(len(X))
    return X
    
def mouse_pressed():
    print("Press")
    global state, drawing, x, time, path
    state = USER
    drawing = []
    x = []
    time = 0
    path = []

def mouse_released():
    print("Release")
    global state, fourier_x
    state = FOURIER
    skip = 1
    #for i in range(0, len(drawing), skip):
    #    x.append(complex(drawing[i][0], drawing[i][1]))
    fourier_x = dft_np(drawing[::skip])
    
    fourier_x.sort(key=lambda a: a['amp'], reverse=True)

def setup():
    create_canvas(500, 500)
    background(0)
    fill(255)
    text_align(CENTER)
    text_size(64)
    text("Draw Something!", width/2, height/2)

def epicycles(x_pos, y_pos, rotation, fourier):
    x = x_pos
    y = y_pos
    for i in range(len(fourier)):
        prevx = x
        prevy = y
        freq = fourier[i]['freq']
        radius = fourier[i]['amp']
        phase = fourier[i]['phase']
        x += radius * cos(freq * time + phase + rotation)
        y += radius * sin(freq * time + phase + rotation)

        stroke(255, 100)
        no_fill()
        ellipse(prevx, prevy, radius * 2)
        stroke(255)
        line(prevx, prevy, x, y)
    return vector(x, y)

def draw():
    global time, path
    background(0)

    if state == USER:
        point = vector(mouse_x - width / 2, mouse_y - height / 2)
        drawing.append(point)
    
    stroke(255)
    no_fill()
    begin_shape()
    for v in drawing:
        vertex(v[0] + width / 2, v[1] + height / 2)
    end_shape()

    if state == FOURIER:
        v = epicycles(width / 2, height / 2, 0, fourier_x)
        path.insert(0, v)
        begin_shape()
        no_fill()
        stroke_weight(2)
        stroke(255, 0, 255)
        for i in range(len(path)):
            vertex(path[i][0], path[i][1])
        end_shape()

        dt = TWO_PI / len(fourier_x)
        time += dt

        if time > TWO_PI:
            time = 0
            path = []

run()