# TITLE : hideme
## Author : Geoffrey Njogu
## Description
Every file gets a flag.
The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye [here](https://artifacts.picoctf.net/c/261/flag.png).
## Solution
In this challenge, we were given a .png image. The first thing I did was run ExifTool on the image, which gave the following warning:
```
Warning: [minor] Trailer data after PNG IEND chunk
```
This indicated that there might be additional data hidden inside the image file. To investigate further, I used binwalk with the command:
```
binwalk -e <filename>
```
Binwalk successfully extracted hidden files into a new directory. Inside the extracted data, I found a folder named secret, which contained a file called flag.png. After opening flag.png, the flag was clearly visible on the image.
