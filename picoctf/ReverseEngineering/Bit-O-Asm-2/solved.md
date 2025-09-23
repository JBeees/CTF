# TITLE : Bit-O-Asm-2
## Author :  LT 'syreal' Jones
## Description
Can you figure out what is in the eax register? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}.
Download the assembly dump [here](https://artifacts.picoctf.net/c/510/disassembler-dump0_b.txt).
## Hints
- PTR's or 'pointers', reference a location in memory where values can be stored.
## Solution
In this challenge we were asked to determine the value stored in the `eax` register. Looking at the disassembly, I found the following instructions:
```asm
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    mov    eax,DWORD PTR [rbp-0x4]
```
From this code, we can see that `0x9fe1a` is first stored at `[rbp-0x4]`. Then, the second instruction moves the value from `[rbp-0x4]` into `eax`.
Therefore, the value of `eax` is `0x9fe1a`.

Converting `0x9fe1a` to decimal gives **654874**, which is the flag.
