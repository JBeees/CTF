# TITLE : Picker II
## Author : LT 'syreal' Jones
## Description
Can you figure out how this program works to get the flag?   
Connect to the program with netcat:   
$ nc saturn.picoctf.net 49476   
The program's source code can be downloaded here.   
## Hints
- Can you do what win does with your input to the program?
## Solution
This challenge is similar to Picker I, but this time the program prevents direct access to the `win` function by using a filter. You can bypass this restriction by using `globals()` and constructing the function name with ASCII codes, like this:
```python
globals()[chr(119)+chr(105)+chr(110)]
```
This will return the hexadecimal representation of the flag. Decode it, and you will get the actual flag.
