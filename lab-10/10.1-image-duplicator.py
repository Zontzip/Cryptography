import os, sys
from PIL import Image

filename = "grayscale.bmp"
height = 300
width = 400

img = Image.open(filename)
im = img.load()

i = 0
while i<height:
    j = 0
    while j<width:
        j = j+1
    i = i+1
newfile = filename.partition('.')
newfile = newfile[0] + "-copy.png"

img.save(newfile)
