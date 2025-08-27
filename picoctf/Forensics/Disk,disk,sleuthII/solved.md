# TITLE : Disk, disk, sleuth! II
## Author : syreal
## Description
All we know is the file with the flag is named `down-at-the-bottom.txt`... Disk image: [dds2-alpine.flag.img.gz](https://mercury.picoctf.net/static/aed64c508175df5fe23207c10e0e47e5/dds2-alpine.flag.img.gz)
## Hints
- The sleuthkit has some great tools for this challenge as well.
- Sleuthkit docs here are so helpful: TSK Tool Overview
- This disk can also be booted with qemu!
## Solution
In this challenge, we were given a .gz file. I first extracted it using gunzip.
Next, I ran the following command to check the partition layout inside the image:
```
mmls <imagename>
```
From the output, I noted the position of the Linux partition. To view its contents, I used:
```
fls -o 2048 <imagename>
```
In the listing, I found the root directory with inode 18290. To explore it, I ran:

```
fls -o 2048 <imagename> 18290
```
Inside, I discovered the flag file. To read its contents, I used:
```
icat -o 2048 <imagename> 18291
```
This revealed the flag. ✅
