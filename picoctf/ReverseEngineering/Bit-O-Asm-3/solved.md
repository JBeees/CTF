# TITLE : Bit-O-Asm-3
## Author : LT 'syreal' Jones
## Description
Can you figure out what is in the eax register? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}.
Download the assembly dump [here](https://artifacts.picoctf.net/c/530/disassembler-dump0_c.txt).
## Hints
- Not everything in this disassembly listing is optimal.
## Solution
In this challenge we were asked to determine the value of the eax register. Looking at the disassembly, we find:
```asm
<+15>:    mov    DWORD PTR [rbp-0xc],0x9fe1a
<+22>:    mov    DWORD PTR [rbp-0x8],0x4
<+29>:    mov    eax,DWORD PTR [rbp-0xc]
<+32>:    imul   eax,DWORD PTR [rbp-0x8]
<+36>:    add    eax,0x1f5
<+41>:    mov    DWORD PTR [rbp-0x4],eax
<+44>:    mov    eax,DWORD PTR [rbp-0x4]
<+47>:    pop    rbp
<+48>:    ret
```
Here’s what happens step by step:

- 0x9fe1a is stored at [rbp-0xc].
- 0x4 is stored at [rbp-0x8].
- eax is loaded with 0x9fe1a.
- eax is multiplied by 0x4.
- 0x1f5 is added to eax.
So the final computation is:
```asm
eax = (0x9fe1a × 0x4) + 0x1f5
```
Calculate this and convert it to decimal will give you the flag.
