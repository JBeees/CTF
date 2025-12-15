# TITLE : Pitter, Patter, Platters
## Author : SYREAL
## Description
'Suspicious' is written all over this disk image.
Download [suspicious.dd.sda1](https://challenge-files.picoctf.net/c_shape_facility/004d4e9345d26e6054e3971df0e1efcfbea71ef7bf659bdc30bfd8a78726c85b/suspicious.dd.sda1)
## Hints
- It may help to analyze this image in multiple ways: as a blob, and as an actual mounted disk.
- Have you heard of slack space? There is a certain set of tools that now come with Ubuntu that I'd recommend for examining that disk space phenomenon...
## Solution
In this challenge, we were given a disk image formatted with ext3. I began the analysis using The Sleuth Kit to enumerate the filesystem contents:
```
fls <disk_name>
```
The output was
```
d/d 11:	lost+found
d/d 2009:	boot
d/d 4017:	tce
r/r 12:	suspicious-file.txt
V/V 8033:	$OrphanFiles
```
From this listing, the file `suspicious-file.txt` (inode 12) stood out as potentially relevant. I then examined its contents using:
```
icat <disk_name> 12
```
The file contained the following line:
```
Nothing to see here! But you may want to look here -->
```
Based on the challenge hints, this suggested that the interesting data was not in the file’s logical content, but elsewhere. Since the filesystem is ext3, this pointed to slack space analysis.

Slack space is unused space at the end of the last allocated disk cluster for a file, which may still contain leftover data from previously stored files.
To extract the slack space associated with suspicious-file.txt, I used:
```
icat -s <disk_name> 12
```
This command extracts only the slack space of the file. In the output, I found the flag, but it was stored in a reversed (flipped) form. Reversing the extracted data revealed the correct flag.
