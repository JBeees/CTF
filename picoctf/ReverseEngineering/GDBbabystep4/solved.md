# TITLE : GDB baby step 4
## Author : LT 'syreal' Jones
## Description
main calls a function that multiplies eax by a constant. The flag for this challenge is that constant in decimal base. If the constant you find is 0x1000, the flag will be picoCTF{4096}.
Debug [this](https://artifacts.picoctf.net/c/532/debugger0_d).
## Hints
- A function can be referenced by either its name or its starting address in gdb.
## Solution 
In this challenge, we are asked to find the constant that multiplies the value in `eax`. When I opened **GDB** and disassembled the `main` function, I noticed that it calls another function named `func1`:
```asm
0x0000000000401142 <+38>:    call   0x401106 <func1>
```
Next, I disassembled func1 and found an `imul` instruction, which performs signed integer multiplication. The instruction looks like this:
```asm
0x0000000000401114 <+14>:    imul   eax, eax, 0x3269
```
Here, `eax` is multiplied by the constant `0x3269`. Converting `0x3269` to decimal will give you the flag.
