# TITLE : GDB baby step 2
## Author : LT 'syreal' Jones
## Description
Can you figure out what is in the eax register at the end of the main function? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}.
Debug [this](https://artifacts.picoctf.net/c/520/debugger0_b).
## Hints
- You could calculate eax yourself, or you could set a breakpoint for after the calculcation and inspect eax to let the program do the heavy-lifting for you. 
## Solution
In this challenge, we were given a binary file. I opened it in **GDB** to analyze its behavior. First, I disassembled the main function using:
```
disas main
```
Unlike the previous challenge, where the value of the eax register was directly shown (e.g., mov eax, <value>), this time the value of eax was calculated through several arithmetic operations.
To capture the final result, I set a breakpoint right before the function exits, at this instruction:
```
0x0000000000401141 <+59>:    pop    rbp
```
I set the breakpoint with:
```
break *0x401141
```
Then I ran the program:
```
run
```
Once execution stopped at the breakpoint, I checked the value of the eax register with:
```
info registers eax
```
This gave me the result in hexadecimal. Finally, I converted the hex value to decimal. The decimal result is the flag. ✅
