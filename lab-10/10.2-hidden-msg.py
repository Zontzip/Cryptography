from PIL import Image

def bitGenerator(messageBits):
    i = 0
    while i < len(messageBits):
      yield messageBits[i]
      i += 1

def hideMsg(image, message):
  (width, height) = image.size

  binMessage = ' '.join(format(ord(x), 'b') for x in message)

  bitsGenerator = bitGenerator(binMessage)
  for x in range(0, width):
    for y in range(0, height):
      pixel = image.getpixel((x, y))

      binPixel = bin(pixel)
      try:
        messageBit = bitsGenerator.next()
        print(messageBit)
        binPixel = binPixel[:-1] + messageBit

        image.putpixel((x, y), int(binPixel, 2))
      except StopIteration:
        return 


image = Image.open("newImage.jpg")
message = "Lorem ipsum dolor sit amet."
hideMsg(image, message)
image.save("hiddenMsgImage.jpg")
