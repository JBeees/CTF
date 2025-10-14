# TITLE : FANTASY CTF
## Author : SYREAL
## Description
Play this short game to get familiar with terminal applications and some of the most important rules in scope for picoCTF.
Connect to the program with netcat:
## Hints
- When a choice is presented like [a/b/c], choose one, for example: c and then press Enter.
## Solution
Connect to the target program using `nc` **(netcat)**. The program behaves like a chat application. To get the flag, follow these steps:

1. When prompted, you will see three options: a, b, and c. Choose any of them.  
2. After selecting one, repeatedly press Enter until the menu changes and shows two options: Play game and About the flag.  
3. Choose Play game.  
4. Press Enter once more.  
5. The program will then print the flag.  
