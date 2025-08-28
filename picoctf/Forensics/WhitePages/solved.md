# TITLE : WhitePages
## Author : John Hammond
## Description
I stopped using YellowPages and moved onto WhitePages... but [the page they gave me](https://jupiter.challenges.picoctf.org/static/74274b96fe966126a1953c80762af80d/whitepages.txt) is all blank!
## Solution
In this challenge, we were given a .txt file that appeared to be completely blank when opened. Suspecting hidden data, I examined the file with xxd, and found that it contained only whitespace-like characters.
Upon closer inspection, the file used two different types of spaces:
- Normal space (0x20)
- EM SPACE (U+2003, UTF-8 e2 80 83)
These were being used to encode binary data.
1. Identify which characters represent binary values. For example:
    - Normal space (0x20) = 1
    - EM SPACE (U+2003) = 0
      (or reversed, depending on the challenge)
2. Convert the sequence of characters into a binary string.
3. Split the binary string into 8-bit chunks, then convert each chunk to its corresponding ASCII character.
```python
with open("whitepages.txt", "r", encoding="utf-8") as f:
    data = f.read()

binary = ""
for ch in data:
    if ch == " ":
        binary += "1"
    elif ch == "\u2003":
        binary += "0"

flag = "".join(
    chr(int(binary[i:i+8], 2))
    for i in range(0, len(binary), 8)
)

print(flag)
```
✅ Running this script decoded the whitespace into readable text, which revealed the flag.
