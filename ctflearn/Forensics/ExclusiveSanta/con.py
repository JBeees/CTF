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

