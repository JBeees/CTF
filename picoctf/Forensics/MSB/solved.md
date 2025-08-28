# TITLE : MSB
## Author : LT 'syreal' Jones
## Description
This image passes LSB statistical analysis, but we can't help but think there must be something to the visual artifacts present in this image...
Download the image [here](https://artifacts.picoctf.net/c/303/Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png)
## Hints
- What's causing the 'corruption' of the image?
## Solution 
In this challenge, we were given a .png image. The challenge uses the MSB method to hide data inside the image. MSB means modifying the most significant bit of each pixel to store the bits of the hidden data.
To recover the hidden data, I used the tool [StegOnline](https://georgeom.net/StegOnline/). After uploading the image, I selected Extract Files/Data. Then, I set the following options:
- Pixel order: Row
- Bit order: MSB
- Bit plane order: R, G, B
- Trim trailing bits: No
- Indexes checked: 7 in the R, G, and B columns

After clicking Go, I downloaded the extracted file. Inside that file, I found the flag.
