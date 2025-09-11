# TITLE : Picker I
## Author : LT 'syreal' Jones
## Description
This service can provide you with a random number, but can it do anything else?
Connect to the program with netcat:
$ nc saturn.picoctf.net 65498
The program's source code can be downloaded here.
## Hints
- Can you point the program to a function that does something useful for you?
## Solutioin
In this challenge, the program allows us to execute any function that exists within it. There is a `win` function that outputs the flag. When I executed `win`, it returned the flag as a hexadecimal value. After decoding the hex, I obtained the actual flag.
