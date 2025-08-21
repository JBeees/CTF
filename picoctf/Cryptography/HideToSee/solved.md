# TITLE : HideToSsee
## Author : Sunday Jacob Nwanyim
## Description
How about some hide and seek heh?
Look at this image [here](https://artifacts.picoctf.net/c/236/atbash.jpg).
## Hint
- Download the image and try to extract it.
## Solution
In this challenge, the task involves steganography, where information (such as a flag) is hidden inside a file, like an image. To solve it, I used a tool called steghide with the following command:
```
steghide extract -sf <image name>
```
Since no passphrase was required, this command extracted a .txt file containing an encrypted flag. Based on the clue provided in the image, I realized the encryption used was Atbash. After applying Atbash decoding, I successfully obtained the flag.
