# TITLE : Wireshark doo dooo do doo...
## Author : Dylan
## Description
Can you find the flag? [shark1.pcapng](https://mercury.picoctf.net/static/4c996ecfb7fbada15a9799511f24dc99/shark1.pcapng).
## Solution
In this challenge, I used Wireshark to analyze the packets. To get the flag, I only needed to look at the packets that have `text/html`
 in the Info column. When I opened one of these packets, I found an encrypted flag. After decrypting it, I obtained the flag.
