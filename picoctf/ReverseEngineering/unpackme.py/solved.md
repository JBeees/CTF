# TITLE : unpackme.py
## Author : LT 'syreal' Jones
## Description
Can you get the flag?
Reverse engineer this [Python program](https://artifacts.picoctf.net/c/50/unpackme.flag.py).
## Solution
In this challenge we were given a Python file. When I run it, it asks for a password. The program uses Fernet (and Base64) to encrypt data. I tried decrypting and printing the plain variable and obtained the flag.
