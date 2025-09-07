# TITLE : keygenme-py
## Author : syreal
## Description
[keygenme-trial.py](https://mercury.picoctf.net/static/9055e7d35f5f4646338a1734aea0dda5/keygenme-trial.py)
## Solution
In this challenge, we were given a .py file, and our task was to determine the value of the variable `key_part_dynamic1_trial`.

To obtain this value, we analyzed a function that verifies the key against the SHA-256 hash of `username_trial`. The relevant code was as follows:
```python
if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
    return False
return True
```
From this, we can see that the program builds `key_part_dynamic1_trial` using specific characters from the SHA-256 digest of the string b"FRASER".

I wrote a script **code.py** to automate this process:
```python
import hashlib

username_trial = b"FRASER"
c = ""
c += hashlib.sha256(username_trial).hexdigest()[4]
c += hashlib.sha256(username_trial).hexdigest()[5]
c += hashlib.sha256(username_trial).hexdigest()[3]
c += hashlib.sha256(username_trial).hexdigest()[6]
c += hashlib.sha256(username_trial).hexdigest()[2]
c += hashlib.sha256(username_trial).hexdigest()[7]
c += hashlib.sha256(username_trial).hexdigest()[1]
c += hashlib.sha256(username_trial).hexdigest()[8]

print(c)
```
Running this script produced the required value of `key_part_dynamic1_trial`.
After combining it with `key_full_template_trial`, we were able to reconstruct the complete key and obtain the flag.
