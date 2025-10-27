# TITLE : PW Crack 1
## Author : LT 'syreal' Jones
## Description
Can you crack the password to get the flag?
Download the password checker [here](https://artifacts.picoctf.net/c/10/level1.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/10/level1.flag.txt.enc)in the same directory too.
## Hints
- To view the file in the webshell, do: `$ nano level1.py`
- To exit nano, press `Ctrl` and `x` and follow the on-screen prompts.
- The `str_xor` function does not need to be reverse engineered for this challenge.
## Solution
In this challenge we were given a Python file and an encrypted flag `flag_enc`. Inspecting the script I found this function:
```py
def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "691d"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")
```
I ran the script, entered `691d` when prompted, and the script returned the flag by XOR-decrypting `flag_enc` with the password via `str_xor`.
