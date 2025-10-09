# TITLE : Need For Speed
## Author : Alexander Bushkin
## Description
The name of the game is [speed](https://www.youtube.com/watch?v=8piqd2BWeGI). Are you quick enough to solve this problem and keep it above 50 mph? [need-for-speed](https://jupiter.challenges.picoctf.org/static/cd51b2c95be9f3626db6fe6665afb5a3/need-for-speed).
## Hints
- What is the final key?
## Solution
In this challenge we were given a binary that does not prompt for input and appears to enforce a time limit. I opened the binary in Ghidra and found the `main` function:
```c
undefined8 main(void){
  header();
  set_timer();
  get_key();
  print_flag();
  return 0;
}
```
`set_timer()` installs a SIGALRM handler and calls alarm(1), so the program will receive a SIGALRM after one second. That prevents us from interacting with the binary long enough to provide a key. To bypass the timer, I used GDB to stop execution before `set_timer()` was called and then jumped directly to `get_key()`.
Steps I took:

1. Start **GDB**:  
2. Set a breakpoint inside main before `set_timer` is invoked. I found the correct offset by disassembling main, then set the breakpoint:
```
break *(main+0x30)   # address offset may differ per binary; use objdump/`disas main` to find correct offset
run
```
3. Once execution stopped at that breakpoint, I transferred control directly to `get_key()`:
```
jump *(main+0x40)
```
After jumping and allowing the program to continue, I was able to run `get_key()` without `set_timer()` ever being executed, and the program printed the flag.
