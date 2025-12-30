# TITLE : Chalkboard
## Author : kcbowhunter
## Description
Solve the equations embedded in the jpeg to find the flag. Solve this problem before solving my Scope challenge which is worth 100 points.
## Solution
In this challenge, we were given a JPG file. I examined the file’s metadata using `exiftool` and found the flag stored in the `comment` field. However, the flag contained placeholders that required solving a math problem to determine the values of `x` and `y`. After solving the equations and substituting the correct values into the flag format, I obtained the final flag.
