# TITLE : Pho Is Tasty!
## Author : kcbowhunter
## Description
The flag is hidden in the jpeg file. Good Luck! Have some Pho! Solve this challenge before solving my Scope challenge for 100 points.
## Solution 
In this challenge, we were given a JPG file. As an initial step, I examined the file’s hex header using the following command:
```
xxd <file_name> | head
```
This command displays the first few bytes of the file in hexadecimal format. While inspecting the header output, I found the flag embedded directly in the file, allowing me to solve the challenge without further analysis.
