# TITLE : unpackme 
## Author : LT 'syreal' Jones
## Description
Can you get the flag?
Reverse engineer this [binary](https://artifacts.picoctf.net/c/205/unpackme-upx).
## Hints
- What is UPX?
## Solution
In this challenge we were given a binary file that was packed with **UPX**. If you try to decompile a UPX-packed binary directly, you usually only see the packer stub (the decompression code) and not the actual program logic. Therefore we need to unpack the binary first:
```bash
upx -d <fileName>
```
After unpacking, I loaded the binary into **Ghidra** and decompiled it. I found the following main function:
```c
undefined8 main(void)

{
  long in_FS_OFFSET;
  int local_44;
  char *local_40;
  undefined8 local_38;
  undefined8 local_30;
  undefined8 local_28;
  undefined4 local_20;
  undefined2 local_1c;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_38 = 0x4c75257240343a41;
  local_30 = 0x30623e306b6d4146;
  local_28 = 0x6865666430486637;
  local_20 = 0x36636433;
  local_1c = 0x4e;
  printf("What\'s my favorite number? ");
  __isoc99_scanf(&DAT_004b3020,&local_44);
  if (local_44 == 0xb83cb) {
    local_40 = (char *)rotate_encrypt(0,&local_38);
    fputs(local_40,(FILE *)stdout);
    putchar(10);
    free(local_40);
  }
  else {
    puts("Sorry, that\'s not it!");
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```
Explanation 
- The program prints What's my favorite number? and reads an integer into local_44.
-  It then checks:
```c
if (local_44 == 0xb83cb)
```
- 0xb83cb in decimal is 754,635.
- If the value matches, the program calls rotate_encrypt(0, &local_38), which likely decodes or decrypts a hidden string (the flag). The result is printed with fputs, followed by a newline, and the allocated memory is freed.
- If the input is incorrect, the program prints: Sorry, that's not it!
I ran the unpacked binary, entered `754635`, and the program printed the flag.
