# TITLE : Blank Page
## Author : Haker
## Description
I've just graduated the Super Agent School. This is my first day as a spy. The Master-Mind sent me the secret message, but I don't remember how to read this. Help!
## Solution
In this challenge, we were given a .txt file that appeared to be completely blank when opened. Suspecting hidden data, I examined the file with xxd, and found that it contained only whitespace-like characters.
Upon closer inspection, the file used two different types of spaces:
- Normal space (0x20)
- EM SPACE (U+200f, UTF-8 e2 80 8f)
These were being used to encode binary data.
1. Identify which characters represent binary values. For example:
    - Normal space (0x20) = 0
    - EM SPACE (U+200f) = 1
      (or reversed, depending on the challenge)
2. Convert the sequence of characters into a binary string.
3. Split the binary string into 8-bit chunks, then convert each chunk to its corresponding ASCII character.
```py
with open("TheMessage.txt", "r", encoding="utf-8") as f:
    data = f.read()

binary = ""
for ch in data:
    if ch == " ":         # normal space
        binary += "0"
    elif ch == "\u200f":  # EM SPACE
        binary += "1"

# split into bytes
message = "".join(
    chr(int(binary[i:i+8], 2))
    for i in range(0, len(binary), 8)
)

print(message)
```
run it will reveal the flag.
