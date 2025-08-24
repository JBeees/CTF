# TITLE : Enhance!
## Author : LT 'syreal' Jones
## Description
Download this image file and find the flag.
- [Download image file](https://artifacts.picoctf.net/c/100/drawing.flag.svg)
## Solution
In this challenge, I used the **strings** command to extract readable text from the file. When I inspected the .svg file in string form, I found a piece of the flag at the bottom of the file. After wrapping it with picoCTF{}, I obtained the complete flag.
