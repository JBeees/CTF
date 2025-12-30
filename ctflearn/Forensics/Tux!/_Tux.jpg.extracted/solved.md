# TITLE : Tux!
## Author : kcbowhunter
## Description
The flag is hidden inside the Penguin! Solve this challenge before solving my 100 point Scope challenge which uses similar techniques as this one.
## Solution
In this challenge, we were given a JPG file. I first inspected the image metadata using `exiftool` and found a Base64-encoded string in the `comment` field. After decoding it, the string revealed a password.

Next, I used `binwalk` to extract files embedded within the image, which produced a ZIP archive. Using the recovered password, I successfully extracted the ZIP file. Inside the extracted contents, there was a file containing the flag. Opening this file revealed the final flag.
