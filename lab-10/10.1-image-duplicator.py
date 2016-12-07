from PIL import Image

def duplicate_image(filename):
    img = Image.open(filename)
    im = img.load()
    (width, height) = img.size

    newImg = Image.new("RGB", (width, height))
    newIm = newImg.load()

    for x in range(width):
        for y in range(height):
            newIm[x, y] = im[x, y]

    gray = newImg.convert('L')
    gray.save("newImage.jpg", "JPEG")

if __name__ == "__main__":
    duplicate_image("cat.jpg")