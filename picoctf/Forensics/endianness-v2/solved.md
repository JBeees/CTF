# TITLE : endianness-v2
## Author : Junias Bonou
## Description
Here's a file that was recovered from a 32-bits system that organized the bytes a weird way. We're not even sure what type of file it is.
Download it [here](https://artifacts.picoctf.net/c_titan/114/challengefile) and see what you can get out of it.
## Solution
In this challenge, we were given a file that originally came from a 32-bit system. When I inspected the hex dump, the bytes appeared scrambled, which suggested that the file might have an endianness issue. To confirm this, I ran:
```
xxd <file_name> | head
```
From the output, I noticed the following line:
```
00000000: e0ff d8ff 464a 1000 0100 4649 0100 0001  ....FJ....FI....
```
The sequence e0ff d8ff immediately stood out because, when interpreted with swapped byte order, it becomes ffe0 ffd8, which corresponds to the FF D8 FF E0 JPEG header. This indicated that the file was likely a JPEG whose bytes were reversed in 4-byte words.

Based on that observation, I attempted to reconstruct the original file by reversing each 4-byte block. I used the following Python script:
```py
data = open("challengefile", "rb").read()
out = bytearray()

for i in range(0, len(data), 4):
    out.append(data[i+3])
    out.append(data[i+2])
    out.append(data[i+1])
    out.append(data[i])     
open("fixed.jpg", "wb").write(out)
```
After running the script, I successfully recovered a valid JPEG image, which contained the flag.
