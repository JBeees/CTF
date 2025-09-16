# TITLE : GDB baby step 1
## Author : LT 'syreal' Jones
## Description
Can you figure out what is in the eax register at the end of the main function? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}.
Disassemble [this](https://artifacts.picoctf.net/c/512/debugger0_a).
## Hints
- gdb is a very good debugger to use for this problem and many others!
- main is actually a recognized symbol that can be used with gdb commands.
## Solution
In this challenge we were given a binary and asked: what is the value of the `eax` register at the end of `main`? I debugged the file with gdb and inspected the functions:
```
gdb ./out
(gdb) info functions
```
I found main, then disassembled it:
```
(gdb) disassemble main
```
In the disassembly I saw the instruction:
```
mov    eax,0x86342
```
This instruction loads the hexadecimal value `0x86342` into `eax`. Convert it to decimal, and that is your flag.
