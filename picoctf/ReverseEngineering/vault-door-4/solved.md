# TITLE : vault-door-4
## Author : Mark E. Haase
## Description
This vault uses ASCII encoding for the password. The source code for this vault is here: [VaultDoor4.java](https://jupiter.challenges.picoctf.org/static/c695ee23309d453a3ef369c34cc1bccb/VaultDoor4.java)
## Hints
- Use a search engine to find an "ASCII table".
- You will also need to know the difference between octal, decimal, and hexadecimal numbers.
## Solution
In this challenge we were given a Java file. To get the flag we found a `byte[] myBytes` containing a mix of decimal, hex, and octal values. Interpreting each value as an ASCII character produced the flag string.
