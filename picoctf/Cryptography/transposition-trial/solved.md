# TITLE : transposition-trial
## Author : Will Hong
## Description
Our data got corrupted on the way here. Luckily, nothing got replaced, but every block of 3 got scrambled around! The first word seems to be three letters long, maybe you can use that to recover the rest of the message.
Download the corrupted message [here](https://artifacts.picoctf.net/c/192/message.txt).
## Hints
Split the message up into blocks of 3 and see how the first block is scrambled
## Solution
To solve this challenge, the flag is given in a scrambled form.
Rearrange it by processing the text in 3-letter chunks:

- For each chunk, move the last letter to the front, then append the first two letters. Example: het → the

Apply this to every 3-letter block in sequence to recover the flag.
