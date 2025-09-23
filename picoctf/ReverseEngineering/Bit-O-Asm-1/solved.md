## TITLE : Bit-O-Asm-1
## Author : LT 'syreal' Jones
## Description
Can you figure out what is in the eax register? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}.
Download the assembly dump here.
## Hints
- As with most assembly, there is a lot of noise in the instruction dump. Find the one line that pertains to this question and don't second guess yourself!
## Solution
In this challenge we were asked to find the value stored in the `eax` register. I inspected the disassembly and found the instruction:
```asm
<+15>:    mov    eax,0x30
```
That instruction sets `eax` to 0x30. Converting the hexadecimal value 0x30 to decimal gives 48, so the flag is 48.
