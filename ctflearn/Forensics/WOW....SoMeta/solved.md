# TITLE : Wow.... So Meta
## Author : 3301_
## Description
This photo was taken by our target. See what you can find out about him from it.
## Solution
In this challenge, we were given a JPG file. Since the challenge referenced metadata, I analyzed the image using `exiftool`. Within the metadata, I found the flag stored in the `Camera Serial Number` field. After wrapping it in the `CTFlearn{...}` format, the submission was accepted.
