# TITLE : Snowboard
## Author : kcbowhunter
## Description
Find the flag in the jpeg file. Good Luck!
## Solution
In this challenge, we were given a JPG file. When I analyzed the file using `exiftool`, I found a string resembling a flag in the `comment` field. However, submitting this value resulted in an incorrect flag.

I then examined the file’s hex data using the command:
```
xxd <file_name> | head
```
In the output, I noticed a Base64-encoded string embedded in the file header. After decoding the Base64 data, I obtained the real flag.
```
Q1RGbGVhcm57U2tpQmFuZmZ9Cg==
```
