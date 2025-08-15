# TITLE : substitution2
## Author : Will Hong
## Description
It seems that another encrypted message has been intercepted. The encryptor seems to have learned their lesson though and now there isn't any punctuation! Can you still crack the cipher?
Download the message [here](https://artifacts.picoctf.net/c/112/message.txt).
## Hints
- Try refining your frequency attack, maybe analyzing groups of letters would improve your results?
## Solution
To solve this challenge, you can approach it similarly to the previous [substitution1](https://github.com/JBeees/CTF/tree/main/picoctf/Cryptography/substitution1) challenge. You can use the provided [tool](https://www.101computing.net/mono-alphabetic-substitution-cipher/) to help decode the content. Make sure to follow the lowest line flag format to correctly extract the flag.

