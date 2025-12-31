# TITLE : abandoned place
## Author : fakeprofile
## Description
the flag is outside of the pic, try to find it. another hint: dimensions, dimensions, everything is in dimensions.
## Solution
In this challenge, I received a JPEG file. The description mentioned the dimensions of the image. At first, analyzing the file revealed nothing unusual. Later, I discovered a method to change the image dimensions to reveal hidden data.

In a JPEG file, the image dimensions are stored in the SOF0 (Start of Frame) marker, which starts with 0xFFC0. I located this marker at offset 0x9D using the command:
```
xxd <file_name> | grep "ffc0"
```
The relevant bytes looked like this:
```
00000090: 1414 1414 1414 1414 1414 1414 1414 ffc0  ................
000000a0: 0011 0806 8407 e003 0111 0002 1101 0311  ................
```
Here, the height and width of the image are specified after the marker. I increased the height to 0x684 (1668 in decimal). After saving the modified file and opening it, the hidden content (the flag) became visible.

