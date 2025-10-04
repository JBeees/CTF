# TITLE : ARMssembly 4
## Author : Dylan McGuire
## Description
What integer does this program print with argument 3251372985? File: [chall_4.](https://mercury.picoctf.net/static/fbb182234c0fd8d12dd14e6a070d4b45/chall_4.S) Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
## Hints
- Switching things up
## Solution
I was given an **AArch64 assembly source file** and needed to cross-compile it on an x86_64 machine. I assembled the source and linked it with the GNU AArch64 toolchain, then executed the resulting binary under QEMU user-mode emulation. After running the program with the required arguments, I converted the program output to hexadecimal and formatted the result according to the challenge specification; that produced the flag. Below is the command 
```asm
aarch64-linux-gnu-as -o chall.o chall.S
aarch64-linux-gnu-gcc -static -o chall chall.o
sudo apt install qemu-user-static
```
