# TITLE : GDB Test Drive
## Author : LT 'syreal' Jones
## Description
Can you get the flag?
Download this [binary](https://artifacts.picoctf.net/c/85/gdbme).
Here's the test drive instructions:
```asm
$ chmod +x gdbme
$ gdb gdbme
(gdb) layout asm
(gdb) break *(main+99)
(gdb) run
(gdb) jump *(main+104)
```
## Solution
I was given a binary for a CTF challenge and began the analysis in Ghidra. In `main` I found the following relevant excerpt:
```c
undefined8 main(void)

{
  char *__s;
  long in_FS_OFFSET;
  undefined8 local_38;
  undefined8 local_30;
  undefined8 local_28;
  undefined8 local_20;
  undefined1 local_18;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_38 = 0x4c75257240343a41;
  local_30 = 0x4362383846336235;
  local_28 = 0x6030624760433530;
  local_20 = 0x4e32676662346668;
  local_18 = 0;
  sleep(100000);
  __s = (char *)rotate_encrypt(0,&local_38);
  fputs(__s,stdout);
  putchar(10);
  free(__s);
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```
The flag is stored across the `local_38`, `local_30`, `local_28`, and `local_20` variables; together they form a null-terminated string on the stack. That string is passed to `rotate_encrypt`, which applies a rotation cipher and returns the printable flag. However, execution in main calls `sleep(100000)`, which would pause the binary for roughly **100,000 seconds** (≈ 1 day, 3 hours, and 46 minutes) before reaching `rotate_encrypt`. The challenge description therefore instructs you to set the instruction pointer to `main+104` to skip the sleep call and continue execution directly to the deobfuscation routine — doing so reveals the flag immediately. Following that instruction yields the flag.
