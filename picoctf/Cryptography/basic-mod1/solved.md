# TITLE : basic-mod1
## Author : Will Hong
## Description 
We found this weird message being passed around on the servers, we think we have a working decryption scheme.
Download the message [here](https://artifacts.picoctf.net/c/128/message.txt).
Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})
## Hints
- Do you know what mod 37 means?
- mod 37 means modulo 37. It gives the remainder of a number after being divided by 37.
## Solution
In this solution, we only need to decrypt the contents of message.txt based on the instructions provided. I used Python to implement the decryption and solve the challenge.
```python
numbers = [165, 248, 94, 346, 299, 73, 198, 221, 313, 137, 205, 87, 336, 110, 186, 69, 223, 213, 216, 216, 177, 138]
flag = ""

for n in numbers:
    temp = n % 37
    if 0 <= temp <= 25:       # 0-25 → A-Z
        flag += chr(65 + temp)
    elif 26 <= temp <= 35:    # 26-35 → 0-9
        flag += str(temp - 26)
    elif temp == 36:          # 36 → _
        flag += '_'

print(flag)
``` 
