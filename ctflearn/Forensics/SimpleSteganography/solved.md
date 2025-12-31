# TITLE : Simple Steganography
## Author : emiwaydodo
## Description
Think the flag is somewhere in there. Would you help me find it? hint-" Steghide Might be Helpfull"
## Solution
In this challenge, we were given a JPG file. I first analyzed the image using exiftool to inspect its metadata. During this analysis, I found the keyword `myadmin` in the `Keywords` field.

Next, I used `steghide` to extract hidden data from the image and supplied the discovered keyword as the passphrase. This successfully extracted a file containing a Base64-encoded string.

After decoding the Base64 string, the plaintext revealed the flag, completing the challenge.
