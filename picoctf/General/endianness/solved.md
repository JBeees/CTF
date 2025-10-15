# TITLE : endianness
## Author : Nana Ama Atombo-Sackey
## Description
Know of little and big endian?
[Source](https://artifacts.picoctf.net/c_titan/116/flag.c)
Additional details will be available after launching your challenge instance.
## Hints
- You might want to check the ASCII table to first find the hexadecimal representation of characters before finding the endianness.
- Read more about how endianness here
## Solution
In this challenge, we were asked to determine the little-endian and big-endian representations of a given word. The provided code included a function that converts a word into both formats. For example, if the word is `city`, its little-endian form is `79746963`, while its big-endian form is `63697479`. You need to apply the same process to the word you receive from the server. If you do it correctly, you’ll obtain the flag.
