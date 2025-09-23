# TITLE : ARMssembly 0
## Author : Dylan McGuire
## Description
What integer does this program print with arguments 4112417903 and 1169092511? File: [chall.S](https://mercury.picoctf.net/static/55a414fdd81f39784d662e8023c5aeb8/chall.S) Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
## Hints 
- Single Compare
## Solution
I was given an **ARMv8** (AArch64) assembly source and assembled it with the cross toolchain:
```bash
aarch64-linux-gnu-gcc -c chall.S -o chall.o
aarch64-linux-gnu-gcc chall.S -o chall
```  
I loaded the resulting ELF into **Ghidra** and found the main function. It reads two command-line arguments, converts them to integers, passes them to `func1`, and prints the result:
```
undefined8 main(undefined8 param_1,long param_2)

{
  int iVar1;
  int iVar2;
  ulong uVar3;
  
  iVar1 = atoi(*(char **)(param_2 + 8));
  iVar2 = atoi(*(char **)(param_2 + 0x10));
  uVar3 = func1(iVar1,iVar2);
  printf("Result: %ld\n",uVar3 & 0xffffffff);
  return 0;
}
```
The `func1` implementation is:
```c
uint func1(uint param_1,uint param_2)

{
  if (param_2 < param_1) {
    param_2 = param_1;
  }
  return param_2;
}
```
So `func1` returns the maximum of the two unsigned parameters. Therefore, `uVar3` will be the larger of the two arguments passed on the command line. The flag is in description format.
