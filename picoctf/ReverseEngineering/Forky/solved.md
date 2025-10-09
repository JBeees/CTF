# TITLE : Forky
## Author : SAMUEL
## Description
In this program, identify the last integer value that is passed as parameter to the function doNothing().
## Hints
- What happens when you fork? The flag is picoCTF{IntegerYouFound}. For example, if you found that the last integer passed was 1234, the flag would be picoCTF{1234}
## Solution
In this challenge, we are given a binary file. I opened it directly in **Ghidra** for analysis and found the following `main` function:
```c
undefined4 main(void){
  int *piVar1;
  
  piVar1 = (int *)mmap((void *)0x0,4,3,0x21,-1,0);
  *piVar1 = 1000000000;
  fork();
  fork();
  fork();
  fork();
  *piVar1 = *piVar1 + 0x499602d2;
  doNothing(*piVar1);
  return 0;
}
```
### **Analysis**

- The program calls `fork()` four times sequentially.
- Each `fork()` duplicates all existing processes. So the total number of processes after each fork is:
| Fork | Total Processes |
|------|----------------|
| 1st  | 2              |
| 2nd  | 4              |
| 3rd  | 8              |
| 4th  | 16             |
- All 16 processes share the same memory because `piVar1` points to a shared anonymous memory region (MAP_SHARED).
- At the end, every process executes:
```c
*piVar1 = *piVar1 + 0x499602d2;
```
- If all increments were applied without race conditions, the total value would be:
```c
*piVar1 = 1000000000 + 16 * 0x499602d2
```
- Since this exceeds the 32-bit signed integer limit, it overflows.
### **Handling Overflow**
- The actual behavior in memory is equivalent to modulo 2^32
```
overflowed value = (1000000000 + 16⋅0x499602d2) mod 2^32
```
- To interpret it as a signed 32-bit integer, subtract 2^32 if the result is larger than 2^32 - 1
- This final signed integer is the flag.
