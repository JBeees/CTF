# TITLE : Naughty Cat
## Author : Negatyw01
## Description
I think my cat is hiding something...
## Solution
In this challenge, we were given a PNG file. When analyzing the file using pngcheck, it reported additional data after the `IEND` chunk, which indicates that extra data is appended to the image and may contain an embedded file.

To extract the embedded data, I used:
```
binwalk -e <file_name>
```
This command extracted a directory containing an MP3 file. I then played the audio using `ffplay`. By pressing the `w` key during playback to cycle through visualization modes, I observed a hidden text in the spectrogram, indicating the use of spectrogram steganography.
The revealed text was:
```
str3am_1s_y0ur_fr13nd
```
At first, I assumed this string was the flag, but it was not accepted.
Upon further inspection, I discovered a RAR file with a corrupted header. To fix it, I manually corrected the first 8 bytes of the file to the valid RAR5 header:
```
52 61 72 21 1A 07 01 00
```
This was done using:
```
hexedit <file_name>
```
After repairing the header, I extracted the archive using:
```
unrar x <file_name>
```
The extraction process prompted for a password. I used the previously recovered spectrogram text. This successfully extracted a `.txt` file, whose contents contained the actual flag.
