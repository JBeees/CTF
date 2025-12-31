# TITLE : PDF by fdpumyp
## Author : K1K9
## Description
Hi, just as we talked during a break, you have this file here and check if something is wrong with it. That's the only thing we found strange with this suspect, I hope there will be a password for his external drive

Bye
## Solution
In this challenge, we were given a PDF file. As an initial step, I used the strings utility to extract printable text from the file. During this process, I discovered a suspicious Base64-encoded string embedded in the output.
```
Q1RGbGVhcm57KV8xbDB3M3kwVW0wMG15MTIzfQ==
```
After decoding the Base64 string, it revealed the flag, completing the challenge.
