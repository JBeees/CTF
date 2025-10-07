# TITLE : asm4
## Author : Sanjay C
## Description
What will asm4("picoCTF_a3112") return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://jupiter.challenges.picoctf.org/static/80186ad81f4a1569b480e7fbf68b29ca/test.S)
## Hints
- Treat the Array argument as a pointer
## Solution
In this challenge, just like the previous one, we were given an assembly source file. I opened ChatGPT and asked it to analyze the code, and it explained that the assembly corresponds to the following C program:
```c
int asm4(char *s)
{
    int acc = 0x246;   // 0x246 = 582 decimal
    int len = 0;
    while (s[len] != '\0')
        len++;

    for (int j = 1; j < len - 1; j++) {
        acc = acc + (s[j] - s[j-1]) + (s[j+1] - s[j]);
    }

    return acc;
}
```
After inserting the given string argument into the function, I calculated the final value of `acc`. Then, I converted that value to hexadecimal — and that hexadecimal result turned out to be the flag.
