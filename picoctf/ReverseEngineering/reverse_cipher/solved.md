# TITLE : reverse_cipher
## Author : Danny Tunitis
## Description
We have recovered a [binary](https://jupiter.challenges.picoctf.org/static/48babf8f8c4c6b8baf336680ea5b9ddf/rev) and a [text file](https://jupiter.challenges.picoctf.org/static/48babf8f8c4c6b8baf336680ea5b9ddf/rev_this). Can you reverse the flag.
## Hints
- objdump and Gihdra are some tools that could assist with this
## Solution
In this challenge we have a binary that writes a reversed flag. I analyzed the program with **Ghidra** and found the following loop in main where the flag is processed:
```c
  for (i = 8; (int)i < 0x17; i = i + 1) {
     if ((i & 1) == 0) {
        temp_char = copy_flag[(int)i] + '\x05';
     }
     else {
        temp_char = copy_flag[(int)i] + -2;
     }
     fputc((int)temp_char,rev_flag);
  }
```
This loop iterates i from 8 to 22 (inclusive). For each `i`:
- If `i` is even, the program adds 5 to the character (+ 0x05).
- If `i` is odd, the program subtracts 2 (- 2).

The resulting character is written to the output file `rev_flag`.
To reverse this transformation for a given mapped string, you must undo those operations and you must compute even/odd based on the original `i` value that starts at 8. Therefore:

- If `i` is even → reverse by subtracting 5.
- If `i` is odd → reverse by adding 2.
```py
def map_text(text):
    result = ""
    i = 0
    for ch in text:
        if (i % 2 == 0):
            result += chr((ord(ch) - 5) % 256)
        else:
            result += chr((ord(ch) + 2) % 256)
        i+=1
    return result

text = "w1{1wq8/7376j.:"

res = map_text(text)

print("Original  :", text)
print("Result", res)
```
The result will be the flag.
