# TITLE : not crypto
## Author : asphyxia
## Description
there's crypto in here but the challenge is not crypto... 🤔
## Solution
In this challenge we were given a binary that checks our input against the real flag using `memcmp`. Because the binary performs several transformations on the input before comparing, I used static and dynamic analysis to find the comparison site and inspect the values being compared.

First I opened the binary in **Ghidra** to locate interesting functions and to understand the overall control flow. Then I launched **GDB** and listed available functions with:
```
info functions
```
I saw `memcmp` in the function list, so I set a breakpoint on it to catch every comparison the program makes:
```
break memcmp
```
Then I ran the program:
```
run
```
When execution stopped at the breakpoint, I inspected the first argument register (rdi), which points to the first buffer compared by memcmp—the processed version of the user input.
To view the full string stored at that memory location, I used:
```
x/s $rdi
```
This revealed the entire flag
