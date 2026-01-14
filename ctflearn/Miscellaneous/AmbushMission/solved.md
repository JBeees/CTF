# TITLE : Ambush Mission
## Author : pian
## Description
Hi, i can't tell you my name since now i'm in a mission. In case to arrest our fugitive target, our team had been intercepted communication between the target with his fellow and found this image (https://mega.nz/#!TKZ3DabY!BEUHD7VJvq_b-M22eD4VfHv_PPBnW2m7CZUfMbveZYw). It looks like they are going to meet in specific place, but we still don't know the time yet. Can you help me?
## Solution
In this challenge, we were given a PNG file. When I analyzed it using common forensic tools such as `strings`, `binwalk`, and `exiftool`, no useful information was found. I then used an online steganography analysis tool, which revealed that the hidden data was a reversed Base64-encoded string. After reversing the string back to its correct order and decoding it using `Base64`, the flag was successfully revealed.
