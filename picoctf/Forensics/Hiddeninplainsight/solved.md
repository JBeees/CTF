# TITLE : Hidden in plainsight
## Author : Yahaya Meddy
## Description
You’re given a seemingly ordinary JPG image. Something is tucked away out of sight inside the file. Your task is to discover the hidden payload and extract the flag.
Download the jpg image [here](https://challenge-files.picoctf.net/c_amiable_citadel/90f1eb2dc53634c5e708b56878391f0398bc8848104d86464e06822a469d2d99/img.jpg).
## Hints
- Download the jpg image and read its metadata
## Solution
In this challenge, we were given a JPG file. First, I checked its metadata using:
```
exiftool <jpg_name>
```
In the Comment field, I found this Base64 string:
```
c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9
``` 
After decoding it, I obtained:
```
steghide:cEF6endvcmQ=
```
The part after the colon is another Base64 string, which decodes to:
```
pAzzword
```
This suggested that the file contained hidden data using steghide, with the passphrase `pAzzword`.
To extract the hidden file, I ran:
```
steghide extract -sf <jpg_name>
```
It prompted for a passphrase, so I entered `pAzzword`. The extraction succeeded, and a flag file was produced. Opening that file revealed the flag.
