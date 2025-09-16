# TITLE : packer
## Author : Mubarak Mikail
## Description
Reverse this linux executable?
[binary](https://artifacts.picoctf.net/c_titan/103/out)
## Hints 
- What can we do to reduce the size of a binary after compiling it.
## Solution
In this challenge, I first checked the type of the file using the following command:
```bash
file out
```
The output showed that the file had no section headers. This made me suspect that the file was compressed with UPX. To confirm, I ran:
```bash
strings out | grep upx
```
I found the line:
```bash
$Info: This file is packed with the UPX executable packer http://upx.sf.net $
```
This confirmed my suspicion. I then decompressed the binary using:
```bash
upx -d out
```
After decompression, I obtained a readable binary. I opened it in **Ghidra** to decompile and analyze the code. Looking at the main function, I found the flag, but it was in hex-encoded ASCII format. I decoded it, which gave me the final flag.
