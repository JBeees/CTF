# TITLE : asm1
## Author Sanjay C
## Description
What does asm1(0x2e0) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://jupiter.challenges.picoctf.org/static/f1c2358ff7d1e9386e41552c549cf2f6/test.S)
## Hints
- assembly conditions
## Solution
In this challenge we have an assembly file. The function is called with the argument `0x2e0`, which the code stores at `DWORD PTR [ebp-0x8]`. Follow the conditional logic in the function; the final value returned in `EAX` is the flag (submit it as a hexadecimal value, without any picoCTF wrapper).
