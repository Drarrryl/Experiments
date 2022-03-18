# Importing Image from PIL package
from PIL import Image, ImageColor
from webcolors import rgb_to_name
from functions import returnAvg, returnGreat, returnGreatString, returnLow, findSum, findDif, difGreat, determineMax, rgb2hex, hex2name
# creating a image object
im = Image.open(r"/workspace/Experiments/Pictures/ocean1.png")
px = im.load()

# Max and Min for Pixels in Image
xBound, yBound = im.size

img = Image.new('RGB', (xBound, yBound))

colorname = "blue"

needColor = True

for x in range(xBound):
    for y in range(yBound):
        needColor = True
        while needColor:
            r = px[x, y][0]
            g = px[x, y][1]
            b = px[x, y][2]
            pxColor = rgb_to_name((r, g, b))
            print(pxColor)
            if pxColor == colorname:
                needColor = False
                print("Found", colorname, "color at coords:", x, ",", y)
                img.putpixel((x, y), (r, g, b))
            else:
                contrast = 50
                f = (returnGreat(r, g, b)-contrast)
                img.putpixel((x, y), (f, f, f))
                needColor = False
img.save("newImg.jpg")
print("Image Saved!")
img.show()