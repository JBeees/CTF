# TITLE : Rubber Duck
## Author : kcbowhunter
## Description
Find the flag! Simple forensics challenge to get started with.
## Solution
In this challenge, we were given a JPG file. Since the challenge referenced metadata, I analyzed the image using `exiftool`. Within the metadata, I found the flag stored in the `Comment` field. After wrapping it in the `CTFlearn{...}` format, the submission was accepted.
