from py5canvas import *
from py5canvas import geom
from PIL import ImageOps
from PIL import ImageEnhance
from importlib import reload
import utils 
reload(utils)

print(utils.test)

w, h = 500, 500
# The first argument is the "camera index"
# Depending on platform you may need to change this number to 0 or 1 or 2
vin = VideoInput(1, size=(w, h)) 
#vin = VideoInput("fingers.mov", size=(w, h)) # Use a video file instead of a camera

def setup():
    create_canvas(w, h)

def draw():
    background(255,100)
    # fill(100, 50)
    no_stroke()

    img = vin.read()
    img = img.convert('L')
    contours = utils.find_contours(img, eps=random(10,90))


    img2= ImageEnhance.Color(img).enhance(0)
    img3 =ImageEnhance.Contrast(img2).enhance(10)
    img4 = ImageOps.invert(img.convert('L'))
    image(img2, opacity=100)
    image(img3, opacity=0)
    image(img4, opacity=1)

    box = geom.bounding_box(contours)
    # contours = geom.transform_to_rect(contours, geom.make_rect(0, 0, 100, 100))
    # mat = geom.rect_in_rect_transform(geom.make_rect(0, 0, w, h), geom.make_rect(0, 0, 100, 100))
    # contours = geom.tsm(mat, contours)

    

    for poly in contours:
    # print(poly)
        # polygon(poly, close=True)
        curve(poly, close=False)

    stroke(random(255)).no_fill()
    rectangle(box)
    # spacing = width/img.height
    # for y in range(img.height):
    #     for x in range(img.width): #
    #         push()
    #         v = img.getpixel((x,y)) # In range 0 - 255
    #         radius = remap(v, (0, 255), (spacing*2, -10.0))
    #         translate(x*spacing+spacing/2, y*spacing+spacing/4)
    #         text("<3", radius*2, radius*4)
    #         # circle(0, 0, radius*3)
    #         pop()

run()