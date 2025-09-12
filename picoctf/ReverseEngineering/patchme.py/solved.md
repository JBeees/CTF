# TITLE : patchme.py
## Author : LT 'syreal' Jones
## Description
Can you get the flag?
Run this [Python program](https://artifacts.picoctf.net/c/200/patchme.flag.py) in the same directory as this [encrypted flag](https://artifacts.picoctf.net/c/200/flag.txt.enc).
## Solution 
We’re given a Python script that decrypts a text file. The script asks for a password at runtime; supplying the correct password will decrypt the file and reveal the flag.
Password:
```python
ak98-=90adfjhgj321sleuth9000
```
How to use it
Run the script:
```bash
python3 script.py
```
When prompted for the password, paste:
```python
ak98-=90adfjhgj321sleuth9000
```
The script will decrypt the provided text file and print the flag.
