# TITLE : Corrupted File
## Author : javier
## Description
Help! I can't open this file. Something to do with the file header… Whatever that is. https://mega.nz/#!aKwGFARR!rS60DdUh8-jHMac572TSsdsANClqEsl9PD2sGl-SyDk
## Solution
In this challenge, I received a GIF file. First, I examined the file header using:
```
xxd <file_name> | head
```
The header appeared incorrect:
```
00000000: 3961 f401 f401 f400 0000 0000 3a00 0000  9a..........:...
```
It seemed the GIF version was invalid (9a). To fix this, I inserted 4 additional bytes at the beginning of the file and combined it:
```
printf "\x01\x02\x03\x04" > insert.bin
cat insert.bin ex.gif > new.gif
```
Next, I used a hex editor to correct the first six bytes of the header to a valid `GIF89a` header:
```
00000000: 4749 4638 3961 f401 f401 f400 0000 0000  GIF89a..........
00000010: 3a00 0000 003a 3a00 3a66 0000 6600 3a00  :....::.:f..f.:.
```
After this fix, the GIF opened successfully. Inside, there was a hidden Base64-encoded string, but it was hard to read directly. I separated it into frames using ImageMagick:
```
convert new.gif frame_%03d.png
```
After combining all the extracted strings and decoding the Base64 content, I was able to reveal the flag.
