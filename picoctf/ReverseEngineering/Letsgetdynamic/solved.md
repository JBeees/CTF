# TITLE : Let's get dynamic
## Author : Ryan Ramseyer
## Description
Can you tell what this file is reading? [chall.S](https://mercury.picoctf.net/static/4c020cde27614e9bad9d80028173541d/chall.S)
## Hints
- Running this in a debugger would be helpful
## Solution
In this challenge, we are given an assembly source file. First, I compiled it using the command below:
```c
gcc -no-pie -o chall chall.S
```
After compiling, I opened the binary in **Ghidra** for analysis. I found the main function as follows:
```c

bool main(void)

{
  int iVar1;
  size_t sVar2;
  long in_FS_OFFSET;
  int local_11c;
  byte local_118 [64];
  char input [64];
  byte local_98 [64];
  byte local_58 [56];
  long local_20;
  
  local_20 = *(long *)(in_FS_OFFSET + 0x28);
  local_98[0] = 0x4b;
  local_98[1] = 0x6f;
  local_98[2] = 0xf8;
  local_98[3] = 0x60;
  local_98[4] = 0xb6;
  local_98[5] = 0x85;
  local_98[6] = 0xbc;
  local_98[7] = 0;
  local_98[8] = 0x5c;
  local_98[9] = 0x49;
  local_98[10] = 0x9c;
  local_98[0xb] = 0x43;
  local_98[0xc] = 0x12;
  local_98[0xd] = 0xdb;
  local_98[0xe] = 0x81;
  local_98[0xf] = 0x16;
  local_98[0x10] = 0xb0;
  local_98[0x11] = 0x82;
  local_98[0x12] = 0x96;
  local_98[0x13] = 0x28;
  local_98[0x14] = 0x6c;
  local_98[0x15] = 0xa7;
  local_98[0x16] = 0xd1;
  local_98[0x17] = 0x42;
  local_98[0x18] = 0xcc;
  local_98[0x19] = 0x6e;
  local_98[0x1a] = 0x37;
  local_98[0x1b] = 0xad;
  local_98[0x1c] = 0xd4;
  local_98[0x1d] = 0x20;
  local_98[0x1e] = 0x6d;
  local_98[0x1f] = 0xf3;
  local_98[0x20] = 0xa2;
  local_98[0x21] = 0xb2;
  local_98[0x22] = 0x37;
  local_98[0x23] = 0xd3;
  local_98[0x24] = 0x15;
  local_98[0x25] = 0xe7;
  local_98[0x26] = 0xf9;
  local_98[0x27] = 0xee;
  local_98[0x28] = 0xf8;
  local_98[0x29] = 0xf0;
  local_98[0x2a] = 0xab;
  local_98[0x2b] = 0x77;
  local_98[0x2c] = 0x9c;
  local_98[0x2d] = 0xbd;
  local_98[0x2e] = 0xfd;
  local_98[0x2f] = 0x11;
  local_98[0x30] = 0x6f;
  local_98[0x31] = 0;
  local_58[0] = 0x28;
  local_58[1] = 0x14;
  local_58[2] = 0x8a;
  local_58[3] = 0x1f;
  local_58[4] = 0xe2;
  local_58[5] = 199;
  local_58[6] = 0xef;
  local_58[7] = 0x6f;
  local_58[8] = 0x23;
  local_58[9] = 0x2a;
  local_58[10] = 0xeb;
  local_58[0xb] = 0x6f;
  local_58[0xc] = 0x60;
  local_58[0xd] = 0xf4;
  local_58[0xe] = 0xff;
  local_58[0xf] = 0x55;
  local_58[0x10] = 0x87;
  local_58[0x11] = 0xee;
  local_58[0x12] = 0xa3;
  local_58[0x13] = 0x44;
  local_58[0x14] = 0x12;
  local_58[0x15] = 0x90;
  local_58[0x16] = 0xa7;
  local_58[0x17] = 0x19;
  local_58[0x18] = 0xf6;
  local_58[0x19] = 0x17;
  local_58[0x1a] = 0x61;
  local_58[0x1b] = 0x90;
  local_58[0x1c] = 0xae;
  local_58[0x1d] = 0x5e;
  local_58[0x1e] = 0x53;
  local_58[0x1f] = 0x8d;
  local_58[0x20] = 0xce;
  local_58[0x21] = 0xf5;
  local_58[0x22] = 0x75;
  local_58[0x23] = 0xd0;
  local_58[0x24] = 0x44;
  local_58[0x25] = 0xa4;
  local_58[0x26] = 0xa0;
  local_58[0x27] = 0x85;
  local_58[0x28] = 0xf1;
  local_58[0x29] = 0xfd;
  local_58[0x2a] = 0xa1;
  local_58[0x2b] = 0x2e;
  local_58[0x2c] = 0x95;
  local_58[0x2d] = 0xe1;
  local_58[0x2e] = 0xf6;
  local_58[0x2f] = 0x48;
  local_58[0x30] = 0x31;
  local_58[0x31] = 0;
  fgets(input,0x31,stdin);
  local_11c = 0;
  while( true ) {
    sVar2 = strlen((char *)local_98);
    if (sVar2 <= (ulong)(long)local_11c) break;
    local_118[local_11c] = (byte)local_11c ^ local_98[local_11c] ^ local_58[local_11c] ^ 0x13;
    local_11c = local_11c + 1;
  }
  iVar1 = memcmp(input,local_118,0x31);
  if (iVar1 == 0) {
    puts("No, that\'s not right.");
  }
  else {
    puts("Correct! You entered the flag.");
  }
  if (local_20 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return iVar1 == 0;
}
```
From this code, we can see that the program performs an XOR operation between two byte arrays (`local_98` and `local_58`), along with the loop index and the constant 0x13. The resulting values are stored in `local_118`.

Finally, it compares our input with the computed array `local_118` using memcmp.

However, notice that if `memcmp` returns 0 (meaning the input matches `local_118`), the program prints:
```
No, that's not right.
```
This is intentionally reversed — a simple anti-debugging trick to confuse solvers. In reality, if your input matches the correct flag, you’ll get the **“No, that’s not right.”** message.

To find the correct flag, I used **GDB** and set a breakpoint at the `memcmp` function. After running the binary and inspecting memory at that point, I found that only part of the flag — **"picoCTF"** — was visible.

This happened because `local_98[7]` equals `0x00` (a null byte), which causes `strlen((char *)local_98)` to stop early, cutting off the rest of the computation.

To test this, I replaced the null byte (0x00) at index 7 with a random nonzero value and reran the process in Python. This allowed the full computation to complete, revealing the entire flag.

Here’s the Python script I used to reconstruct the output:
```py
local_98 = [
    0x4b,0x6f,0xf8,0x60,0xb6,0x85,0xbc,0x10,
    0x5c,0x49,0x9c,0x43,0x12,0xdb,0x81,0x16,
    0xb0,0x82,0x96,0x28,0x6c,0xa7,0xd1,0x42,
    0xcc,0x6e,0x37,0xad,0xd4,0x20,0x6d,0xf3,
    0xa2,0xb2,0x37,0xd3,0x15,0xe7,0xf9,0xee,
    0xf8,0xf0,0xab,0x77,0x9c,0xbd,0xfd,0x11,
    0x6f,0x00
]

local_58 = [
    0x28,0x14,0x8a,0x1f,0xe2,199,0xef,0x6f,
    0x23,0x2a,0xeb,0x6f,0x60,0xf4,0xff,0x55,
    0x87,0xee,0xa3,0x44,0x12,0x90,0xa7,0x19,
    0xf6,0x17,0x61,0x90,0xae,0x5e,0x53,0x8d,
    0xce,0xf5,0x75,0xd0,0x44,0xa4,0xa0,0x85,
    0xf1,0xfd,0xa1,0x2e,0x95,0xe1,0xf6,0x48,
    0x31,0x00
]

# compute local_118
local_118 = []

for i in range(len(local_98)):
    if local_98[i] == 0:
        break
    value = i ^ local_98[i] ^ local_58[i] ^ 0x13
    local_118.append(value)

# print as bytes and as readable ASCII if printable
print("local_118 (hex):", [hex(x) for x in local_118])
print("local_118 (bytes):", bytes(local_118))
print("local_118 (ASCII):", ''.join(chr(x) if 32 <= x <= 126 else '.' for x in local_118))
```
