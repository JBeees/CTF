# TITLE : Operation Orchid
## Author : LT 'syreal' Jones
## Description
Download this disk image and find the flag.
Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.
- [Download compressed disk image](https://artifacts.picoctf.net/c/212/disk.flag.img.gz)
## Solution
We were given a .gz file. First, I decompressed it with gunzip to obtain a disk image. I used Sleuth Kit to analyze the image. Running `mmls disk.flag.img` showed three partitions; the third partition (which contained the root filesystem) started at sector 411648. To list the root directory I used:
```bash
fls -o 411648 disk.flag.img
```
The output showed a root directory inode 472. To list the contents of that inode I ran:
```bash
fls -o 411648 disk.flag.img 472
```
The directory contained these entries:
```
r/r 1875:       .ash_history
r/r * 1876 (realloc): flag.txt
r/r 1782:       flag.txt.enc
```
I look at the .ash_history file to see what commands had been run:
```bash
icat -o 411648 disk.flag.img 1875
```
The .ash_history revealed the following sequence of commands, which documented how the flag was created and encrypted:
```
touch flag.txt
nano flag.txt
apk add nano
nano flag.txt
openssl enc -aes-256-cbc -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567
shred -u flag.txt
ls -al
halt
```
Next, I extracted the encrypted flag from the image:
```bash
icat -o 411648 disk.flag.img 1782 > flag.txt
```
Then I decrypted the file using the same cipher and password shown in the history:
```bash
openssl aes256 -d -salt -in flag.txt -out dec.txt -k unbreakablepassword1234567
```
I opened dec.txt and retrieved the flag.
