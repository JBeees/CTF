# TITLE : extensions
## Author : Sanjay C/Danny
## Description
This is a really weird text file TXT? Can you find the flag?
## Hints
- How do operating systems know what kind of file it is? (It's not just the ending!
- Make sure to submit the flag as picoCTF{XXXXX}
## Solution
In this challenge, we were given a .txt file. I examined it using the `file <filename>` command and discovered that it was actually a PNG image. To view it properly, I renamed the file extension from .txt to .png using the command:
```
mv flag.txt flag.png
```
After changing the extension, I was able to open the image and retrieve the flag.
