# TITLE : fixme2.py
## Author : LT 'syreal' Jones
## Description
Fix the syntax error in the Python script to print the flag.
[Download Python script](https://artifacts.picoctf.net/c/4/fixme2.py)
## Hints
- Are equality and assignment the same symbol?
- To view the file in the webshell, do: $ nano fixme2.py
- To exit nano, press Ctrl and x and follow the on-screen prompts.
- The str_xor function does not need to be reverse engineered for this challenge.
## Solution
In this challenge, we are given a Python file. To get the flag, we just need to change the assignment operator to an equality operator in the following line:
```py
if flag = "":
```
should be changed to
```py
if flag == ""
```
After making this change, run the file again and you will get the flag.
