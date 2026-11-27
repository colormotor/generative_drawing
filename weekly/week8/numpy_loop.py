from py5canvas import *

num_frames = 300

def parameters():
    return {'Palette y': (0.0, 0.0, 1.0),
            'mult': (5, 1, 30)}

def colorize_image(grey_img, palette, row):
    palette = np.array(palette)/255 # Assume input is a PIL image
    grey_img = normalize_image(grey_img)
    rows, cols, channels = palette.shape
    row = int(row*(rows-1))
    # .astype converts an array to the given type
    # we need indices to be integers so we convert to `int`
    indices = (grey_img * (cols - 1)).astype(int)
    return palette[row, indices]


def normalize_image(im):
    return (im - im.min())/(im.max() - im.min())
    
palette = load_image('./palette.jpg')

def setup():
    create_canvas(400, 400)
    num_movie_frames(num_frames)
    frame_rate(60)

def draw():
    t = frame_count/num_frames
    # Get two grids one for x's and one for y's 
    x, y = np.meshgrid(np.linspace(-1, 1, width), np.linspace(-1, 1, height))
    # Convert to polar coordinates (angle, radius)
    angle = np.arctan2(y, x)
    r = sqrt(x**2 + y**2)
    # Comment/uncomment for different variants
    # Spiral
    # v = sin(10 * r + 5 * angle + t * TWO_PI * 2)

    # Expanding circles
    #v = sin(20 * r - t * TWO_PI * 4)

    # Pulsing rounded squares
    v = sin((cos(x * PI) * sin(y * PI) + t * TWO_PI) * params.mult)

    # Trifoil warp 
    # v = sin(8 * r + 6 * sin(3 * angle + t * TWO_PI) + t*TWO_PI*4)

    # Noisy pattern
    #v = sin(noise(x*2)*5 + cos(y*8) + t*TWO_PI)

    # Ripple
    #v = sin((x**2 + y**2)*10 + t*TWO_PI*3)
    
    # Draw it
    image(colorize_image(v, palette, params.palette_y))

run()