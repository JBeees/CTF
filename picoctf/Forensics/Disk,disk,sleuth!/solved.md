# TITLE : Disk, disk, sleuth!
## Author : syreal
## Description 
Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image: dds1-alpine.flag.img.gz
## Hints
- Have you ever used `file` to determine what a file was?
- Relevant terminal-fu in picoGym: https://play.picoctf.org/practice/challenge/85
- Mastering this terminal-fu would enable you to find the flag in a single command: https://play.picoctf.org/practice/challenge/48
- Using your own computer, you could use qemu to boot from this disk!
## Solution
In this challenge, the description mentioned using `srch_strings`. First, I extracted the .gz file with gunzip. Then, I used srch_strings to search for text within the image file. I specifically looked for the keyword "pico", and that’s how I found the flag.

The command I used was:
```
srch_strings dds1-alpine.flag.img | grep pico
```

