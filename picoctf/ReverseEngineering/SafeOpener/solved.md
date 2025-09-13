# TITLE : Safe Opener
## Author : Mubarak Mikail
## Description
Can you open this safe?
I forgot the key to my safe but this program is supposed to help me with retrieving the lost key. Can you help me unlock my safe?
Put the password you recover into the picoCTF flag format like:
picoCTF{password}
## Solution
We received a Java file. Inside it there's a variable named `encodedKey` that contains a Base64-encoded string. Decode that string and you will get the flag.
