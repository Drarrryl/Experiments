# Importing Image from PIL package
from PIL import Image, ImageColor
from webcolors import rgb_to_name
from functions import returnGreat, closest_colour, get_colour_name, inColBounds, rgb2name
# creating a image object
im = Image.open(r"/workspace/Experiments/Pictures/oceanPlastic.jpg")
px = im.load()

# Max and Min for Pixels in Image
xBound, yBound = im.size

img = Image.new('RGB', (xBound, yBound))

# Available Color Names: red, yellow, green, blue, plastic
colorname = "plastic"

needColor = True

for x in range(xBound):
    for y in range(yBound):
        r = px[x, y][0]
        g = px[x, y][1]
        b = px[x, y][2]
        pxColor = rgb2name((r, g, b))
        if inColBounds(pxColor, colorname):
            print("Found", colorname, "at coords:", x, ",", y, pxColor)
            img.putpixel((x, y), (r, g, b))
        else:
            contrast = 50
            f = (returnGreat(r, g, b)-contrast)
            img.putpixel((x, y), (f, f, f))
img.save("newImg.jpg")
print("Image Saved!")