# TITLE : Operation Oni
## Author : LT 'syreal' Jones
## Description
Download this disk image, find the key and log into the remote machine.
Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.
Download disk image
Remote machine: ssh -i key_file -p 59401 ctf-player@saturn.picoctf.net
## Solution
In this challenge, I was given a .gz file. First, I unzipped the file, which resulted in a disk image. Then, I ran the command:
```
mmls disk.img
```
to list the partitions inside the image. I found a partition starting at sector 206848, so I listed its contents with:
```
fls -o 206848 disk.img
```
This showed me the root directory. From there, I navigated deeper by running fls again on the root directory entry. Inside the root directory, I discovered two items: a history file and an .ssh directory.
Inside the .ssh directory, I found both the public and private SSH keys. I extracted the private key to my local machine, fixed its permissions, and then used it to log in to the remote SSH server with:
```
ssh -i prikey -p 63086 ctf-player@saturn.picoctf.net
```
In the ssh you will find flag file, open it, and you will get the flag.

