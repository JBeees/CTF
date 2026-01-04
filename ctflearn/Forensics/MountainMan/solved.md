# TITLE : Mountain Man
## Author : kcbowhunter 
## Description
Don't be fooled by two 0xffd9 markers. xor is your friend.
## Solution
In this challenge, we are given a JPEG file. During analysis, I inspected the file using `xxd` and noticed that it contains two `FF D9` markers, which correspond to the **EOI** (End of Image) marker in the JPEG format.
```
0001edd0: ab43 5d03 c115 1c29 19ff d988 9f8d a7ae  .C]....)........
0001ede0: aab9 a5b0 9ea9 bea5 bfbe 94b9 fba8 a0fe  ................
0001edf0: b6ff d9
```
A valid JPEG should contain only one **EOI** marker, so the presence of multiple `FF D9` markers indicates that additional data is hidden after the first **EOI**. JPEG decoders stop parsing at the first `FF D9`, meaning any data that follows is ignored by normal image viewers.
##### Extracting the hidden data

After identifying the first `FF D9`, I extracted the bytes that follow it. The extracted data appears as raw hexadecimal values:
```
88 9f 8d a7 ae aa b9 a5 b0 9e a9 be a5 bf be 94 b9 fb a8 a0 fe b6
```
This data does not resemble readable text or a known file signature, suggesting that it has been obfuscated.
The challenge hint explicitly mentions XOR, which strongly suggests that the hidden data is XOR-encoded. Since XOR operates on raw bytes, I first used CyberChef’s `From Hex` operation to convert the hexadecimal representation into actual binary data.

Next, I applied XOR Brute Force with a key length of 1 byte, which is standard for CTF XOR challenges. CyberChef tested all 256 possible single-byte keys.

During this process, one of the decoded outputs produced readable text that matched a CTF flag format, revealing the flag.

The XOR key used in this case was `cb`
