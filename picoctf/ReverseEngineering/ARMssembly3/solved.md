# TITLE : ARMssembly 3
## Author : Dylan McGuire
## Description
What integer does this program print with argument 3350728462? File: [chall_3.S](https://mercury.picoctf.net/static/9f5593ecc5da7043cf69a8926efc3be8/chall_3.S) Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
## Hints 
- beep boop beep boop...
## Solution
In this challenge, we were given an assembly source file. First, I compiled it using the following commands:
```bash
aarch64-linux-gnu-as -o chall.o chall_3.S
aarch64-linux-gnu-gcc -static -o chall chall.o
```
Then, I opened the binary in **Ghidra** to analyze it. I found that the program contains `main`, `func1`, and `func2`.

In `func1`, the operations are as follows:
```c
undefined4 func1(uint param_1)

{
  undefined4 local_14;
  undefined4 local_4;
  
  local_4 = 0;
  for (local_14 = param_1; local_14 != 0; local_14 = local_14 >> 1) {
    if ((local_14 & 1) != 0) {
      local_4 = func2(local_4);
    }
  }
  return local_4;
}
```
The program doing shift operation. Then return the result, So i run my program. After i get the result from it i convert it to hex. And it will be the flag.
