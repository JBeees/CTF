# TITLE : What Lies Within
## Author : Julio/Danny
## Description
There's something in the [building](https://jupiter.challenges.picoctf.org/static/011955b303f293d60c8116e6a4c5c84f/buildings.png). Can you retrieve the flag?
## Hints
- There is data encoded somewhere... there might be an online decoder.
## Solution
In this challenge, the PNG image uses steganography to hide information. I analyzed it with zsteg and successfully extracted the flag.
```
zsteg <filename>
```
