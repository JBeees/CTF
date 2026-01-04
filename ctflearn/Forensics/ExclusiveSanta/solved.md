# TITLE : Exclusive Santa
## Author : EdbR
## Description
Dear Santa,
Hey! There are so many toys that I want, but I just don't have the money. I don't care which toy I get as long as it's one or the other, but not both!
## Solution
In this challenge, we were given a RAR archive. After extracting it using unrar, we obtained two images, named `1.png` and `3.png`.

I then analyzed `3.png`using `binwalk` and discovered that it contained multiple embedded files, including another PNG image:
```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1200 x 875, 8-bit/color RGBA, non-interlaced
78            0x4E            Zlib compressed data, default compression
52406         0xCCB6          PNG image, 1280 x 720, 8-bit/color RGBA, non-interlaced
52447         0xCCDF          Zlib compressed data, compressed
```
This output indicates that a second PNG image is embedded inside `3.png` at offset `52406` (0xCCB6). I extracted this embedded image using the following command:
```
dd if=3.png of=img2.png bs=1 skip=52406
```
After extraction, I examined all three images: `1.png`, `3.png`, and `img2.png`.
- `3.png` appears to serve as a hint, depicting an XOR-related diagram.
- `1.png` is a distorted image, likely containing obfuscated data.
- `img2.png` appears to be the clean reference image corresponding to `1.png`.
Based on the hint in `3.png,` I performed an LSB XOR operation between `1.png` and `img2.png`. This revealed a new image containing the actual flag, but in reversed order.
Finally, I reversed the extracted text to obtain the correct flag.

To perform the LSB XOR operation, I used the following script
```py
from PIL import Image
import numpy as np

a = np.array(Image.open("1.png").convert("RGB"))
b = np.array(Image.open("img2.png").convert("RGB"))

# extract LSB
a_lsb = a & 1
b_lsb = b & 1

# XOR LSBs
xor_lsb = a_lsb ^ b_lsb

# amplify for visibility
out = xor_lsb * 255

Image.fromarray(out.astype(np.uint8)).save("xor_lsb.png")
```
