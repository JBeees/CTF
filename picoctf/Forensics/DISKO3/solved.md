# TITLE : DISKO 3
## Author : Darkraicg492
## Description
Can you find the flag in this disk image? This time, its not as plain as you think it is!
Download the disk image [here](https://artifacts.picoctf.net/c/542/disko-3.dd.gz).
## Hints
- How will you search and extract files in a partition?
## Solution
In this challenge, we were given a compressed disk image file. I first used gunzip to decompress it.
To analyze the image, I ran fls to list the files and directories inside the image:
```bash
fls disko-3.dd
```
From the output, I noticed a log directory. To look inside it, I used the inode of the directory with this command:
```bash
fls disko-3.dd 4
```
There, I found a file named flag.gz. I extracted it to my local system using:
```bash
icat disko-3.dd 522628 > flag.gz
```
When I opened flag.gz, it appeared as unreadable (compressed) data. After decompressing it with gunzip, I obtained the actual flag.
