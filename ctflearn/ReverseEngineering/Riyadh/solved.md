# TITLE : Riyadh
## Author : kcbowhunter
## Description
Another entry level Reversing challenge, if you are new to Reversing you probably want to try my Reyjkavik challenge before attempting this challenge. Good Luck! The flag is hidden inside the Riyadh program. Solve the Challenge, get the flag, and I have included the encrypted sources used to create the challenge in the Riyadh.zip file. If you do to the work of solving the Challenge, I'm providing the Challenge source code (C++ and Python) if you are interested in studying the sources after solving the challenge. I think this is a great way to improve your Reversing skills when learning. Please don't share the sources or flag after you solve the challenge.
## Solution
In this challenge, we are given a binary file. I first opened it in Ghidra to analyze the code. Inside `main`, I found the following important logic:
```c
  else {
    CTFLearnHiddenFlag();
    __s2 = *(char **)(param_2 + 8);
    Msg3((char *)&buffer);
    iVar4 = strcmp((char *)&buffer,__s2);
    if (iVar4 == 0) {
                    /* You entered the wrong flag :-(
                        */
      uVar10 = 2;
      Msg4((char *)&buffer);
      puts((char *)&buffer);
    }
    else {
      sVar5 = strlen(__s2);
      if (sVar5 == 0x1e) {
        iVar4 = 0;
        pcVar6 = (char *)operator.new[](0x100);
        Msg5(pcVar6);
        lVar7 = 0;
```
This code works as follows:
1. `Msg3` constructs a fake flag and stores it in buffer.    
2. The program compares that fake flag with the user input using `strcmp`.    
3. If they match, it prints a message saying the flag is wrong.    
4. Otherwise, it checks the length of the input.     
5. If the input length is exactly `0x1e` (30 characters), it allocates memory and calls `Msg5`.
So the real logic is:
- `Msg3` → generates a fake flag
- `Msg5` → generates the real flag, but only when the input length is 30


First, I set a breakpoint on the `strcmp` call. When I ran the program, I could see the fake flag coming from `Msg3`.
Then I focused on `Msg5`.   
I set a breakpoint after the call to `Msg5` in main and ran the program with a 30-character input:
```
(gdb) break *main+151
run aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
x/s $rbp
```
At this point, $rbp contains a pointer to the buffer that `Msg5` just filled. When I printed it, GDB showed the real flag.
