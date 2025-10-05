# TITLE : vault-door-8
## Author : Mark E. Haase
## Description
Apparently Dr. Evil's minions knew that our agency was making copies of their source code, because they intentionally sabotaged this source code in order to make it harder for our agents to analyze and crack into! The result is a quite mess, but I trust that my best special agent will find a way to solve it. The source code for this vault is here: [VaultDoor8.java](https://jupiter.challenges.picoctf.org/static/9b13abb1479aa3979db28a9083712663/VaultDoor8.java)
## Hints 
- Clean up the source code so that you can read it and understand what is going on.
- Draw a diagram to illustrate which bits are being switched in the scramble() method, then figure out a sequence of bit switches to undo it. You should be able to reuse the switchBits() method as is.
## Solution
In this challenge we were given a Java source file. As is typical for these problems, the program contains a `checkPassword` function that defines an `expected` array:
```java
char[] expected = {
0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xE0, 0x95, 0xF1, 0xE1, 0xE0, 0xA4, 0xC0, 0x94, 0xA4 } 
```
To recover the flag, we examine how the program transforms user input. The input is passed to a `scramble()` routine that repeatedly swaps pairs of bits in each character (via `switchBits`). If the scrambled result matches the `expected` array, the password is accepted — i.e., the original input (or the substring the program extracts from it) is the flag.
