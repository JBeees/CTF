# TITLE : interencdec
## Author : NGIRIMANA Schadrack
## Description
Can you get the real meaning from this file.
Download the file [here](https://artifacts.picoctf.net/c_titan/111/enc_flag).
## Hint
- Engaging in various decoding processes is of utmost importance
## Solution
In this challenge, we are given an enc_flag in Base64:
```
YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzVNR3N5TXpjNWZRPT0nCg==
```
I decoded it using [CyberChef](https://gchq.github.io/CyberChef/) and got:
```
d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg5MGsyMzc5fQ==
```
This is also Base64, so I decoded it again and got:
```
wpjvJAM{jhlzhy_k3jy9wa3k_890k2379}
```
This string is a cipher encrypted with a Caesar shift of +7 (shifted upward). After decoding it, I obtained the flag.
