# TITLE : PW Crack 2
## Author : LT 'syreal' Jones
## Description
Can you crack the password to get the flag?
Download the password checker [here](https://artifacts.picoctf.net/c/15/level2.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/15/level2.flag.txt.enc) in the same directory too.
## Hints
- Does that encoding look familiar?
- The str_xor function does not need to be reverse engineered for this challenge
## Solution
In this challenge we were given a Python file and an encrypted flag `flag_enc`. Inspecting the script I found this function:
```py
def level_2_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    print(chr(0x33)+chr(0x39)+chr(0x63)+chr(0x65))
    if( user_pw == chr(0x33) + chr(0x39) + chr(0x63) + chr(0x65) ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")
```
The four `chr()` calls produce the string `39ce`. I ran the script, entered `39ce` when prompted, and the script used str_xor with that password to decrypt `flag_enc` and printed the flag.
