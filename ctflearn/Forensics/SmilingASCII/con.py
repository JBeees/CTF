from PIL import Image

img = Image.open("smiling.png")
pixels = img.load()

out = ""
for y in range(img.height):
    for x in range(img.width):
        r, g, b, a = pixels[x, y]
        if 32 <= a <= 126:   # printable ASCII
            out += chr(a)

print(out)

