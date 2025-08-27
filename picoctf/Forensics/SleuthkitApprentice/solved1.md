# TITLE : Sleuthkit Apprentice
## Author : LT 'syreal' Jones
## Description
Download this disk image and find the flag.
Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.
[Download compressed disk image](https://artifacts.picoctf.net/c/136/disk.flag.img.gz)
## Solution
In this challenge we were given a disk image compressed with gz. First I decompressed it:
```
gunzip disk.flag.img.gz
```
Because the file is a disk image, I used Sleuth Kit to analyze it. I started by listing the partitions with:
```
mmls disk.flag.img
```
mmls showed three partitions. I examined the third partition by listing its files:
```
fls -o 360448 disk.flag.img
```
(The -o 360448 option tells Sleuth Kit to start reading the file system at sector 360448, which is where that partition begins.)
The output included the root directory and several standard directories:
```
d/d 451:        home
d/d 11: lost+found
d/d 12: boot
d/d 1985:       etc
d/d 1986:       proc
d/d 1987:       dev
d/d 1988:       tmp
d/d 1989:       lib
d/d 1990:       var
d/d 3969:       usr
d/d 3970:       bin
d/d 1991:       sbin
d/d 1992:       media
d/d 1993:       mnt
d/d 1994:       opt
d/d 1995:       root
d/d 1996:       run
d/d 1997:       srv
d/d 1998:       sys
d/d 2358:       swap
V/V 31745:      $OrphanFiles  
```
I listed the root directory (inode 1995) with:
```
fls -o 360448 disk.flag.img 1995
```
Inside root I found a directory my_folder (inode 3981), so I listed that:
```
fls -o 360448 disk.flag.img 3981
```
The output showed two files:
```
r/r * 2082(realloc):    flag.txt    
r/r 2371:               flag.uni.txt   
```
I recovered the regular file flag.uni.txt:
```
icat -o 360448 disk.flag.img 2371 > flag.txt
```
Then open the flag.txt, and you get the flag.
