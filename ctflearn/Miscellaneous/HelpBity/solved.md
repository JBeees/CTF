# TITLE : Help Bity
## Author : ioancristian
## Description
Bity had the flag for his problem. Unfortunately, his negative friend Noty corrupted it. Help Bity retrieve his flag. He only remembers the first 4 characters of the flag: CTFL. Flag: BUGMdsozc0osx^0r^`vdr1ld|
## Solution
In this challenge, we were given a string and informed that the first four characters of the flag should be CTFL. We were also told to wrap the substring `sozc0o` with backticks (`), indicating that this part required special handling.

I initially attempted to recover the flag using a Python script that alternately incremented and decremented each character’s ASCII value (based on its index). The code used is shown below:
```py
def ascii_decrement(s: str) -> str:
    result = []
    i = 0
    for c in s:
        if i % 2 == 0:
            result.append(chr(ord(c) + 1))
        else :
            result.append(chr(ord(c) - 1))
        i+=1
    return ''.join(result)


# Example usage
text = "BUGMd`sozc0o`sx^0r^`vdr1ld|"
print(text)
decoded = ascii_decrement(text)
print(decoded)
```
Which give me
```
CTHLe_tn{b1nary]1q__wcs0mc}
```
Although the result resembled a flag format, it was clearly incorrect. Based on the known prefix CTFL and common CTF flag patterns, I manually corrected the remaining characters. After adjusting the incorrect symbols and letters, the correct flag was recovered:
```
CTFLearn{b1nary_1s_awes0me}
```
