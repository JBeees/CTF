# TITLE : So Meta
## Author : Kevin Cooper/Danny
## Description
Find the flag in this [picture](https://jupiter.challenges.picoctf.org/static/916b07b4c87062c165ace1d3d31ef655/pico_img.png).
## Hints
- What does meta mean in the context of files?
- Ever heard of metadata?
## Solution
In this challenge, I only needed to look at the file’s metadata. I used the exiftool utility with the command `exiftool <image name>`. After running it, I found the flag in the Artist field.
