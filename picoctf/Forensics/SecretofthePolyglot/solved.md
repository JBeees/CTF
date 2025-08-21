# TITLE : Secret of the Polyglot
## Author : syreal
## Description
The Network Operations Center (NOC) of your local institution picked up a suspicious file, they're getting conflicting information on what type of file it is. They've brought you in as an external expert to examine the file. Can you extract all the information from this strange file?
Download the suspicious file [here](https://artifacts.picoctf.net/c_titan/96/flag2of2-final.pdf).
## Hints
- This problem can be solved by just opening the file in different ways
## Solution
To solve this challenge, I first examined the file in hex using the xxd tool. From the hex dump, I noticed that the file header indicated it was actually a .png file instead of a .pdf. After changing the extension to .png, I was able to extract the first part of the flag.

The second part of the flag was still inside the original .pdf file. By combining both parts, I obtained the full flag.

