# TITLE : ARMssembly 2
## Author : Dylan McGuire
## Description
What integer does this program print with argument 4189673334? File: [chall_2.S](https://mercury.picoctf.net/static/5c0f1b8d9f0656c228ea0adb62cd5fbf/chall_2.S) Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
## Hints
-  Loops
## Solution
In this challenge, we got a assemble source again. So i compile it using below command.
```bash
aarch64-linux-gnu-as -o chall.o chall_2.S
aarch64-linux-gnu-gcc -static -o chall chall.o
```
Then i opened Ghidra to analyze the binary file. After opening the binary file in Ghidra for analysis, I found two functions: `main` and `func1`.
In `func1`, the argument is processed in a loop as shown below:
```c
int func1(uint param_1)

{
  undefined4 local_8;
  undefined4 local_4;
  
  local_8 = 0;
  for (local_4 = 0; local_4 < param_1; local_4 = local_4 + 1) {
    local_8 = local_8 + 3;
  }
  return local_8;
}
```
In this function, `local_8` increases by 3 on every loop iteration.
Since `param_1` is a very large number, the result eventually overflows the 32-bit integer limit.
That means when the loop finishes, `local_8` does not contain the full value you’d expect — instead, it’s effectively the result modulo 2³².

We can calculate it as:
```
12,569,020,002 mod 4,294,967,296 = 3979085410
```
Finally, convert that result to hexadecimal, and you’ll get the flag.
