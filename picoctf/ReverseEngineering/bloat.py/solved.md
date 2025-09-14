# TITLE : bloat.py
## Author : LT 'syreal' Jones
## Description
Can you get the flag?
Run this [Python program](https://artifacts.picoctf.net/c/104/bloat.flag.py) in the same directory as this [encrypted flag](https://artifacts.picoctf.net/c/104/flag.txt.enc).
## Solution
In this challenge we were given a Python file. To get the flag I only had to insert the correct password. I used the value of `arg432`, which is defined in the `arg133` function. The password — `happychance` — worked, and I received the flag.
