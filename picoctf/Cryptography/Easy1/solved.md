# TITLE : Easy1
## Author : Alex Fulton/Danny
## Description
The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a table to help UFJKXQZQUNB with the key of SOLVECRYPTO. Can you use this [table](https://jupiter.challenges.picoctf.org/static/1fd21547c154c678d2dab145c29f1d79/table.txt) to solve it?.
## Hints
- Submit your answer in our flag format. For example, if your answer was 'hello', you would submit 'picoCTF{HELLO}' as the flag.
- Please use all caps for the message.
## Solution
This challenge uses the Vigenère cipher to encrypt the data. It is a method of encrypting alphabetic text using a repeating keyword. It is a polyalphabetic cipher, meaning it applies multiple Caesar ciphers with different shifts instead of just one. To help solve this challenge, I used a [tool](https://cryptii.com/pipes/vigenere-cipher) or you can use the given table to solve this challenge, which helped me retrieve the flag.
