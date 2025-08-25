# TITLE : Sleuthkit Intro
## Author : LT 'syreal' Jones
## Description
Download the disk image and use mmls on it to find the size of the Linux partition. Connect to the remote checker service to check your answer and get the flag.
Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.
[Download disk image](https://artifacts.picoctf.net/c/164/disk.img.gz)
Access checker program: nc saturn.picoctf.net 49526
## Solution
In this challenge, I first decompressed the .gz file using gunzip. Next, I used the `mmls` tool to analyze the disk image and obtained partition information. Then, I ran the provided checker program and entered the requested input. Finally, I received the flag.
