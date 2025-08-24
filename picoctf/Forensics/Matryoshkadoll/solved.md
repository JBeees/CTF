# TITLE : Matryoshka doll
## Author : Susie/Pandu
## Description
Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](https://mercury.picoctf.net/static/f6cc2560a70b1ea811c151accba5390f/dolls.jpg)
## Hints
- Wait, you can hide files inside files? But how do you find them?
- Make sure to submit the flag as picoCTF{XXXXX}
## Solution
In this challenge, the hint suggested that there was a file hidden inside another file. To verify this, I inspected the .jpg file using xxd and noticed a .zip header appearing after the .png IEND chunk. This indicated that another file was appended.

I then used **binwalk** to extract the hidden file, which gave me another directory containing an image. I repeated the same process checking for hidden data inside the extracted files with binwalk until I eventually found the flag file. Opening it revealed the flag.

