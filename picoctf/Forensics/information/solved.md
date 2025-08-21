# TITLE : information
## Author : SUSIE
## Description
Files can always be changed in a secret way. Can you find the flag? [cat.jpg](https://mercury.picoctf.net/static/149ab4b27d16922142a1e8381677d76f/cat.jpg)
## Hints
- Look at the details of the file
- Make sure to submit the flag as picoCTF{XXXXX}
## Solution
To solve this challenge, I inspected the image’s metadata using [exiftool](https://exiftool.org/). In the License field I found a string encoded in Base64. After decoding that Base64 string, I obtained the flag.
```
exiftool <image name>
```

