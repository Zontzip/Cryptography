import os, sys
from PIL import Image

filename = "grayscale.bmp"
width = 400
height = 300

img = Image.open(filename)
im = img.load()

newImg = Image.new("RGB", (width, height))
newIm = newImg.load()

for x in range(width):
    for y in range(height):
        newIm[x, y] = im[x, y]

newImg.save("test.png", "PNG")
