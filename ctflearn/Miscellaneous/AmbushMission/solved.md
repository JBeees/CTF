# TITLE : Ambush Mission
## Author : pian
## Description
Hi, i can't tell you my name since now i'm in a mission. In case to arrest our fugitive target, our team had been intercepted communication between the target with his fellow and found this image (https://mega.nz/#!TKZ3DabY!BEUHD7VJvq_b-M22eD4VfHv_PPBnW2m7CZUfMbveZYw). It looks like they are going to meet in specific place, but we still don't know the time yet. Can you help me?
## Solution
In this challenge, we were given a `PNG` file. Initial analysis using common forensic tools such as `strings`, `binwalk`, and `exiftool` did not reveal any useful information. I then uploaded the image to an online steganography analysis tool, [StegOnline](https://georgeom.net/StegOnline/image). By browsing the bit planes—specifically bit 0 of the red channel—I discovered hidden data. The extracted data turned out to be a reversed Base64-encoded string. After reversing the string to its correct order and decoding it using Base64, the flag was successfully revealed.
