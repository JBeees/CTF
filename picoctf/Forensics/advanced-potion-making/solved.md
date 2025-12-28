# TITLE : advanced-potion-making
## Author : BIGC
## Description
Ron just found his own copy of advanced potion making, but its been corrupted by some kind of spell. Help him recover it!
## Solution
In this challenge, we were given a corrupted PNG file. To investigate the issue, I first inspected the file’s hex header using:
```
xxd <file_name> | head
```
The output 
```
00000000: 8950 4211 0d0a 1a0a 0012 1314 4948 4452  .PB.........IHDR
00000010: 0000 0990 0000 04d8 0802 0000 0004 2de7  ..............-.
00000020: 7800 0000 0173 5247 4200 aece 1ce9 0000  x....sRGB.......
```
From this output, it is clear that the file was intended to be a PNG, as the IHDR chunk is present. However, the PNG signature and IHDR length fields were corrupted, which prevents image viewers and analysis tools from parsing the file correctly.
### Fixing the PNG Header
To repair the file, I edited the header manually using:
```
hexedit <file_name>
```
I corrected the PNG signature and IHDR length to their proper values:
```
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
00000010: 0000 0990 0000 04d8 0802 0000 0004 2de7  ..............-.
```
After applying these changes, I verified the file using pngcheck, which reported no errors, confirming that the PNG structure was now valid.
When opening the repaired image, it displayed only a red image. This suggested that the visible image data was intentionally misleading and that the flag might be hidden at the bit level rather than in the visible pixel data.

To investigate this, I used [StegOnline](https://georgeom.net/StegOnline/) and selected the “Browse Bit Planes” feature. By examining individual bit planes of the image, the hidden message became visible, revealing the flag.
