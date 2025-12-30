# TITLE : I'm a Dump
## Author : lancillotto
## Description
The keyword is hexadecimal, and removing an useless H.E.H.U.H.E. from the flag. The flag is in the format CTFlearn{}
## Solution
In this challenge, we were given a binary file. When I attempted to execute it, the program produced no output. I then analyzed the binary using the `strings` command, which revealed the flag embedded in the file. The final step was to remove the char `H` from the extracted string to obtain the correct flag.
