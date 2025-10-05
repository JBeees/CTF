# TITLE : asm2
## Author : Sanjay C
## Description
What does asm2(0x4,0x2d) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://jupiter.challenges.picoctf.org/static/ceac75672637589213b952abe32c84b3/test.S)
## Hints 
- assembly conditions
## Solution
In this challenge, we’re given an assembly file. The program takes two arguments, as described in the task. At the end, it asks for the value of `EAX`.

After analyzing the code, I found that the program executes a loop until a certain condition is met. Logically, it can be represented as:
```c
int asm2(int a, int b) {
    while (a <= 0x5fa1) {
        b += 1;
        a += 0xd1;
    }
    return b;
}
```
Once the loop finishes, the value stored in `EAX` (in hexadecimal format) becomes the flag.
