# TITLE : ARMssembly1
## Author : Pranay Garg
## Description
For what argument does this program print `win` with variables 85, 6 and 3? File: chall_1.S Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
## Hints
- Shifts
## Solution
In this challenge, we are given an assembly source file. First, I compiled it with the following commands:
```bash
aarch64-linux-gnu-gcc -c chall_1.S  -o chall_1.o
aarch64-linux-gnu-gcc chall_1.o -o chall
```
After compiling, I opened the binary in Ghidra to analyze it. Inside, I found the `main` function, which takes two arguments, and a function named `func`, which processes the second argument to determine the win condition.

Here is the decompiled content of `func`:
```c
int func(int param_1){
  return 0x715 - param_1;
}
```
To reach the win condition, `func` must return `0`. That means the input `param_1` must be exactly `0x715`. In decimal, that value is `1813`. This is the value you need to provide as the argument to trigger the **"You win!"** message.

Don’t forget to follow the specific instructions from the challenge description when providing the input.
