# TITLE : GDB baby step 3
## Author : LT 'syreal' Jones
## Description
Now for something a little different. 0x2262c96b is loaded into memory in the main function. Examine byte-wise the memory that the constant is loaded in by using the GDB command x/4xb addr. The flag is the four bytes as they are stored in memory. If you find the bytes 0x11 0x22 0x33 0x44 in the memory location, your flag would be: picoCTF{0x11223344}.
Debug this.
## Hints 
- You'll need to breakpoint the instruction after the memory load.
- Use the gdb command x/4xb addr with the memory location as the address addr to examine. GDB manual page.
- Any registers in addr should be prepended with $ like $rbp.
- Don't use square brackets for addr
- What is endianness?
## Solution
In this challenge, we were given a binary file. The description stated that the constant `0x2262c96b` is loaded into memory inside the main function, specifically at this instruction:
```
0x0000000000401115 <+15>:  mov    DWORD PTR [rbp-0x4],0x2262c96b
```
Since we needed to examine the constant byte by byte, I first determined the address of `rbp-0x4`.

I checked the value of `rbp` using:
```
info registers rbp
```
Then I subtracted `0x4` from the value of rbp to get the address where the constant was stored.
Next, I examined 4 bytes at that memory location with:
```
x/4xb 0x7fffffffdb5c
```
The result was:
```
0x7fffffffdb5c:  0x6b  0xc9  0x62  0x22
```
This output shows the constant stored in little-endian order.
Finally, combining the bytes, we get the flag:
```
picoCTF{0x6bc96222}
```
