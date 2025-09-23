# TITLE : Bit-O-Asm-3
## Author : LT 'syreal' Jones
## Description
Can you figure out what is in the eax register? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}.
Download the assembly dump [here](https://artifacts.picoctf.net/c/511/disassembler-dump0_d.txt).
## Hints
- Don't tell anyone I told you this, but you can solve this problem without understanding the compare/jump relationship.
- Of course, if you're really good, you'll only need one attempt to solve this problem.
## Solution
n this challenge we were asked to determine the value of the eax register. Looking at the disassembly, we see the following instructions:
```asm
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    cmp    DWORD PTR [rbp-0x4],0x2710
<+29>:    jle    0x55555555514e <main+37>
<+31>:    sub    DWORD PTR [rbp-0x4],0x65
<+35>:    jmp    0x555555555152 <main+41>
<+37>:    add    DWORD PTR [rbp-0x4],0x65
<+41>:    mov    eax,DWORD PTR [rbp-0x4]
```
Step-by-step analysis:

At <+15>, the program stores 0x9fe1a (decimal 654874) into [rbp-0x4].

At <+22>, it compares [rbp-0x4] with 0x2710 (decimal 10000).

If [rbp-0x4] <= 10000, execution jumps to <+37> and adds 0x65 (decimal 101).

Otherwise ([rbp-0x4] > 10000), it executes <+31> and subtracts 0x65.

Finally, the result is moved into eax.

Since the initial value 0x9fe1a = 654874 is much larger than 10000, the subtraction path is taken:
```asm
eax = 0x9fe1a - 0x65
```
From the result above convert it to decimal and you will get the flag.
