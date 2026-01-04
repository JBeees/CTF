# TITLE : Smiling ASCII
## Author : lvmalware
## Description
Find the flag on the smiling face.
## Solution
In this challenge, we are given a PNG file. I first ran strings on the file and found a Base64-encoded string:
```
RGlkIHlvdSBrbm93IHRoYXQgcGl4ZWxzIGFyZSwgbGlrZSB0aGUgYXNjaWkgdGFibGUsIG51bWJlcmVkIGZyb20gMCB0byAyNTU/Cg==
```
After decoding it, the message reads:
```
Did you know that pixels are, like the ascii table, numbered from 0 to 255?
```
This hint suggests that pixel values (which range from 0 to 255) can be interpreted directly as ASCII characters.

Next, I checked the image’s pixel mode using Python:
```
print(img.mode)
```
The output shows that the image uses four values per pixel, meaning it is in RGBA mode. After running several tests, I discovered that the hidden data is stored in the alpha channel.

To extract the flag, I used the following Python script to read the alpha values and convert them into ASCII characters:
```py
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
```
The output of this script reveals the flag.
