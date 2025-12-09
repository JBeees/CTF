# TITLE : Corrupted file
## Author : Yahaya Meddy
## Description
This file seems broken... or is it? Maybe a couple of bytes could make all the difference. Can you figure out how to bring it back to life?
Download the file [here](https://challenge-files.picoctf.net/c_amiable_citadel/10f12b1f51f0a73a50f6bd08cc2d0ef6b1e8039a27daac52f27b450dabeaec97/file).
## Hints
- Try checking the file’s header.
- JPEG
- Tools like xxd or hexdump can help you inspect and edit file bytes.
## Solution
In this challenge, we were given a file. I inspected its hexadecimal content using the xxd tool:
```
xxd <file_name>
``` 
From the output, I noticed that the header indicated a JFIF signature, which means it should be a JPEG file. However, when I tried to open it, the viewer reported that the file was corrupted.

I examined the header more closely and found this at the beginning of the file:
```
00000000: 5c78 ffe0 0010 4a46 4946 0001 0100 0001 
```
The first two bytes (5C 78) were incorrect. A valid JPEG file must start with the magic bytes FF D8. Because of this incorrect header, the file was unreadable.

To fix it, I used hexedit to modify the binary and replaced the first two bytes with:
```
FF D8
```
After saving the changes, I reopened the file—and it successfully rendered. Inside, I found the flag.
